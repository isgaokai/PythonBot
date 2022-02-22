# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import pymysql
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random


# 使用Chrome浏览器
browser = webdriver.Chrome()
# 百度网站
url = 'https://www.baidu.com'
# 发送请求访问
browser.get(url=url)
# 搜索输入框
input_1 = browser.find_element_by_xpath('//*[@id="kw"]')
# 输入搜索条件'失信人'
input_1.send_keys('失信人')
# 随机睡眠1～3秒
time.sleep(random.randint(1, 3))
# 连接数据库
database = pymysql.connect(host='localhost', user='root', password='woaini', database='crawler', port=3306, charset='utf8')
# 创建游标
sor = database.cursor()
# 库内总信息条数
sum_message = 1380
# 爬取100次
for count in range(1, 101):
    # 百度一下按钮
    botton_input = browser.find_element_by_xpath('//*[@id="su"]')
    # 随机睡眠1～3秒
    time.sleep(random.randint(1, 3))
    # 进行点击按钮
    botton_input.click()
    # 显性等待 timeout：60秒 直到locator成立
    locator = (By.XPATH, '//*[@id="1"]/div/div[4]/ul/li')
    WebDriverWait(browser, 60).until(EC.presence_of_element_located(locator))
    # 爬取前100页信息
    for page in range(1, 101):
        # 返回提示
        print('开始获取第%s次,第%s页内容......' % (count, page))
        # 随机睡眠1～3秒
        time.sleep(random.randint(1, 3))
        # 当前页面信息条数
        page_message = 0
        # 一页10人的全部按钮
        bottons = browser.find_elements_by_xpath('//*[@id="1"]/div/div[4]/ul/li')
        # 当前页面数据
        current_page_datas = []
        # 进行数据获取
        for botton in bottons:
            # 随机睡眠0～2秒
            time.sleep(random.randint(0, 2))
            # 点击按钮
            botton.click()
            # 当前数据未存在法定代表人或者负责人姓名一栏
            if '法定代表人或者负责人姓名' not in botton.text:
                # 筛选出有用数据
                temp_list = botton.text.split('\n')[1:6]
                # 进行数据修改
                for index, value in enumerate(temp_list):
                    try:
                        temp_list[index] = value.split('：')[1]
                    except:
                        continue
            # 当前数据存在法定代表人或者负责人姓名一栏
            else:
                # 筛选出有用数据
                temp_list = botton.text.split('\n')[1:7]
                # 删除无用数据
                temp_list.pop(1)
                # 进行数据修改
                for index, value in enumerate(temp_list):
                    try:
                        temp_list[index] = value.split('：')[1]
                    except:
                        continue
            # 转化为元组类型
            temp_tuple = tuple(temp_list)
            # 添加到当前页面数据列表中
            current_page_datas.append(temp_tuple)
            # 当前页面信息条数
            page_message += 1
        # 库内总条数
        sum_message += page_message
        # 当前页数为1
        if page == 1:
            # 下一页按钮
            next_botton = browser.find_element_by_xpath('//*[@id="1"]/div/div[5]/p/span[7]')
            # 进行点击
            next_botton.click()
        # 当前页数不为1
        else:
            # 下一页按钮
            next_botton = browser.find_element_by_xpath('//*[@id="1"]/div/div[5]/p/span[8]')
            # 进行点击
            next_botton.click()
        # 随机睡眠1～2秒
        time.sleep(random.randint(1, 2))
        # sql语句
        sql = 'insert into crawler.people_with_poor_credit values (%s, %s, %s, %s, %s)'
        # 批量插入数据库
        sor.executemany(sql, current_page_datas)
        # 因为对数据库进行修改所以进行提交
        database.commit()
        # 返回提示
        print('第%s次，第%s页信息，共%s条已全部获取！ 当前库内总信息条数:%s！' % (count, page, page_message, sum_message))
        # 写入完成页数
        with open('/ActualCombat/people_with_poor_creditBot/V1/now_page.txt',
                  mode='w') as wnp:
            wnp.write(str(page))
