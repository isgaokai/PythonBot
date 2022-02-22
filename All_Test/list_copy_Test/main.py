# -*- encoding : utf-8 -*-
# @Author : Fenglchen
l1 = ['1', '2', ['3', '4']]
for i in l1:
    print(id(i))
l2 = l1
l2[2][0] = '5555'
for i in l2:
    print(id(i))
l1.remove('1')
print(l2)
print(l1)

