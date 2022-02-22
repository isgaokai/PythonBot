# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import requests

pr = {'http': 'http://175.7.199.166:3256'}
print(pr)
url = 'http://httpbin.org/ip'
res = requests.get(url=url, proxies=pr)
print(res)
print(type(res))
print(res.text)
try:
    a = eval(res.text)
    print(type(a))
except:
    print('我不对')
    print(type(res.text))
print(len(res.text))
print(type(res.text))
