import scrapy
from lxml import etree
from dangdang.items import DangdangItem


class DangdangspiderSpider(scrapy.Spider):
    name = "dangdangSpider"
    allowed_domains = ["dangdang.com"]
    start_urls = ["https://category.dangdang.com/pg1-cp01.01.02.00.00.00.html"]


    def parse(self, response):
        mytree = etree.HTML(response.text)
        book_list = mytree.xpath('//ul[@class="bigimg"]/li')

        for book in book_list:

            
            name = book.xpath('.//a[@title]/@title')
            name = name[0].strip() if name else "N/A"

            price = book.xpath('.//span[@class="search_now_price"]/text()')
            price = price[0].strip() if price else "N/A"

            press = book.xpath('.//p[@class="search_book_author"]/span/a/text()')
            press = press[-1].strip() if press else "N/A"

            content = book.xpath('.//p[@class="detail"]/text()')
            content = ' '.join([d.strip() for d in content]).strip() if content else "N/A"

            item = DangdangItem()
            item["name"] = name
            item["price"] = price
            item["press"] = press
            item["content"] = content

            yield item
