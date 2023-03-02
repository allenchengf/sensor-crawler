# Scrapy settings for sensor_crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "sensor_crawler"

SPIDER_MODULES = ["sensor_crawler.spiders"]
NEWSPIDER_MODULE = "sensor_crawler.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "sensor_crawler (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 100

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0

# The download delay setting will honor only one of:

CONCURRENT_REQUESTS_PER_DOMAIN = 100
CONCURRENT_REQUESTS_PER_IP = 100

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "sensor_crawler.middlewares.SensorCrawlerSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "sensor_crawler.middlewares.SensorCrawlerDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'sensor_crawler.pipelines.PrtgCrawlerPipeline': 300,
   'sensor_crawler.channel_pipelines.ChannelCrawlerPipeline': 301,
   'sensor_crawler.menu_pipelines.MenuPipeline': 303
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True

# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 100
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = True

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

DOWNLOAD_TIMEOUT = 30

# MySQL Setting
MYSQL_HOST = '10.88.55.121'
MYSQL_USER = 'rdadmin'
MYSQL_PWD = 'Kz8Zq)Rod^5qeZML'
MYSQL_DB = 'billing'
MYSQL_PORT = 3306
MYSQL_CHARSET = 'utf8mb4'
# MYSQL_HOST = '127.0.0.1'
# MYSQL_USER = 'root'
# MYSQL_PWD = 'root'
# MYSQL_DB = 'billing'
# MYSQL_PORT = 3306
# MYSQL_CHARSET = 'utf8mb4'

# PRTG CONFIG
PRTG_USERNAME = 'ict.monitor'
PRTG_PASSHASH = '3168990700'

# REDIS SETTING
REDIS_HOST ='10.88.55.123'
REDIS_PORT =6379
REDIS_DB_INDEX = 0
REDIS_PASSWORD = ''
# REDIS_HOST ='localhost'
# REDIS_PORT =6379
# REDIS_DB_INDEX = 0
# REDIS_PASSWORD = ''
