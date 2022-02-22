# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

# 连接数据库
conn = pymysql.connect(host='localhost', user='root', password='woaini', database='crawler', port=3306, charset='utf8')
# 创建数据库游标 用以执行sql语句
cursor = conn.cursor()


class ScrapySxrPipeline:
    def process_item(self, item, spider):
        try:
            # sql语句进行向shixinren表内插入数据
            sql = 'insert into crawler.scrapy_sxr VALUES (%s,%s,%s,%s)'
            # 执行sql语句 数据需要为元组
            cursor.execute(sql, (item['name'], item['reference_number'], item['executive_count'], item['province']))
            # 因为对数据库进行了修改 所以需要提交数据库
            conn.commit()
        except:
            return item
        return item
