# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from ActualCombat.scrapy_bqg.Tools.tools import Tools

class ScrapyBqgPipeline:
    def process_item(self, item, spider):
        Tools.download_goal_novel(item['select_novel'],item['name'],item['content'])
        return item
