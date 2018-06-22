# -*- coding: utf-8 -*-

# Scrapy settings for MPspider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'MPspider'

SPIDER_MODULES = ['MPspider.spiders']
NEWSPIDER_MODULE = 'MPspider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'MPspider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#     'MPspider.middlewares.SeleniumMiddleware': 543,
# }

SPIDER_MIDDLEWARES = {
    'MPspider.middlewares.MpspiderAgentMiddleware': 543,
}


# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'MPspider.middlewares.SeleniumMiddleware': 543,
#    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#     'MPspider.pipelines.MpspiderPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# ---------- Mysql数据库的配置信息 ----------
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'mpspider'  # 数据库名字，请修改
MYSQL_USER = 'root'  # 数据库账号，请修改
MYSQL_PASSWD = '123456'  # 数据库密码，请修改
MYSQL_PORT = 3306  # 数据库端口，在dbhelper中使用

# ----------- selenium参数配置 -------------
SELENIUM_TIMEOUT = 25  # selenium浏览器的超时时间，单位秒
LOAD_IMAGE = False  # 是否下载图片
WINDOW_HEIGHT = 900  # 浏览器窗口大小
WINDOW_WIDTH = 900

# ----------- 要搜索的微信公众号 -------------
SEARCH_ITEMS = ['GQ实验室', '中国经济学人']

# ----------- 设置UserAgent ----------------
USER_AGENT = [
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12A365   "
    "MicroMessenger/5.4.1 NetType/WIFI",
    "Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; Chitanda/Akari) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 "
    "Mobile Safari/534.30 MicroMessenger/6.0.0.58_r884092.501 NetType/WIFI "
]
