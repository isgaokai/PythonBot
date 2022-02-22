import scrapy


class SbjBotSpider(scrapy.Spider):
    name = 'sbj_bot'
    allowed_domains = ['gov.cn']
    start_urls = ['http://wsgg.sbj.cnipa.gov.cn:9080/tmann/annInfoView/annSearch.html?annNum=1760']

    def parse(self, response):
        print(response.text)
        pass

