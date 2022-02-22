# -*- encoding : utf-8 -*-
# @Author : Fenglchen
l = [1,2,3]
l2 = []
l2.append(l)
l2.append(l)
l2.append(l)
for i in l2:
    print(id(i))
l.append('4')
print(l2)