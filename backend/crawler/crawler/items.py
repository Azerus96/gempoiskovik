import scrapy

class PageItem(scrapy.Item):
    url = scrapy.Field()
    content = scrapy.Field()
