import scrapy


class LolComSpider(scrapy.Spider):
    name = 'lol.com'
    def start_requests(self):
        url = 'http://www.lolgamescdkey.cn/'
        yield scrapy.Request(url=url)

    def parse(self, response):
        print('1')
        for i in range(1000):
            url = 'http://www.lolgamescdkey.cn/'
            yield scrapy.Request(url=url)
