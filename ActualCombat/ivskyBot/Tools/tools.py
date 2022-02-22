# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import os
from ActualCombat.ivskyBot.Image.image import Image
from urllib.request import urlopen

# 工具类
class Tools:
    # 覆盖image_category_pool
    @staticmethod
    def cover_image_category_pool(category_names, category_urls):
        # 获取Pool路径
        project_path = os.path.dirname(os.path.abspath(os.path.abspath('.')))
        file_path = os.path.join(project_path, 'Pool', 'image_category_pool.txt')
        # 写入文件
        with open(file_path, mode='w', encoding='utf-8') as cicp:
            for i, j in zip(category_names, category_urls):
                cicp.write(i)
                cicp.write(' ')
                cicp.write(r'https://www.ivsky.com'+j)
                cicp.write('\n')

    # 覆盖image_gallery_pool
    @staticmethod
    def cover_image_gallery_pool(image_gallery_names, image_gallery_urls):
        # 获取Pool路径
        project_path = os.path.dirname(os.path.abspath(os.path.abspath('.')))
        file_path = os.path.join(project_path, 'Pool', 'image_gallery_pool.txt')
        # 写入文件
        with open(file_path, mode='w', encoding='utf-8') as cigp:
            for i, j in zip(image_gallery_names, image_gallery_urls):
                cigp.write(i)
                cigp.write(' ')
                cigp.write(r'https://www.ivsky.com'+j)
                cigp.write('\n')

    # 读取image_gallery_pool
    @staticmethod
    def read_image_gallery_pool():
        # 获取Pool路径
        project_path = os.path.dirname(os.path.abspath(os.path.abspath('.')))
        file_path = os.path.join(project_path, 'Pool', 'image_gallery_pool.txt')
        with open(file_path, mode='r', encoding='utf-8') as rigp:
            all_image_gallery = rigp.readlines()
        for i in all_image_gallery:
            Image.image_gallery_and_url.append(i.replace('\n', '').split())


    # 读取image_category_pool
    @staticmethod
    def read_image_category_pool():
        # 获取Pool路径
        project_path = os.path.dirname(os.path.abspath(os.path.abspath('.')))
        file_path = os.path.join(project_path, 'Pool', 'image_category_pool.txt')
        with open(file_path, mode='r', encoding='utf-8') as ricp:
            all_image_category = ricp.readlines()
        for i in all_image_category:
            Image.image_category_and_url.append(i.replace('\n', '').split())

    # 进行创建类别文件夹
    @staticmethod
    def create_category_folder(category_names):
        for name in category_names:
            # 获取Pool路径
            project_path = os.path.abspath('..')
            file_path = os.path.join(project_path, 'Download', name)
            print(file_path)
            os.mkdir(file_path)

    # 进行创建图片集文件夹
    @staticmethod
    def create_imagr_gallert_folder(image_category, imagr_gallert_name):
        # 获取Pool路径
        project_path = os.path.abspath('..')
        file_path = os.path.join(project_path, 'Download', image_category, imagr_gallert_name)
        os.mkdir(file_path)

    # 进行下载图片文件
    @staticmethod
    def download_image(image_category, imagr_gallert_name, image_content_name, image_content_url):
        # 获取上级目录路径
        project_path = os.path.abspath('..')
        # 获取相对应的图片集的路径
        file_path = os.path.join(project_path, 'Download', image_category, imagr_gallert_name)
        # 如果该路径没有被创建则 进行创建
        try:
            os.mkdir(file_path)
        except:
            pass

        while True:
            try:
                content_res = urlopen(image_content_url).read()
                break
            except:
                continue
        # 进行下载图片
        with open(file_path + '/' + image_content_name + '.jpg', 'wb') as wi:
            wi.write(content_res)
            return True
        return False
