import scrapy


class DangdangItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    press = scrapy.Field()
    content = scrapy.Field()