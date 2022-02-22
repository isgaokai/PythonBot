# -*- encoding : utf-8 -*-
# @Author : Fenglchen
a = []
with open('/Users/tempuser/PycharmProjects/python爬虫/connection_proxy/Proxy_pool/proxy_pool.txt', mode='r') as dm:
    all = dm.readlines()
    print(all)
for i in all:
    a.append(i.replace('\n', ''))
print(a)
print(len(a))
a = set(a)
print(a)
print(len(a))
with open('/Users/tempuser/PycharmProjects/python爬虫/connection_proxy/Proxy_pool/new_proxy_pool.txt', mode='w') as dm:
    for i in a:
        dm.write(i)
        dm.write('\n')