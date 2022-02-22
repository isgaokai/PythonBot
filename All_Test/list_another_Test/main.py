# -*- encoding : utf-8 -*-
# @Author : Fenglchen
l = [[j for j in range(1,4)] for i in range(3)]
print(l)
for i in l:
    print(id(i))