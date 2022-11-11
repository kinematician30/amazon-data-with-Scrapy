import scrapy


class TripadvCrwlSpider(scrapy.Spider):
    name = 'tripadv_crwl'
    allowed_domains = ['www.tripadvisor.com']
    start_urls = ['http://www.tripadvisor.com/']

    def parse(self, response):
        pass
