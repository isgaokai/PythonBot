# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import pymysql
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random
from chaojiying import check_im
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# 连接数据库
database = pymysql.connect(host='localhost', user='root', password='woaini', database='crawler', port=3306, charset='utf8')
# 创建游标
sor = database.cursor()
# desired_capabilities = DesiredCapabilities.CHROME
# desired_capabilities["pageLoadStrategy"] = "none"
chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_argument("--proxy-server=http://119.115.237.139:4256")
# chrome_options=chrome_opt
# 使用Chrome浏览器
browser = webdriver.Chrome()
# 百度网站
url = 'http://sbj.cnipa.gov.cn/sbcx/'
# browser.proxies = {'http': 'http://222.76.66.212:4256'}
# 发送请求访问
browser.get(url=url)
# class Tools:x
#     @staticmethod


def wait(path):
    if browser.find_element_by_xpath(path):
        return True
    return False


locator = (By.XPATH, '/html/body/div/div[5]/div[1]/div[1]/div/p[4]/a')
WebDriverWait(browser, 2, 0.5).until(EC.element_to_be_clickable(locator))
# 我接收按钮并点击
botton_1 = browser.find_element_by_xpath('/html/body/div/div[5]/div[1]/div[1]/div/p[4]/a')
botton_1.click()
# class button():
#     def __call__(self, browser):
#         if browser.find_element_by_xpath('//*[@id="submitForm"]/div/div[1]/table/tbody/tr[2]/td[2]/div/input'):
#             return True
#         else:
#             return False
# WebDriverWait(browser, 2, 0.5).until(wait('/html/body/div[3]/div[1]/ul/li[2]/table')
locator = (By.XPATH, '/html/body/div[3]/div[1]/ul/li[2]/table')
WebDriverWait(browser, 2, 0.5).until(EC.element_to_be_clickable(locator))
# /html/body/div[3]/div[1]/ul/li[4]/table
bottno_2 = browser.find_element_by_xpath('/html/body/div[3]/div[1]/ul/li[2]/table')
bottno_2.click()
# WebDriverWait(browser, 2, 0.5).until(wait('//*[@id="submitForm"]/div/div[1]/table/tbody/tr[2]/td[2]/div/input'))
# locator = (By.XPATH, '//*[@id="submitForm"]/div/div[1]/table/tbody/tr[2]/td[2]/div/input')
# WebDriverWait(browser, 6, 0.5).until(EC.element_to_be_clickable(locator))
# WebDriverWait(browser, 2, 0.5).until(button())
locator = (By.XPATH, '//*[@id="submitForm"]/div/div[1]/table/tbody/tr[2]/td[2]/div/input')
WebDriverWait(browser, 2, 0.5).until(EC.element_to_be_clickable(locator))
input_1 = browser.find_element_by_xpath('//*[@id="submitForm"]/div/div[1]/table/tbody/tr[2]/td[2]/div/input')
input_1.send_keys('30000003')
# class button():
#     def __call__(self, browser):
#         if browser.find_element_by_xpath('//*[@id="_searchButton"]'):
#             return True
#         else:
#             return False
# WebDriverWait(browser,2,0.5).until(button())
bottno_3 = browser.find_element_by_xpath('//*[@id="_searchButton"]')
bottno_3.click()
new_window = browser.window_handles[-1]
browser.switch_to_window(new_window)
# while wait('//*[@id="AREA"]/div/img'):
locator = (By.XPATH, '//*[@id="AREA"]/div/img')

yzm = browser.find_element_by_xpath('//*[@id="AREA"]/div/img')
src = yzm.get_attribute('src')
print('1')
result_yem = check_im(src)
print(result_yem)
yzm_input = browser.find_element_by_xpath('//*[@id="answer"]')
yzm_input.send_keys(result_yem)
print('1')
tijiao_botton = browser.find_element_by_xpath('//*[@id="check"]')
tijiao_botton.click()
locator = (By.XPATH, '//td[@class="lwtd0"]')
WebDriverWait(browser, 2, 0.5).until(EC.element_to_be_clickable(locator))
shenqinghao = browser.find_elements_by_xpath('//td[@class="lwtd0"]')
print(shenqinghao)
registration_number = shenqinghao[1].text
ICOG = shenqinghao[2].text
application_date = shenqinghao[3].text
brand_name = shenqinghao[4].text
petitioner = shenqinghao[5].text

print(registration_number)
sql = 'insert into sbw values (%s,%s,%s,%s,%s)'
sor.execute(sql,(registration_number ,ICOG,application_date,petitioner,brand_name))
database.commit()


# # 搜索输入框
# input_1 = browser.find_element_by_xpath('//*[@id="kw"]')
# # 输入搜索条件'失信人'
# input_1.send_keys('商标局')


# # 百度一下按钮
# botton_input = browser.find_element_by_xpath('//*[@id="su"]')
# # 随机睡眠1～3秒
# time.sleep(random.randint(1, 3))
# # 进行点击按钮
# botton_input.click()
# # 显性等待 timeout：60秒 直到locator成立
# locator = (By.XPATH, '//*[@id="1"]/h3/a[1]')
# WebDriverWait(browser, 60).until(EC.presence_of_element_located(locator))
# botton = browser.find_element_by_xpath('//*[@id="1"]/h3/a[1]')
# # 随机睡眠1～3秒
# time.sleep(random.randint(1, 3))
# # 进行点击按钮
# botton.click()
# # 显性等待 timeout：60秒 直到locator成立
# locator = (By.LINK_TEXT, '商标网上查询')
# WebDriverWait(browser, 120).until(EC.presence_of_element_located(locator))
# botton_1 = browser.find_element_by_link_text('商标网上查询')
# # 随机睡眠1～3秒
# time.sleep(random.randint(1, 3))
# # 进行点击按钮
# botton_1.click()
