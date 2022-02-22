# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import requests
from lxml import etree

# ua = {
#
#     # 'sec-ch-ua-mobile':'?0'
#     # 'sec-ch-ua-platform':'"macOS"'
#     # 'Sec-Fetch-Dest':'document'
#     # 'Sec-Fetch-Mode':'navigate'
#     # 'Sec-Fetch-Site':'none'
#     # 'Sec-Fetch-User':'?1'
#     'Upgrade-Insecure-Requests':'1'
#     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
# }
video_num = 30
while video_num < 40:
    video_url = 'https://e1.monidai.com/20210330/2GOrUdYU/1000kb/hls/lu1MmlQ32880' + str (video_num) + '.ts'
    print(video_url)
    # video_url = ' https://e1.monidai.com/20210330/2GOrUdYU/1000kb/hls/lu1MmlQ3288030.ts'

    video_res = requests.get(video_url)
    # print(type(video_res))
    # video_res = video_res.text
    # print(type(video_res))
    video_res = video_res.content
    # print(type(video_res))
    # video_etree = etree.HTML(video_res)
    # if '404 Not Found' in video_etree.xpath('//title/text()'):
    #     print('下载完成')
    #     break
    print(video_res)
    print(video_num)
    with open('/Users/tempuser/PycharmProjects/python爬虫/ihanjubot/test_video/'+'cs'+'.ts', mode='a+b')as cs:
        cs.write(video_res)
    video_num += 1