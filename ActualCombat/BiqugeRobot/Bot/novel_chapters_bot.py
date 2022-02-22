# -*- encoding : utf-8 -*-
# @Author : Fenglchen
from urllib.request import urlopen
import requests
from lxml import etree
import gzip
from ActualCombat.BiqugeRobot.Tools.tools import Tools
from ActualCombat.BiqugeRobot.Bot.novel_content_bot import novel_content_bot


def novel_chapters_bot(goal_novel_name, result):

    # 获取需要下载小说的url
    novel_url = result

    while True:
        try:
            # 获取目标小说网页内容
            novel_res = requests.get(novel_url)
            break
        except:
            continue

    # 解决中文乱码
    novel_res.encoding = 'utf-8'
    # 进行读取
    novel_res = novel_res.text

    # 对读取后的内容进行解压缩以及解码
    try:
        # 如果其中包含压缩文件
        novel_res = gzip.decompress(novel_res)
        # 进行解码
        novel_res = novel_res.decode()
    # 未包含压缩文件
    except:
        pass

    # 创建一个章节的etree
    novel_etree = etree.HTML(novel_res)
    # 目标小说的章节
    novel_chapters = novel_etree.xpath('//div[@id="list"]/dl/dd/a/text()')
    # 目标小说每章章节的url
    novel_chapters_url = novel_etree.xpath('//div[@id="list"]/dl/dd/a/@href')
    # 写入 novels_chapters_pool
    Tools.cover_novels_chapters_pool(novel_chapters, novel_chapters_url)
    # 启动内容爬取bot
    novel_content_bot(goal_novel_name)
