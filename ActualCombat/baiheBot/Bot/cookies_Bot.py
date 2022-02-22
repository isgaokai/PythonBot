# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import requests

data = {
    'txtLoginEMail': '19834523498',
    'txtLoginPwd': 'woaini1314',
    'spmp': '4.20.53.225.685',
    'challenge': '0e0a125508b8d7bd4ec9c574f4090e50',
    'validate': '6b30e190e4cc81d05cb450343778bdeb',
    'seccode': '6b30e190e4cc81d05cb450343778bdeb|jordan'
}
url = 'https://www.baihe.com'
res = requests.post(url=url, data=data)
print(res.cookies)
