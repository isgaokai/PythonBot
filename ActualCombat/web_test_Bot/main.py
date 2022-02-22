# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import requests
import copy
from lxml import etree


test_url = 'https://new.iskcd.com/20210915/w3qUoSDC/1835kb/hls/playlist.m3u8'
test_res = requests.get(test_url)
test_res = test_res.text
test_list = test_res.split()
# while True:
#     try:
#         test_list.remove('#EXTINF:2.002,')
#         continue
#     except:
#         break\
test_list_temp = copy.deepcopy(test_list)
for i in test_list_temp:
    # print(i)
    if '#EX' in i:
        test_list.remove(i)
test_list = test_list[2:]
print(test_list)

# test_list = test_list[3:]
# print(test_list)
