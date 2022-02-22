# -*- encoding : utf-8 -*-
# @Author : Fenglchen
from urllib.request import urlopen
from lxml import etree
from ActualCombat.ivskyBot.Tools.tools import Tools
from ActualCombat.ivskyBot.Image.image import Image


# 图片内容爬取bot
def image_content_bot(image_category):
    # 读取image_gallery_pool
    Tools.read_image_gallery_pool()
    # 遍历拿出图片集以及对应的url
    for i in Image.image_gallery_and_url:
        # 下载图片个数
        image_success_num = 0
        # 获取图片集的名字
        image_gallery_name = i[0]
        # 获取图片集对应的url
        image_gallery_url = i[1]
        # 创建对应的文件夹
        try:
            Tools.create_imagr_gallert_folder(image_category, image_gallery_name)
        # 对应文件夹已经存在
        except:
            pass
        # 对用户返回提示
        print('爬取%s中的图片中......' % image_gallery_name)
        # 获取url中的内容
        while True:
            try:
                image_content_res = urlopen(image_gallery_url)
                break
            # 当网页发生拥堵时
            except:
                continue
        # 对所得到对内容进行读取
        image_content_res = image_content_res.read()
        # 对读取后的内容进行解码
        image_content_res = image_content_res.decode()
        # 创建一个image_content对etree
        image_content_etree = etree.HTML(image_content_res)
        # 图片内容的名字
        image_content_names = image_content_etree.xpath('//div[@class="left"]/ul/li/div/a/img/@alt')
        # 图片对应的src
        image_content_urls = image_content_etree.xpath('//div[@class="left"]/ul/li/div/a/img/@src')
        # 进行下载相对应的图片
        for name, url in zip(image_content_names, image_content_urls):
            image_success_num += 1
            # 进行格式补充
            url = 'https:/' + url[1:]
            name = name + '(' + str(image_success_num) + ')'
            print('图片：%s 下载中......' % name)
            # 进行下载
            if Tools.download_image(image_category, image_gallery_name, name, url) is True:
                print('图片：%s 下载成功！' % name)
        print('%s中的图片下载完成 共下载成功：%s张图片' % (image_gallery_name, image_success_num))
