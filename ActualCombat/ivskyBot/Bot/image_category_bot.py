# -*- encoding : utf-8 -*-
# @Author : Fenglchen
from urllib.request import urlopen
from lxml import etree
from ActualCombat.ivskyBot.Tools.tools import Tools


# 主页面url
home_page_url = 'https://www.ivsky.com/tupian/'
# 发送请求获取网页内容
while True:
    try:
        home_page_res = urlopen(home_page_url)
        break
    # 当网页发送拥堵时
    except:
        continue
# 对所得到对内容进行读取
home_page_res = home_page_res.read()
# 对读取后的内容进行解码
home_page_res = home_page_res.decode('utf-8')
# 创建一个主页面的etree
home_page_etr = etree.HTML(home_page_res)
# 图片分类的url
category_urls = home_page_etr.xpath('//div[@class="sort"]/ul/li/a/@href')
# 图片分类的名字
category_names = home_page_etr.xpath('//div[@class="sort"]/ul/li/a/text()')
# 对无用数据进行删除
category_urls.remove('/tupian/')
category_names.remove('所有图片')
# 对所爬取到的图片类别进行写入
Tools.cover_image_category_pool(category_names, category_urls)
# 创建相关类别的文件夹
Tools.create_category_folder(category_names)
