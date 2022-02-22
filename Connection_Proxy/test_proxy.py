# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import requests
import time


all_proxies = []
# 对proxy池进行读取
with open('/Users/tempuser/PycharmProjects/python爬虫/Connection_Proxy/Proxy_pool/new_proxy_pool.txt', mode='r') as tp:
    read_all_proxies = tp.readlines()
for proxy in read_all_proxies:
    all_proxies.append(proxy.replace('\n', ''))

bad_proxies = []
# 本机ip
test_res = requests.get('http://httpbin.org/ip')
test_res = test_res.text
print(test_res)
for proxy in all_proxies:
    print(proxy)
    proxy = eval(proxy)
    print(type(proxy))
    count = 0
    while True:
        try:
            if count == 5:
                goal_res = {
                            "origin": "218.68.159.81"
                            }
                break
            goal_res = requests.get('http://httpbin.org/ip', proxies=proxy)
            goal_res = goal_res.text
            break
        except:
            time.sleep(2)
            count = count + 1
            continue
    print(goal_res)
    if goal_res != test_res:
        try:
            # proxy可用
            test_proxy = eval(goal_res)
            print('%s:可用' % proxy)
            with open('/Users/tempuser/PycharmProjects/python爬虫/Connection_Proxy/Proxy_pool/good_proxies.txt', mode='a+')as wgp:
                wgp.write(str(proxy))
                wgp.write('\n')

        except:
            # proxy内内容错误
            print('%s:错误' % proxy)
            with open('/Users/tempuser/PycharmProjects/python爬虫/Connection_Proxy/Proxy_pool/bad_proxies.txt', mode='a+') as wbp:
                wbp.write(str(proxy))
                wbp.write('\n')
    else:
        print('111111111')
        # proxy无法使用
        print('%s:错误' % proxy)
        with open('/Users/tempuser/PycharmProjects/python爬虫/Connection_Proxy/Proxy_pool/bad_proxies.txt',
                  mode='a+') as wbp:
            wbp.write(str(proxy))
            wbp.write('\n')
