# -*- encoding : utf-8 -*-
# @Author : Fenglchen
from ffmpy3 import FFmpeg
c = FFmpeg(
    executable='/Users/tempuser/PycharmProjects/python爬虫/All_Test/ffmepg_Test/ffmpeg',
    inputs={'1.mp4':None,'1.mp3':None},
    outputs={'bcddd.mp4':None}
)
c.run()
