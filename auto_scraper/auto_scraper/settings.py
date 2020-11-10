BOT_NAME = 'auto_scraper'

SPIDER_MODULES = ['auto_scraper.spiders']
NEWSPIDER_MODULE = 'auto_scraper.spiders'


DUPEFILTER = True
# Disable cookies (enabled by default)
COOKIES_ENABLED = False
RANDOMIZE_DOWNLOAD_DELAY = True
SCHEDULER_ORDER = 'DFO'

# Crawlera settings
CRAWLERA_ENABLED = True
CRAWLERA_PRESERVE_DELAY = False

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

HTTPCACHE_ENABLED = True

DOWNLOAD_DELAY = 1
DOWNLOAD_TIMEOUT = 100

DOWNLOADER_MIDDLEWARES = {
    # 'auto_scraper.middlewares.CustomRetryMiddleware': 120,
    'scrapy_crawlera.CrawleraMiddleware': 610,
}

ITEM_PIPELINES = {
   'auto_scraper.pipelines.CsvWriterPipeline': 350,
}

