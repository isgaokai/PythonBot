# -*- encoding : utf-8 -*-
# @Author : Fenglchen
def A(num):
    if num %2 == 0:
        return True
    else:
        return False

listwd = [1,2,3,4,5,6,7,8]
goal = filter(A, listwd)
fm = list(goal)
print(fm)