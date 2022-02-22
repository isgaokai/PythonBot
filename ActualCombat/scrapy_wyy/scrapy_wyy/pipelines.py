# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
# 进行数据库连接
database = pymysql.connect(host='192.168.16.21', user='root', password='123456', port=3306, database='crawler', charset='utf8')
# 创建游标
cur = database.cursor()


class ScrapyWyyPipeline:

    def process_item(self, item, spider):
        print(item)
        # 插入语句
        sql = 'insert into scrapy_wyy_hcl values (%s,%s,%s)'
        # 因为设置主键 所以这里使用try
        try:
            # 执行sql语句
            cur.execute(sql, (item['song_id'],item['song_name'], item['total_comment']))
            # 因为对数据库进行修改 所以进行提交数据库
            database.commit()
        except:
            pass
        return item
