# -*- encoding : utf-8 -*-
# @Author : Fenglchen
# 获取用户需要的图书
from ActualCombat.BiqugeRobot.Tools.tools import Tools
from ActualCombat.BiqugeRobot.Bot.novel_chapters_bot import novel_chapters_bot
import time
from ActualCombat.BiqugeRobot.Novels.novel import Novels
from ActualCombat.BiqugeRobot.Bot.novel_content_bot import novel_content_bot

def user_page():
    # 检验是否有
    Tools.read_schedule_book_name_pool()
    _ = 0
    # 当小说没有/下载完成时 对用户进行询问
    if  Novels.schedule_book_name:
        for _ in range(3):
            print('监测到上次手动退出下载:%s，是否继续上次进度下载？' % Novels.schedule_book_name[0])
            choose = input('1.Yes 2.No\n')
            if choose not in ['1', '2']:
                print('输入错误！')

            elif choose == '1':
                novel_content_bot(Novels.schedule_book_name[0])

            elif choose == '2':
                # 清空
                Novels.schedule_book_name.clear()
                _ = 0
                break
    if _ == 2:
        print('错误次数过多！自动进行清空进度！')


    while True:
        print('****************************')
        # 获取用户需要获取的图书
        for i in range(3):
            goal_novel_name = input('请输入需要下载的小说：')
            # 对用户输入进行检验
            if Tools.check_novel_name(goal_novel_name) is True:
                i = 0
                break
            else:
                print('输入非法！请重新输入！不可包含特殊符号/空格！')
        # 错误次数过多
        if i == 2:
            print('错误次数过多！自动返回主页面！')
            break

        # 对目标小说进行检验
        result = Tools.check_goal_novel(goal_novel_name)
        if result is False:
            print('笔趣阁暂未添加该图书！')
        else:
            # 记录当前下载小说
            Tools.cover_schedule_book_name_pool(goal_novel_name)
            # 开始下载计时
            time_start = time.time()
            print('下载中！请耐心等待！')
            novel_chapters_bot(goal_novel_name, result)
            # 下载完毕计时
            time_stop = time.time()
            print('总共下载用时间:%d 分钟' % ((time_stop-time_start)/60))

        # 当小说没有/下载完成时 对用户进行询问
        for _ in range(3):
            choose = input('是否继续下载？1.Yes 2.No\n')
            if choose not in ['1', '2']:
                print('输入错误！')

            elif choose == '1':
                _ = 0
                break

            elif choose == '2':
                return False

        # 错误次数过多
        if _ == 2:
            print('错误次数过多！自动返回上一页面！')
            break
