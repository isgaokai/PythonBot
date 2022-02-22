# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import threadpool
import requests
from lxml import etree


# 伪装成百度爬虫
headers = {
    'User-agent': 'Baiduspider'
}

# 调度器类
class Scheduler:
    # 构造函数
    def __init__(self):
        # 存放所有的url
        self.all_ulrs = []

    # 定义方法 往all_urls里存放url
    def put_url_in_all_urls(self, url):
        # 当前被存放的url不在请求过的url中以及未保存过该url
        if url not in self.all_ulrs:
            # 进行添加
            self.all_ulrs.append(url)

    # 定义方法 和all_urls中拿出一条url
    def get_url_from_all_urls(self):
        return self.all_ulrs.pop()


def a():
    for i in range(100):
        url = 'https://www.baidu.com/'
        # 发送请求获取响应
        response = requests.get(url, headers=headers, timeout=3)
        # 进行解码
        response = response.content.decode()
        # 创建一个etree对象
        res_etree = etree.HTML(response)
        # 当前页面内存在的所有url
        now_page_urls = res_etree.xpath('//a/@href')
        for url_n in now_page_urls:
            Scheduler.put_url_in_all_urls(url_n)
            print('放入了%s' % url_n)


def b():
    for i in range(100):
        print(Scheduler.get_url_from_all_urls())


if __name__ == '__main__':
    pool_size = 10
    pool = threadpool.ThreadPool(pool_size)
    reqs = threadpool.makeRequests(a, b)
    [pool.putRequest(req) for req in reqs]
    pool.wait()
