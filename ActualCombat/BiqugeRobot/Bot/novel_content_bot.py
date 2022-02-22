# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import requests
from lxml import etree
import gzip
from ActualCombat.BiqugeRobot.Tools.tools import Tools
from ActualCombat.BiqugeRobot.Novels.novel import Novels
import os


def novel_content_bot(goal_novel_name):
    if len(Novels.schedule_book_name) == 0:
        # 创建目标小说txt
        Tools.download_goal_novel(goal_novel_name,'')
    # 获取目标小说路径
    project_path = os.path.dirname('')
    goal_novel_path = goal_novel_name + '.txt'
    file_path = os.path.join(project_path, 'Download', goal_novel_path)
    # 获取目标小说的章节名以及url
    Tools.read_novels_chapters_pool()
    # 判断笔趣阁服务器是否发生等待 0 False
    wait_num = 0
    # 用以控制只输出一次提示
    decide = 1

    # 遍历进行爬取章节内容
    for url in Novels.novel_chapter_url:
        # 获取url
        try:
            # 获取每章的url
            chapter_url = 'https://www.xbiquge.la'+url[2]
        except:
            continue

        if url[3] == '1':
            continue

        # 获取内容
        while True:
            try:
                # 获取目标网页内容
                chapter_res = requests.get(chapter_url)
                break
            except:
                # 发生等待情况
                wait_num += 1
                continue

        # 笔趣阁服务器发生等待
        if wait_num >= 1 and decide == 1:
            decide = 0
            print('笔趣阁网络拥堵！下载时间将会延长！')


        # 解决中文乱码
        chapter_res.encoding = 'utf-8'
        # 进行读取
        chapter_res = chapter_res.text

        # 对读取后的内容进行解压缩以及解码
        try:
            # 如果其中包含压缩文件
            chapter_res = gzip.decompress(chapter_res)
            # 进行解码
            chapter_res = chapter_res.decode()
        # 未包含压缩文件
        except:
           pass

        # 创建一个每章的etree
        chapter_etree = etree.HTML(chapter_res)
        # 目标小说每章的内容
        novel_content = chapter_etree.xpath('//div[@id="content"]/text()')

        # 以追加方式写入
        with open(file_path, mode='a+', encoding='utf-8') as downl:
            # 写入章节数
            downl.write(url[0])
            downl.write('\t')
            # 写入章节题目
            downl.write(url[1])
            downl.write('\n')
            # 写入章节内容
            for _ in novel_content:
                downl.write(_.replace(' ', ' '))
            # 章节分割
            downl.write('\n')
            downl.write('\n')

        # 下载成功每章返回提示
        print(url[0]+' '+url[1]+' '+'下载完成！')
        # 每章下载成功后进行更改状态
        url[3] = '1'
        # 进行更新
        Tools.update_novels_chapters_pool()

