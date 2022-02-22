# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import pymysql


# 连接数据库
cs_user_database = pymysql.connect(user='root', password='woaini', host='localhost', database='csuser', port=3306, charset='utf8')
# 创建一个游标
