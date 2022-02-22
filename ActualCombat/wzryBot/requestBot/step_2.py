# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import os
import requests
from lxml import etree

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    'referer': 'https://pvp.qq.com/raiders/',
}


with open('all_urls.txt', mode='r') as rru:
    dummy = rru.read()
all_urls = dummy.split('\n')

for url in all_urls:
    response = requests.get(url=url, headers=headers)
    response = response.content.decode('GBK')
