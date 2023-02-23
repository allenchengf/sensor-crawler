import logging
from twisted.enterprise import adbapi


class PrtgCrawlerPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_crawler(cls, sensor_crawler):
        dbparams = {
            'host': sensor_crawler.settings['MYSQL_HOST'],
            'user': sensor_crawler.settings['MYSQL_USER'],
            'passwd': sensor_crawler.settings['MYSQL_PWD'],
            'db': sensor_crawler.settings['MYSQL_DB'],
            'port': sensor_crawler.settings['MYSQL_PORT'],
            'charset': sensor_crawler.settings['MYSQL_CHARSET']
        }
        dbpool = adbapi.ConnectionPool('pymysql', **dbparams)
        return cls(dbpool)

    def process_item(self, item, spider):
        if "url" in item:
            # 入庫
            query = self.dbpool.runInteraction(
                self.insert_db,
                item
            )
            query.addErrback(
                self.insert_err,
                item
            )
        return item

    def insert_err(self, failure, item):
        print(failure, 'fail')  # , item)

    def insert_db(self, cursor, item):
        insert_sql = """
                        insert into sensors( 
                        name, 
                        sensor_id, 
                        url, 
                        tags, 
                        status,
                        active)
                        values (%s, %s, %s, %s, %s, %s)
                        """
        params = (item['name'],
                  item['sensor_id'],
                  item['url'],
                  item['tags'],
                  item['status'],
                  item['active'])
        cursor.execute(insert_sql, params)

    def open_spider(self, spider):
        logging.info('start crawler.')
        truncate_sql = 'truncate table sensors'
        self.dbpool.runOperation(truncate_sql)
        print('truncate sensors table.')

    def close_spider(self, spider):
        self.dbpool.close()
