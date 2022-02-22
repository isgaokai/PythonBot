# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import requests

url = 'https://vod3.bdzybf3.com/20210412/xATmikPY/1000kb/hls/index.m3u8'
res = requests.get(url)
print(res.text)
