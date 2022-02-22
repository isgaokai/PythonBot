# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import requests
import copy

url ='http://music.163.com/api/v1/resource/comments/R_SO_4_1875941511'
response =requests.get(url)
response = response.text.split(',')
test = copy.deepcopy(response)
for i in test:
    if 'total' not in i:
        response.remove(i)
print(response)
response = response[0].split(':')[1]
print(response)
