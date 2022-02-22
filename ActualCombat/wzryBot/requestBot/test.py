# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    'referer': 'https://pvp.qq.com/raiders/',
}


response = requests.get('https://game.gtimg.cn/images/yxzj/img201606/heroimg/195/195-mobileskin-3.jpg',headers=headers)
print(response)
print(type(response))
if response.status_code == 404:
    print('1')
else:
    with open('css.jpg',mode='wb') as cs:
        cs.write(response.content)