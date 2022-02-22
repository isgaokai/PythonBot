# -*- encoding : utf-8 -*-
# @Author : Fenglchen
from urllib.request import urlopen
from lxml import etree
from ActualCombat.ivskyBot.Tools.tools import Tools
from ActualCombat.ivskyBot.Image.image import Image
from ActualCombat.ivskyBot.Bot.image_content_bot import image_content_bot

# 读取image_category_pool里面数据
Tools.read_image_category_pool()
# 遍历拿出image的类别以及对应的url
for i in Image.image_category_and_url:
    # 当前页数
    page_count = 1
    # 直到爬取所有页数
    while True:
        # 获取图片类别
        image_category = i[0]
        # 获取图片类别对应的url
        image_category_url = i[1]+'index_' + str(page_count)+'.html'
        # 实现页面翻页
        page_count += 1
        # 获取url中的内容
        while True:
            try:
                image_gallery_res = urlopen(image_category_url)
                break
            # 当网页发生拥堵时
            except:
                continue
        # 对所得到对内容进行读取
        image_gallery_res = image_gallery_res.read()
        # 创建一个image_gallery的etree
        image_gallery_etree = etree.HTML(image_gallery_res)
        # 进行爬取
        try:
            # 图片集的名字
            image_gallery_names = image_gallery_etree.xpath('//ul[@class="ali"]/li/p/a/text()')
            # 图片集的url
            image_gallery_urls = image_gallery_etree.xpath('//ul[@class="ali"]/li/p/a/@href')
        # 当前类别已经全部爬取，跳转下一类别
        except:
            print('%s类别已经全部爬取完毕，进入下一类别爬取！' % image_category)
            break
        print('开始写入啦！z')
        # 进行写入文件
        Tools.cover_image_gallery_pool(image_gallery_names, image_gallery_urls)
        # 执行image_content_bot
        image_content_bot(image_category)
