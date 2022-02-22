# -*- encoding : utf-8 -*-
# @Author : Fenglchen
with open('/Users/tempuser/PycharmProjects/python爬虫/ActualCombat/jiayuanBot/Pool/all_user_id_pool.txt',
          mode='r') as rauip:
    all_user_id = rauip.readlines()

goal =[ ]
for i in all_user_id:
    goal.append(i.replace('\n', ''))
print(goal)
goal = set(all_user_id)
print(goal)
print(len(goal))
with open('/Users/tempuser/PycharmProjects/python爬虫/ActualCombat/jiayuanBot/Pool/final_all_user_id_pool.txt',
          mode='w') as wauip:
    for i in goal:
        wauip.write(i)

