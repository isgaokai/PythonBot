# -*- encoding : utf-8 -*-
# @Author : Fenglchen
from selenium import webdriver
import time
import json

browser = webdriver.Chrome()
target_url = 'https://i.qq.com/?s_url=http%3A%2F%2Fuser.qzone.qq.com%2F1143552064'
browser.get(url=target_url)
browser.switch_to_frame('login_frame')
input_qq = browser.find_element_by_id('switcher_plogin').click()
time.sleep(1)
input1 = browser.find_element_by_id('u')
time.sleep(1)
input1.send_keys('1143552064')
input2 = browser.find_element_by_id('p')
time.sleep(1)
input2.send_keys('woaini1314X')
click = browser.find_element_by_id('login_button').click()
time.sleep(3)
print(browser.get_cookies())
cookie_list = browser.get_cookies()
cookie_dict = {}
for cookie in cookie_list:
    if 'name' in cookie and 'value' in cookie:
        cookie_dict[cookie['name']] = cookie['value']

with open('cookie_dict.txt', 'w') as f:
    json.dump(cookie_dict, f)
#
# # -*- coding: utf-8 -*-
# """
# Created on Sun Jul 22 11:07:23 2018
# @author: Administrator
# """
# from selenium import webdriver
# import time
# import json
#
# qq_number = '********'
# password = '********'
#
# login_url = 'https://i.qq.com/'
# driver = webdriver.Chrome()
# driver.get(login_url)
# #进入登陆的ifame
# driver.switch_to_frame('login_frame')
# driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="u"]').send_keys(qq_number)
# driver.find_element_by_xpath('//*[@id="p"]').send_keys(password)
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="login_button"]').click()
# time.sleep(1)
# cookie_list = driver.get_cookies()
# cookie_dict = {}
# for cookie in cookie_list:
#     if 'name' in cookie and 'value' in cookie:
#         cookie_dict[cookie['name']] = cookie['value']
#
# with open('cookie_dict.txt', 'w') as f:
#     json.dump(cookie_dict, f)