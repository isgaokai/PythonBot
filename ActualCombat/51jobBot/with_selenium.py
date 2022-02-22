# -*- encoding : utf-8 -*-
# @Author : Fenglchen
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import random


# 使用Chrome浏览器
browser = webdriver.Chrome()
# 目标url
url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
# 读取是否存在中断
with open('/Users/tempuser/PycharmProjects/python爬虫/ActualCombat/51jobBot/now_page.txt',
          mode='r') as rnp:
    continue_page = rnp.read()
# 发送请求访问
browser.get(url)
# 显性等待
locator = (By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div[4]/div[2]/div/div/div/span[3]')
WebDriverWait(browser, 60).until(EC.presence_of_element_located(locator))
if continue_page != '':
    go_to_url_input = browser.find_element_by_xpath('//*[@id="jump_page"]')
    go_to_url_input.clear()
    go_to_url_input.send_keys(continue_page)
    go_to_url_botton = browser.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div[4]/div[2]/div/div/div/span[3]')
    # 随机睡眠1～3秒
    time.sleep(random.randint(1, 3))
    go_to_url_botton.click()
# 无加载页面
if continue_page == '':
    continue_page = 1
for page in range(int(continue_page), 1078):
    # 返回提示
    print('开始获取第%s页内容......' % page)
    # 随机睡眠3～5秒
    time.sleep(random.randint(3, 5))
    # 写入当前爬取页面
    with open('/Users/tempuser/PycharmProjects/python爬虫/ActualCombat/51jobBot/now_page.txt',
              mode='w') as wnp:
        wnp.write(str(page))
    # 返回提示
    print('第%s页内容获取成功！' % page)
    # 下一页按钮
    next_botton = browser.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div[4]/div[2]/div/div/div/ul/li[8]')
    # 随机睡眠1～3秒
    time.sleep(random.randint(1, 3))
    # 点击按钮
    next_botton.click()
