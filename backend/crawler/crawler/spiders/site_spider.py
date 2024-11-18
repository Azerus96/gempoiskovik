import scrapy
from crawler.items import PageItem
from urllib.parse import urlparse

class SiteSpider(scrapy.Spider):
    name = "site"

    def __init__(self, start_urls=None, *args, **kwargs):
        super(SiteSpider, self).__init__(*args, **kwargs)
        self.allowed_domains = [urlparse(start_urls).netloc]
        self.start_urls = [start_urls]

    def parse(self, response):
        item = PageItem()
        item['url'] = response.url
        item['content'] = response.text
        yield item

        for link in response.css('a::attr(href)'):
            next_page = response.urljoin(link.get())
            if urlparse(next_page).netloc == self.allowed_domains[0]:
                yield scrapy.Request(next_page, callback=self.parse)
