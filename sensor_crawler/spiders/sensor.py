import json
import scrapy
import re
from scrapy.utils.project import get_project_settings


class SensorSpider(scrapy.Spider):
    settings = get_project_settings()

    name = "sensor"
    start_urls = ['http://172.31.251.9:8080/api/table.xml?content=sensortree&passhash=' + settings.get('PRTG_PASSHASH') + '&username=' + settings.get('PRTG_USERNAME') +
                  '&columns=sensor']
    iterator = 'iternodes'  # This is actually unnecessary, since it's the default value
    itertag = 'sensortree'

    def parse(self, response):
        sensors = response.xpath("//sensortree/nodes/group//sensor").getall()
        sflow_sensortype_refor = "<sensortype>sFlow (Custom)</sensortype>"
        ipfix_sensortype_refor = "<sensortype>IPFIX (Custom)</sensortype>"
        sensor_factory_sensortype_refor = "<sensortype>Sensor Factory</sensortype>"
        for ids, sensor in enumerate(sensors):
            if sflow_sensortype_refor in sensor or ipfix_sensortype_refor in sensor or sensor_factory_sensortype_refor in sensor:
            # if sflow_sensortype_refor in sensor or ipfix_sensortype_refor in sensor:
                Sensor_item = {
                    'ids': ids,
                    'name': re.findall("(?:<name.*?>)(.*?)(?:<\\/name>)", sensor),
                    "sensor_id": re.findall("(?:<id.*?>)(.*?)(?:<\\/id>)", sensor),
                    "url": re.findall("(?:<url.*?>)(.*?)(?:<\\/url>)", sensor),
                    "tags": re.findall("(?:<tags.*?>)(.*?)(?:<\\/tags>)", sensor),
                    "status": re.findall("(?:<status.*?>)(.*?)(?:<\\/status>)", sensor),
                    "active": re.findall("(?:<active.*?>)(.*?)(?:<\\/active>)", sensor),
                }
                Sensor_item['channel_url'] = 'http://172.31.251.9:8080/api/table.json?content=channels&output=json&columns=name,' \
                                      'lastvalue_&id=' + str(Sensor_item["sensor_id"]).replace("['", "").replace("']",
                                                                                                   "") + '&username='+ self.settings.get('PRTG_USERNAME') + '&passhash=' + self.settings.get('PRTG_PASSHASH')

                # print(Sensor_item)
                yield scrapy.Request(Sensor_item['channel_url'], meta={'item': Sensor_item}, callback=self.channel_parse)
                yield Sensor_item

    def channel_parse(self, response):
        item = response.meta['item']
        channels = json.loads(response.text)
        for channel in channels['channels']:
            sensor_id = str(item['sensor_id']).replace("['", "").replace("']", "")
            name = channel['name']
            del channel['name']

            cidr_regex = re.compile(r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/([0-9]|[1-2][0-9]|3[0-2]))')
            if cidr_regex.search(name):
                channel_item = {
                    "sensor_id": sensor_id,
                    "name": name,
                    "lastvalue": json.dumps(channel)
                }

                yield channel_item
