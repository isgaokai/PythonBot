# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import requests


test_url = 'http://httpbin.org/ip'
test_ip = requests.get(url=test_url)
goal_url = 'http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=1fb319f974c540658cd4be2e89254c9a&orderno=YZ20219163721juZzLy&returnType=1&count=1'
print(goal_url)
goal_res = requests.get(goal_url)
goal_res = goal_res.text
print(goal_res)
ip_li = goal_res.split()
print(ip_li)
for i in ip_li:

    proxy = {
        'http':'http://'+i
    }
    print(proxy)
    taeget_ip = requests.get('http://httpbin.org/ip', proxies = proxy)
    print(taeget_ip.text)
    if taeget_ip.text != test_ip.text:
        print('%s 可用'% i)
    else:
        print('不可用')