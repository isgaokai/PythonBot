# -*- encoding : utf-8 -*-
# @Author : Fenglchen
from ActualCombat.BiqugeRobot.Page.user_page import user_page
from ActualCombat.BiqugeRobot.Tools.tools import Tools

# 进行读取novels_name_pool
Tools.read_novels_name_pool()

while True:
    print('****************************')
    print('欢迎进入笔趣阁图书txt下载系统！')
    print('****************************')
    print('1.进行指定图书下载 2.退出系统')
    # 获取用户操作
    choose = input('请进行您的操作：')
    # 非法操作
    if choose not in ['1', '2']:
        print('输入错误！')

    # 用户进入指定图书下载
    elif choose == '1':
        user_page()

    # 退出系统
    elif choose == '2':
        break
