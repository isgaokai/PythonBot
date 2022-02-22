# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyWyyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    song_id = scrapy.Field()
    song_name = scrapy.Field()
    total_comment = scrapy.Field()
    pass
