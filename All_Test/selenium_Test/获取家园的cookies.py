# -*- encoding : utf-8 -*-
# @Author : Fenglchen
from selenium import webdriver
import time
import json

browser = webdriver.Chrome()
url = 'https://login.jiayuan.com/?pre_url=%2Fusercp&channel=1&position=21&refrer=https://www.jiayuan.com&host=0'
browser.get(url=url)
in_1 = browser.find_element_by_id('login_email')
time.sleep(1)
in_1.send_keys('19834523498')
in_2 =  browser.find_element_by_id('login_password')
time.sleep(2)
in_2.send_keys('woainigk54.')
bo = browser.find_element_by_id('login_btn')
time.sleep(2)
bo.click()
cookies_list = browser.get_cookies()
print(cookies_list)
cookies_dict = {}
for cookie in cookies_list:
    cookies_dict[cookie['name']] = cookie['value']
print(cookies_dict)
browser.close()