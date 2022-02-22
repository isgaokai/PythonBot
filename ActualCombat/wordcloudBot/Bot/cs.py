# -*- encoding : utf-8 -*-
# @Author : Fenglchen
with open('/Users/tempuser/PycharmProjects/python爬虫/ActualCombat/wordcloudBot/Pool/all_usernames_pool.txt',
          mode='r',encoding='gbk') as ra:
    all_user_name = ra.readlines()

all_user_names = []
for name in all_user_name:
    all_user_names.append(name.replace('\n',''))
print(len(all_user_names))
all_user_names = set(all_user_names)
print(len(all_user_names))