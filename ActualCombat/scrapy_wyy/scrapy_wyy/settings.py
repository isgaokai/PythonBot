# Scrapy settings for scrapy_wyy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapy_wyy'

SPIDER_MODULES = ['scrapy_wyy.spiders']
NEWSPIDER_MODULE = 'scrapy_wyy.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_wyy (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'authority': 'music.163.com',
    'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'iframe',
    'referer': 'https://music.163.com/',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,zh-HK;q=0.6',
    'cookie': '_iuqxldmzr_=32; _ntes_nnid=befcfe3de664bd73bca0cd5fe7636bb2,1610967449275; _ntes_nuid=befcfe3de664bd73bca0cd5fe7636bb2; NMTID=00OqSyjGOxY0qJubU0ZqINes-M1F9EAAAF3FSR_IA; WM_TID=esfNxYaZfbRBBUVBFAN6blMyWXDQXTh1; WEVNSM=1.0.0; WNMCID=mvvpzz.1632278674817.01.0; WM_NI=1ZLStNoXDy%2BcyM4B34nGvXWsIoSF5GMPrEw2cc6l2Flmryn3djj5Q4nNPy9JeGYX2qjgiJmt3kv75Y1KSBh9CyhFLdNcCNox8dh%2F%2B1Ci2zpPEosi66R263y52zo8RFCdZFQ%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb3c24683948392ae69f38e8fb3c14f928e9ebaf53492edafa4fb809089f7abe12af0fea7c3b92af38684b4f746ad888c9aaa69bb93fca3b240ae99bab9d6798bb19da7b84d8f90bea6f63aa1bdfa8db14eb0b3be9aed39a8b6a6d6d440ae92a09abc42a79997b9b17baab9a7abf080f1b5bad8b853f3959da3eb3381a7a8a7cf708ebd8dafee74fcbca8d0aa3b81b7fe9bf35c87b1bd8ab53e92eefad4fc3ff2a6a1d9d14e81bc96a7d437e2a3; ntes_kaola_ad=1; JSESSIONID-WYYY=P69o9tyY2hOjpsRJC%2FwKErYZHgC%2FIqkAl46rlWEpoZzt8FxK6TK0akafQSh9ksSE6ATyIyjYe9Kv%5CEPZaD0C5yfnPyMDZTdGo7zzYvhP1OeEMZTzeYD3PkrwR6miaBvbIH5aTHwDIxaeCHSXQ91Y%2F45UdbT2pU3bEx%2BCF6abgDc0%2FARA%3A1632817627026',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'scrapy_wyy.middlewares.ScrapyWyySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'scrapy_wyy.middlewares.ScrapyWyyDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'scrapy_wyy.pipelines.ScrapyWyyPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
