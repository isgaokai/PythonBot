# -*- encoding : utf-8 -*-
# @Author : Fenglchen
from selenium import webdriver
import time

cookies = {
    'UM_distinctid': '17bf277bf8e763-0ffbad3484099a-113f6757-129790-17bf277bf8f5fa',
    'goN9uW4i0iKzS': '54p9Oh5.nujnJ0R0cPqirtGqmxM8Pw5PubKqi_THKJH_OkYtSJAecv2MWdHnLwvB70xqjh1dClvFUFeiso93Biq',
    'tmas_cookie': '2272.7689.15400.0000',
    '018f9ebcc3834ce269': '2efc18aea4fa1734db221a2d03a37f68',
    'JSESSIONID': '0000IgEeETt6p3tu_27dqd_tvLp:1bm104mv1',
    'goN9uW4i0iKzT': '53VvthbmxngaqqqmZck6htAxC4e.tVnVKVpwJZbMKn.7FM4Dset8SHmPsCv97mNQ_oAp727gQjsZq29KKd7jfrkxRTUG2Tx930BOc5Uoh14Tjk_WyH104zgcB27Ljg6NYdS3KeNEtgfE4p58mzVkohcgxg9SpZxnthyqGYb.JxX0kLL7EAWyNjlI9bolZF3608ILseoXV2i.HuY60.9mZH_vPTnZu8ZfK87fbKoQ8FF6IJrkOcVvlOqu.KE4DdhIuBOgQohXyrXZrBvw5atUVzbFEMXfrA9wP0tXDfRqRmEXa',
}
url = 'http://wcjs.sbj.cnipa.gov.cn/txnT01.do'
browser = webdriver.Chrome()
browser.get(url)
browser.add_cookie(cookie_dict=cookies)
print('1')
int = browser.find_elements_by_class_name("icon_box")[3]
time.sleep(1)
int.click()
time.sleep(1)
