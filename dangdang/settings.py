BOT_NAME = "dangdang"

SPIDER_MODULES = ["dangdang.spiders"]
NEWSPIDER_MODULE = "dangdang.spiders"

ITEM_PIPELINES = {
    "dangdang.pipelines.DangdangPipeline": 300,
    "dangdang.pipelines.MySQLStorePipeline": 1,
}
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"

ROBOTSTXT_OBEY = True
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
