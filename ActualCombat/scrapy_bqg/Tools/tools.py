# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import os


class Tools:
    @staticmethod
    def read_all_novels():
        with open('/Users/tempuser/PycharmProjects/python爬虫/ActualCombat/scrapy_bqg/Pool/novels_name_pool.txt',
                  mode='r') as rab:
            all_novels = rab.readlines()
        final_all_novels = []
        for novel in all_novels:
            final_all_novels.append(novel.split())
        final_all_books = dict(final_all_novels)
        return final_all_books

    @staticmethod
    def check_goal_novel(novel_name, novels):
        try:
            if novels[novel_name]:
                return True
            else:
                print('暂未找到该书！')
        except:
            print('暂未找到该书')

    @staticmethod
    def create_goal_file(novel_name):
        project_path = os.path.dirname('')
        file_path = os.path.join(project_path, 'Download', novel_name)
        try:
            os.mkdir(file_path)
        except:
            pass

    # 下载小说进行保存
    @staticmethod
    def download_goal_novel(select_novel,goal_novel_name,content):
        # 获取Download路径创建一个新txt
        project_path = os.path.abspath('')
        goal_novel_path = goal_novel_name + '.txt'
        file_path = os.path.join(project_path,'Download',select_novel,goal_novel_path)
        # 创建文件并写入作者
        with open(file_path, mode='w', encoding='utf-8') as dgn:
            dgn.write('软件作者：fenglchen')
            dgn.write('\n')
            for i in content:
                dgn.write(i.replace(' ', ' '))
