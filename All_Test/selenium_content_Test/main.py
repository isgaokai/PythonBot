# -*- encoding : utf-8 -*-
# @Author : Fenglchen
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# 声明浏览器对象
# 完成浏览器对象的初始化并将其赋值为browser对象
browser = webdriver.Chrome()
# 访问页面
browser.get('https://www.liuxue86.com/a/4179370.html')

content = browser.find_element_by_xpath('//*[@id="article-content"]')
print(content.text)