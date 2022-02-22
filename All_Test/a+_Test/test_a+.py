# -*- encoding : utf-8 -*-
# @Author : Fenglchen
with open('/111111/ce_a+.txt', mode='a+') as acs:
    acs.write('wdwdfqfqwfqw')


with open('/111111/ce_a+.txt', mode='a+') as acwws:
    acwws.seek(0)
    bbb = acwws.readlines()
    print(bbb)