import scrapy
import json
from ..items import ScrapySxrItem


# 添加用户标识为:Baiduspider 为百度爬虫 获取更多权限
headers = {
    'User-Agent': 'Baiduspider'
}

# 读取百家姓文件 用以进行后续步骤中的遍历查找
with open('/Users/tempuser/PycharmProjects/python爬虫/ActualCombat/scrapy_sxr/bai.txt', encoding='utf-8') as r:
    firstnames = r.readlines()
# 对读取百家姓内的数据进行处理 去除'\n'
firstnames = [i.strip() for i in firstnames]


class SxrBotSpider(scrapy.Spider):
    name = 'sxr_bot'
    allowed_domains = ['baidu.com']
    def start_requests(self):
        name_first_index = int(input('请选择爬取姓的下标的开始:'))
        name_list_index = int(input('请选择爬取姓的下标的结尾:'))
        first_num = int(input('请选择爬取的页数开头:'))
        list_num = int(input('请选择爬取的页数结尾:'))
        first_num = first_num * 10
        list_num = list_num * 10
        for index in range(name_first_index, name_list_index + 1):
            firstname = firstnames[index]
            for page_num in range(first_num, list_num + 1, 10):
                url = 'https://sp1.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=%E5%A4%B1%E4%BF%A1%E8%A2%AB%E6%89%A7%E8%A1%8C%E4%BA%BA%E5%90%8D%E5%8D%95&cardNum=&iname=' + firstname + '&areaName=&pn=' + str(page_num) + '&rn=100&from_mid=1&ie=utf-8&oe=utf-8&format=json&t=1632363317807&cb=jQuery1102037220282079843114_1632362748911&_=1632362748913'
                yield scrapy.Request(url=url, headers=headers)

    def parse(self, response):
        # 对获得对响应进行处理并转换为字典类型
        res = json.loads(response.text[47:-2])
        # 在上步处理后的数据进行筛选有用的数据 因为'data'键所对应的值结构为{'data':[{'disp_data':[{xx}]}] } 最终获得的pepo为字典
        for peop in res['data'][0]['disp_data']:
            item = ScrapySxrItem()
            # 获取对应的姓名
            item['name'] = peop['iname']
            # 获取对应的案号
            item['reference_number']= peop['gistId']
            # 获取对应的法院
            item['executive_count'] = peop['gistUnit']
            # 获取对应的地区
            item['province'] = peop['areaName']
            yield item
        pass
