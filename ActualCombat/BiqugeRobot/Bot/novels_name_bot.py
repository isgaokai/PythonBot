# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import requests
from lxml import etree
import gzip
from ActualCombat.BiqugeRobot.Tools.tools import Tools


# 全部小说页面的url
novels_url = 'https://www.xbiquge.la/xiaoshuodaquan/'

while True:
    try:
        # 发送请求获取网页内容
        novels_res = requests.get(novels_url)
        break
    except:
        continue

# 对所得到对内容进行读取
novels_res = novels_res.text
print(novels_res)

# 对读取后的内容进行解压缩以及解码
try:
    # 如果其中包含压缩文件
    novels_res = gzip.decompress(novels_res)
    # 进行解码
    novels_res = novels_res.decode()
# 未包含压缩文件
except:
    pass

# 创建一个全部小说页面的etree
novels_etree = etree.HTML(novels_res)
# 小说的书名
novels_name = novels_etree.xpath('//div[@class="novellist"]/ul/li/a/text()')
# 小说url
novels_url = novels_etree.xpath('//div[@class="novellist"]/ul/li/a/@href')
# 写入文件
Tools.cover_novels_name_pool(novels_name, novels_url)
