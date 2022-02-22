# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import requests
cookie = {
'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '4964499411'
}
url =  'https://user.qzone.qq.com/proxy/domain/r.qzone.qq.com/cgi-bin/tfriend/friend_ship_manager.cgi?uin=1143552064&do=1&rd=0.6764372107767516&fupdate=1&clean=1&g_tk=1923171194&g_tk=1923171194'
response = requests.get(url=url, cookies=cookie)
print(response.text)