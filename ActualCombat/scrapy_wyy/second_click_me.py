# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import pymysql
from pyecharts.charts import Bar
from pyecharts import options as opts

database = pymysql.connect(host='192.168.16.9', user='root', password='woaini',
                           port=3306, database='crawler', charset='utf8')
cur = database.cursor()

sql = 'select * from scrapy_wyy'
all_songs = cur.execute(sql)
final_all_songs= cur.fetchall()
print(final_all_songs)
all_song_names = []
all_song_total_comment = []
count =1
for i in final_all_songs:
    all_song_names.append(i[1])
    all_song_total_comment.append(i[2])
    count = count + 1
    if count >25:
        break
print(all_song_names)
print(all_song_total_comment)
bar = (Bar()
    .add_xaxis(all_song_names)
    .add_yaxis('歌曲评论',all_song_total_comment)
    .set_global_opts(
    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-50)),
    title_opts=opts.TitleOpts(title="Bar-旋转X轴标签", subtitle="解决标签名字过长的问题"),
)
    .set_global_opts(title_opts=opts.TitleOpts(title='音乐信息', subtitle='歌单标题及评论数'), toolbox_opts=opts.ToolboxOpts())
)

bar.render()


