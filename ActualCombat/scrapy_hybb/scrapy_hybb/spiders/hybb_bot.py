import scrapy
import copy
from ActualCombat.scrapy_hybb.scrapy_hybb.items import ScrapyHybbItem
headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    'Accept': 'text/plain, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1632656379985_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&dyTabStr=&ie=utf-8&sid=&word=%E8%8A%B1%E5%9B%AD%E5%AE%9D%E5%AE%9D',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,zh-HK;q=0.6',
}


class HybbBotSpider(scrapy.Spider):
    name = 'hybb_bot'
    allowed_domains = ['baidu.com']

    def start_requests(self):
        for pn in range(0, 3001, 30):
            url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=9609905268562247974&ipn=rj&ct=201326592&is=&fp=result&queryWord=风景C&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&word=风景C&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&nojc=&pn='+str(pn)+'&rn=30&gsm=1e&1632734881147='
            # url =  'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=8660152244156969137&ipn=rj&ct=201326592&is=&fp=result&queryWord=花园宝宝&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&word=花园宝宝&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&expermode=&nojc=&pn='+str(pn)+'&rn=30&gsm=1e&1632669530211='
            yield scrapy.Request(url=url, headers=headers)

    def parse(self, response):
        all_images = response.text
        all_images = all_images.split(',"')
        test_image = copy.deepcopy(all_images)
        for i in test_image:
            if 'thumbURL' not in i:
                all_images.remove(i)
        all_urls = []
        for image in all_images:
            all_urls.append(image.split('":"')[1][:-1])
        item = ScrapyHybbItem()
        item['image_urls'] = all_urls
        yield item
