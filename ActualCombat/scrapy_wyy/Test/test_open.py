# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import os


def get_music():
    path = os.path.abspath('..')
    path = os.path.join(path, 'scrapy_wyy','音乐链接.txt')
    with open(path, mode='r')as rm:
        all_music = rm.read()
    all_music = all_music.split('***\n')
    all_music_name = []
    all_musi_id = []
    for music in all_music:
        try:
            music_name = music.split('\n')[0]
            music_id = music.split('\n')[1].split('=')[1]
            all_musi_id.append(music_id)
            all_music_name.append(music_name)
        except:
            pass
    return all_music_name,all_musi_id