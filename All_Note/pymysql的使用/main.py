# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import pymysql
#
# pymysql的使用
# 1。建立一个传输数据的连接通道
# db = pymysql.connect(host user password database port charset)
# host 主机ip user用户名 password用户密码 database 数据库 port 端口号 charser 字符集
db = pymysql.connect(host='localhost', user='root', password='woaini', database='crawler', port=3306, charset='utf8')
# 2。cursor（）方法
# 游标实际上是一种能从包括多条数据记录的结果集中每次提取一条的机制
# 游标充当指针的作用
# 作用： 用于查询数据库所返回的记录进行遍历。以便进行相应的操作
cursor = db.cursor()
# 3。数据库操作需要使用Cursor类的实例提供的execute()方法执行sql语句成功则返回结果
# 插入操作
# sql = "insert into database.table values('xx','xxx')"
# cursor.execute(sql)
# 查询操作
sql = 'select * from crawler.ivsky'
# 返回查询到的个数 int
res1 = cursor.execute(sql)
# print(res1)
# 查询时获取结果集中的所有行，一行构成一个元祖，然后再将这些元组返回
res2 = cursor.fetchall()
print(res2)
# 查询结果集的方法
# fetchone()  获取结果集的下一行
# fetchmant(size = None) size返回指定的行数
# fetchall()  返回剩下所有行
# cursor.rownumber    返回当前行号
# cursor.rowcount 返回的总行数
# connection 提供了三个方法
# begin commit rollback
# 开始事务 提交事务 回滚事务
# 注！！！
#     如果sql语句对数据库中的数据进行了修改，则需要提交事务
#
# 释放资源
# close()
# close将当前连接归还，并不会终止整个连接， 调用close后再次查询，即可查询到最新的数据。
sql = "insert into crawler.ivsky VALUES ('qqqq','wwww')"
res_1 = cursor.execute(sql)
db.commit()
# 查询操作
sql = 'select * from crawler.ivsky'
# 返回查询到的个数 int
res1 = cursor.execute(sql)
# print(res1)
# 查询时获取结果集中的所有行，一行构成一个元祖，然后再将这些元组返回
res2 = cursor.fetchall()
print(res2)
# 在执行查询操作时候要尽量避免使用%s或者format（）的字符串替换操作，这样做是为了避免sql注入的发生
# 参数化查询，不仅可以有效的防止注入攻击，还可以提高查询的效率
# cursor.execute(query,args=元组，列表，字符串)
# sql = "select * from table where name like %s and age < %s"
# cursor.execute(sql,('tom%',25))
#
# 或者
#
# sql = "select * from table where name like %(name)s and age < %(age)s"
# cursor.execute(sql,{'name':'tom%','age':25})
