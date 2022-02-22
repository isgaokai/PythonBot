# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import jieba
from collections import Counter
import copy

import wordcloud
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# 特殊符号表
special_str = r'!@#$~%^&*()（）_+{}[]:";<>.：《》~！@#￥%……&*（）——+?/╱| \'，。？,、｀━“─┓┃=【￣·\u2006➕＊\u3000'

# 所有评论
all_comments = []
# 最终词条
final_worlds = []
# 读取文件
with open('//Users/tempuser/PycharmProjects/python爬虫/ActualCombat/wordcloudBot/Pool/initial_comments_pool.txt',
          mode='r') as rtcp:
    temp_all_comments = rtcp.readlines()
# 数据处理
for comment in temp_all_comments:
    comment = comment.replace('\n', '')
    test_comment = copy.deepcopy(comment)
    for i in test_comment:
        if i in special_str:
            comment = comment.replace(i, '')
    all_comments.append(comment)
# 去除空
while True:
    try:
        all_comments.remove('')
    except:
        break
# 进行词频计算
for comment in all_comments:
    words = jieba.lcut(comment)
    for word in words:
        final_worlds.append(word)
counter = Counter(final_worlds)
counter = dict(counter)
final_words_list = [(key, value)for key, value in counter.items()]

picture = np.array(Image.open('/Users/tempuser/Desktop/Maroon5.jpeg'))
word_cloud = wordcloud.WordCloud(
    font_path='/Users/tempuser/Downloads/shouzhati_downcc/手札体.ttf',
    mask=picture,
    max_font_size=100,
    background_color='white',
    max_words=20000
)
word_cloud.generate_from_frequencies(dict(final_words_list))
image = word_cloud.to_image()
image.show()
word_cloud.to_file('/Users/tempuser/PycharmProjects/python爬虫/ActualCombat/wordcloudBot/pictures/1.jpg')

