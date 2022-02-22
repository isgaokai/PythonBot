# -*- encoding : utf-8 -*-
# @Author : Fenglchen
from urllib.request import urlopen
from lxml import etree
import gzip

url = 'https://www.ivsky.com/tupian/'
while True:
    try:
        res = urlopen(url)
        break
    except:
        print('1')
        continue
res = res.read()
res = res.decode('utf-8')
print(res)
etr = etree.HTML(res)
goal = etr.xpath('//div[@class="sort"]/ul/li/a/@href')
# goal_temp = etr.xpath('//div[@class="htag"]/a/text()')
print(goal)
# print(goal_temp)
