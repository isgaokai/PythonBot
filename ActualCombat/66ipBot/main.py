# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import requests
from lxml import etree

test_url = 'http://httpbin.org/ip'
test_ip = requests.get(url=test_url)
for i in range(1, 19):
    target_url = 'http://www.66ip.cn/areaindex_35/' + str(i) + '.html'
    res = requests.get(target_url)
    res = res.content.decode('gb2312')
    etr = etree.HTML(res)
    target_ips = etr.xpath('//div[@id="footer"]/div/table/tr/td[1]/text()')[1:]
    target_ports = etr.xpath('//div[@id="footer"]/div/table/tr/td[2]/text()')[1:]
    for ip, port in zip(target_ips, target_ports):
        proxy = {
            'http':'http://'+ip+':'+port
        }
        print(proxy)
        try:
            proxy_ip = requests.get(url=test_url, proxies=proxy, timeout =5)
        except:
            print('跳过')
            continue

        try:
            with open('/connection_proxy/Proxy_pool/proxy_pool.txt', mode='a+',
                      encoding='utf-8') as dw:
                dw.write(str(proxy))
                dw.write('\n')
        except:
            print('内容错误')
            pass

        # if proxy_ip.text != test_ip.text and type(proxy_ip) == dict:
        #     print('666')
        #     print(type(proxy))
        #     print(proxy_ip.text)
        #     try:
        #         with open('/Users/tempuser/PycharmProjects/python爬虫/connection_proxy/Proxy_pool/proxy_pool.txt', mode='a+', encoding='utf-8') as dw:
        #             dw.write(str(proxy))
        #             dw.write('\n')
        #     except:
        #         print('内容错误')
        #         pass
        # else:
        #     print('%s不行' % ip)
