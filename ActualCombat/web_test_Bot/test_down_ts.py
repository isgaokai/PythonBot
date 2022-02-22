# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import requests
from web_test_Bot.main import test_list

count = 0
for i in test_list:
    test_url = i
    test_res = requests.get(test_url)
    test_res = test_res.content
    with open('/Users/tempuser/PycharmProjects/python爬虫/web_test_Bot/test_download/test.mp4', mode='a+b') as ts:
        ts.write(test_res)
    count += 1
    w = 'ts{}'.format(count)+'下载成功！'.rjust(15, "*")
    print(w)
