# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import os
from ActualCombat.BiqugeRobot.Novels.novel import Novels


# 工具类
class Tools:

    # 检验用户输入书名
    @staticmethod
    def check_novel_name(novel_name):
        # 用户输入书名中包含空格
        if novel_name.count(' ') != 0:
            return False

        # 用户输入包含特殊符号
        if novel_name.isalnum() is False:
            return False

        # 用户输入为空
        if len(novel_name) == 0:
            return False

        # 通过检验
        return True

    # 检验当前图书笔趣阁是否添加
    @staticmethod
    def check_goal_novel(novel_name):
        for novel in Novels.novels_name_url:
            if novel[0] == novel_name:
                return novel[1]

        return False

    # 读取novels_name_pool
    @staticmethod
    def read_novels_name_pool():
        # 获取Pool路径
        project_path = os.path.dirname('')
        file_path = os.path.join(project_path, 'Pool', 'novels_name_pool.txt')
        # 读取文件中数据
        with open(file_path, mode='r', encoding='utf-8') as rnnp:
            all_novels = rnnp.readlines()
        for _ in all_novels:
            Novels.novels_name_url.append(_.replace('\n', '').split())

    # 读取novels_chapters_pool
    @staticmethod
    def read_novels_chapters_pool():
        # 清空初始化
        Novels.novel_chapter_url.clear()
        # 获取Pool路径
        project_path = os.path.abspath('')
        file_path = os.path.join(project_path, 'Pool', 'novels_chapters_pool.txt')
        # 读取文件中数据
        with open(file_path, mode='r', encoding='utf-8') as rncp:
            all_chapters = rncp.readlines()
        for _ in all_chapters:
            Novels.novel_chapter_url.append(_.replace('\n', '').split())

    # 读取schedule_book_name_pool
    @staticmethod
    def read_schedule_book_name_pool():
        # 获取Pool路径
        project_path = os.path.abspath('')
        file_path = os.path.join(project_path, 'Pool', 'schedule_book_name_pool.txt')
        # 读取文件中数据
        with open(file_path, mode='r', encoding='utf-8') as rsbnp:
            schedule_book_name = rsbnp.read()
        # 非空检验
        if  schedule_book_name:
            Novels.schedule_book_name.append(schedule_book_name)


    # 覆盖novels_name_pool
    @staticmethod
    def cover_novels_name_pool(novels_name, novels_url):
        # 获取Pool路径
        project_path = os.path.dirname(os.path.abspath(os.path.abspath('')))
        file_path = os.path.join(project_path, 'Pool', 'novels_name_pool.txt')
        # 写入文件
        with open(file_path, mode='w', encoding='utf-8') as cnnp:
            for i, j in zip(novels_name,novels_url):
                cnnp.write(i)
                cnnp.write(' ')
                cnnp.write(j)
                cnnp.write('\n')

    # 覆盖novels_chapters_pool
    @staticmethod
    def cover_novels_chapters_pool(novel_chapters, novel_chapters_url):
        # 获取Pool路径
        project_path = os.path.abspath('')
        file_path = os.path.join(project_path, 'Pool', 'novels_chapters_pool.txt')
        # 写入文件
        with open(file_path, mode='w', encoding='utf-8') as cncp:
            for i, j in zip(novel_chapters, novel_chapters_url):
                cncp.write(i)
                cncp.write(' ')
                cncp.write(j)
                cncp.write(' ')
                cncp.write('0')
                cncp.write('\n')

    # 覆盖schedule_book_name_pool
    @staticmethod
    def cover_schedule_book_name_pool(novel_name):
        # 获取Pool路径
        project_path = os.path.abspath('')
        file_path = os.path.join(project_path, 'Pool', 'schedule_book_name_pool.txt')
        # 写入文件
        with open(file_path, mode='w', encoding='utf-8') as csbnp:
            csbnp.write(novel_name)

    # 当前爬取进度更新
    @staticmethod
    def update_novels_chapters_pool():
        # 获取Pool路径
        project_path = os.path.abspath('')
        file_path = os.path.join(project_path, 'Pool', 'novels_chapters_pool.txt')
        # 写入文件
        with open(file_path, mode='w', encoding='utf-8') as uncp:
            for chapter in Novels.novel_chapter_url:
                for i in chapter:
                    uncp.write(i)
                    uncp.write(' ')
                uncp.write('\n')

    # 下载小说进行保存
    @staticmethod
    def download_goal_novel(goal_novel_name,content):
        # 获取Download路径创建一个新txt
        project_path = os.path.dirname('.')
        goal_novel_path = goal_novel_name + '.txt'
        file_path = os.path.join(project_path, 'Download', goal_novel_path)
        # 创建文件并写入作者
        with open(file_path, mode='w', encoding='utf-8') as dgn:

            dgn.write('\n')
            if not content:
                return
            else:
                for i in content:
                    dgn.write(i)
