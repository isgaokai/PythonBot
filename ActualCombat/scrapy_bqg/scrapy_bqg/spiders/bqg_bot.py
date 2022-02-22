import scrapy
from ActualCombat.scrapy_bqg.Tools.tools import Tools
from lxml import etree
from ActualCombat.scrapy_bqg.scrapy_bqg.items import ScrapyBqgItem

# 添加用户标识为:Baiduspider 为百度爬虫 获取更多权限
headers = {
    'User-Agent': 'Baiduspider'
}


class BqgBotSpider(scrapy.Spider):

    allowed_domains = ['xbiquge.la']
    all_novels = Tools.read_all_novels()
    select_novel = input('请选择您想要下载的图书:')
    if Tools.check_goal_novel(select_novel, novels=all_novels):
        goal_start_url = all_novels[select_novel]
        Tools.create_goal_file(select_novel)
    else:
        print('抱歉！笔趣阁当前未收录！')

    name = 'bqg_bot'

    start_urls = [goal_start_url]

    def parse(self, response):
        # 小说的响应
        novel_res = response.text
        # 创建一个章节的etree
        novel_etree = etree.HTML(novel_res)
        # 目标小说每章章节的url
        novel_chapters_url = novel_etree.xpath('//div[@id="list"]/dl/dd/a/@href')
        for url in novel_chapters_url:
            goal_url = 'https://www.xbiquge.la'+url
            test_name = url.split('/')[3]
            test_name = test_name.split('.')[0]
            yield scrapy.Request(url=goal_url, callback=self.parse_content, headers=headers,meta={'single_name':test_name})

    def parse_content(self, response):
        single_name = response.meta['single_name']
        chapter_etree = etree.HTML(response.text)
        # 目标小说每章的内容
        novel_content = chapter_etree.xpath('//div[@id="content"]/text()')
        item = ScrapyBqgItem()
        item['name'] = single_name
        item['content'] = novel_content
        item['select_novel'] = BqgBotSpider.select_novel
        yield item
