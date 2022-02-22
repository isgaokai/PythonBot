# -*- encoding : utf-8 -*-
# @Author : Fenglchen
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# 声明浏览器对象
# 完成浏览器对象的初始化并将其赋值为browser对象
browser = webdriver.Chrome()
# 访问页面
browser.get('https:www.taobao.com')
# # 输出网页源代码
# print(browser.page_source)
# # 进行关闭
# browser.close()

# 查找节点
# 根据name值获取
# find_element_by_name()
# 根据id获取
# find_element_by_id()
# 所有获取单个节点的方法
# find_element_by_id
# find_element_by_name
# find_element_by_xpath
# find_element_by_link_text
# find_element_by_partial_link_text
# find_element_by_tag_name
# find_element_by_class_name
# find_element_by_css_selector

# input_first = browser.find_element_by_id('q')
# input_seconed = browser.find_element_by_name('q')
# input_third = browser.find_element_by_xpath('//*[@id = "q"]')
# print(input_first, input_seconed, input_third)
# browser.close()


# 另外，Selenium 还提供了通用方法 find_element()，它需要传入两个参数：查找方式 By 和值。
# 实际上，它就是 find_element_by_id() 这种方法的通用函数版本，比如 find_element_by_id(id) 就等价于 find_element(By.ID, id)，
# 二者得到的结果完全一致。
# input_first = browser.find_element(By.ID,'q')
# print(input_first)
# browser.close()

# 多个节点
# 使用find_elements()
# lis = browser.find_elements_by_css_selector('.service-bd li')
# print(lis)
# browser.close()
# 所有获取多个节点的方法
# 返回结果为列表
# find_elements_by_id
# find_elements_by_name
# find_elements_by_xpath
# find_elements_by_link_text
# find_elements_by_partial_link_text
# find_elements_by_tag_name
# find_elements_by_class_name
# find_elements_by_css_selector

# 节点交互
# # 输入文字
# send_keys()
# # 清空文字
# clear()
# # 点击按钮
# click()
input = browser.find_element_by_id('q')
input.send_keys('iPhone')
time.sleep(1)
input.clear()
input.send_keys('iPad')
button = browser.find_element_by_class_name('btn-search')
button.click()
input_username = browser.find_element_by_name('fm-login-id')
input_username.send_keys('qqqqqqq')







# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
# browser = webdriver.Chrome()
# try:
#     browser.get('https://www.baidu.com')
#     input = browser.find_element_by_id('kw')
#     input.send_keys('Python')
#     input.send_keys(Keys.ENTER)
#     wait = WebDriverWait(browser, 10)
#     wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
#     print(browser.current_url)
#     print(browser.get_cookies())
#     print(browser.page_source)
# finally:
#     browser.close()