# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import json
import multiprocessing
import time
import pymysql
import requests
from lxml import etree

# 连接数据库
conn = pymysql.connect(host='localhost', user='root', password='woaini', database='crawler', port=3306, charset='utf8')

# 创建数据库游标 用以执行sql语句
cursor = conn.cursor()

with open('/Users/tempuser/PycharmProjects/python爬虫/ActualCombat/people_with_poor_creditBot/V2/all_urls.txt',
          mode='r') as rau:
    urls = rau.readlines()
all_urls = []
for url in urls:
    all_urls.append(url.replace('\n',''))


def req(url):
    try:
        res = requests.get(url=url, timeout=3)
        res = json.loads(res.text[47:-2])
        # 在上步处理后的数据进行筛选有用的数据 因为'data'键所对应的值结构为{'data':[{'disp_data':[{xx}]}] } 最终获得的pepo为字典
        for peop in res['data'][0]['disp_data']:
            # 获取对应的姓名
            name = peop['iname']
            # 获取对应的案号
            case_num = peop['gistId']
            # 获取对应的法院
            gistUnit = peop['gistUnit']
            # 获取对应的地区
            areaName = peop['areaName']
            # 进行写入数据库 因为数据库内添加了主键，以案号为主键 ，重复数据会报错，所以需要对异常处理

            try:
                # sql语句进行向shixinren表内插入数据
                sql = 'insert into crawler.final_people_with_poor_credit VALUES (%s,%s,%s,%s)'
                # 执行sql语句 数据需要为元组
                cursor.execute(sql, (name, case_num, gistUnit, areaName))
                # 因为对数据库进行了修改 所以需要提交数据库
                conn.commit()
            # 发送重复数据
            except:
                pass
        # 进行跳过
    except:
        print('出错')
        pass

if __name__ == '__main__':
    for j in range(3):
        for i in range(8):
            url = all_urls.pop(0)
            # 多进程创建
            p = multiprocessing.Process(target=req, args=(url,))
            # 多进程开始
            p.start()
        time.sleep(1)