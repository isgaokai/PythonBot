# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import requests
url = 'https://search.jiayuan.com/v2/search_v2.php'
# headers内容
headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User_Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Referer': 'https://search.jiayuan.com/v2/index.php?key=&sex=f&stc=2:18.25&sn=default&sv=1&p=1&pt=106683&ft=off&f=select&mt=d'
}

# data内容
data = {
    'sex': 'f',
    'sn': 'default',
    'sv': '1',
    'p': '1',
    'stc': '2:18.25',
    'f': 'select',
    'listStyle': 'bigPhoto',
    'pri_uid': '294241775',
    'jsversion': 'v5'
}
res = requests.post(url=url, headers= headers,data=data)
