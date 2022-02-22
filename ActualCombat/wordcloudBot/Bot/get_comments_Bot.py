# -*- encoding : utf-8 -*-
# @Author : Fenglchen
from selenium import webdriver
import time

# 使用Chrom浏览器
browser = webdriver.Chrome()
# 目标url
url = 'https://music.163.com/#/song?id=29019227'
# 对目标页面进行访问
browser.get(url)
# 休息1秒
time.sleep(1)
# 切换到g_iframe框架
browser.switch_to_frame("contentFrame")
# 当前库内总共评论数
sum_comments = 0
all_usernames = []
# 对前3000页的评论进行爬取
for page in range(1, 3001):
    print('开始获取第%s页内容......' % page)
    comments_count = 0
    # 休息1秒
    time.sleep(1)
    # 当前页面的所有评论
    comments = browser.find_elements_by_xpath('//div[@class="itm"]/div[2]/div[1]/div')
    # 因为在第一页评论时会有精彩评论，所以进行屏蔽
    if page == 1:
        comments = comments[16:]

    # 写入文件
    with open('//Users/tempuser/PycharmProjects/python爬虫/ActualCombat/wordcloudBot/Pool/new_comments_pool.txt',
              mode='a+') as wtcp:
        # 遍历写入当前页面的全部评论
        for comment in comments:
            # 进行读取
            comment = comment.text
            try:
                # 数据处理
                comment_temp = comment.split('：')
                # 当前评论用户名
                now_username = comment_temp[0]
                # 一个用户仅可评论一次
                if now_username in all_usernames:
                    continue
                print(comment)
                # 添加新的用户名
                all_usernames.append(now_username)
                goal_comment = comment_temp[1]
                # 对当前页面评论进行计数
                comments_count += 1
                # 写入评论
                wtcp.write(goal_comment)
                wtcp.write('\n')
            except:
                pass

    # 返回提示
    sum_comments += comments_count
    print('第%s页评论，共%s条已全部获取！ 当前库内总评论数:%s！' % (page, comments_count, sum_comments))
    # 记录页数
    with open('/Users/tempuser/PycharmProjects/python爬虫/ActualCombat/wordcloudBot/Pool/target_page.txt',
              mode='w') as wtp:
        wtp.write(str(page))
        wtp.write('\n')

    # 记录用户名
    with open('/Users/tempuser/PycharmProjects/python爬虫/ActualCombat/wordcloudBot/Pool/all_usernames_pool.txt',
              mode='w', encoding='gbk') as waup:
        for username in all_usernames:
            waup.write(username)
            waup.write('\n')

    # 休息2秒
    time.sleep(2)

    # 点击下一页
    while True:
        try:
            # 上一页与下一页按钮类明前四位一样
            bottons = browser.find_elements_by_class_name('zbtn')
            # 获取下一页按钮
            next_botton = bottons[1]
            # 休息1秒
            time.sleep(1)
            # 点击按钮
            next_botton.click()
            break
        except:
            continue

