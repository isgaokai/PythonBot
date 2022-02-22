import scrapy
from lxml import etree
from ActualCombat.scrapy_wyy.scrapy_wyy.items import ScrapyWyyItem
import copy
from ActualCombat.scrapy_wyy.Test.test_open import get_music

class WyyBotSpider(scrapy.Spider):
    name = 'wyy_bot'

    # 这里填写歌单的url
    def start_requests(self):
        all_music_name, all_musi_id = get_music()
        for index,value in enumerate(all_musi_id):
            url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_'+all_musi_id[index]
            r = scrapy.Request(url=url)
            r.meta['song_name'] = all_music_name[index]
            r.meta['song_id'] = all_musi_id[index]
            yield r

    def parse(self, response):
        # 创建一个item对象
        item = ScrapyWyyItem()
        # 歌曲id
        item['song_id'] = response.meta['song_id']
        # 歌曲名
        item['song_name'] = response.meta['song_name']
        # 数据处理
        response = response.text.split(',')
        test_toatl_comment = copy.deepcopy(response)
        for i in test_toatl_comment:
            if 'total' not in i:
                response.remove(i)
        # 歌曲总评论数
        item['total_comment'] = response[0].split(':')[1]
        yield item

    # def parse(self, response):
    #     # 创建etree
    #     song_etree = etree.HTML(response.text)
    #     # 获取所有歌
    #     all_song_name = song_etree.xpath('//div[@id="song-list-pre-cache"]/ul/li/a/text()')
    #     # 获取所以歌的id
    #     all_song_id = song_etree.xpath('//textarea[@id="song-list-pre-data"]/text()')
    #     # 创建一个item对象
    #     item = ScrapyWyyItem()
    #     # 进行数据初选
    #     all_song_id = all_song_id[0].split(',')
    #     # 进行深拷贝
    #     test_all_song = copy.deepcopy(all_song_id)
    #     # 进行数据筛选
    #     for i in test_all_song:
    #         if 'R_SO' not in i:
    #             all_song_id.remove(i)
    #     # 对该歌单每首歌对信息进行筛选
    #     for index, value in enumerate(all_song_id):
    #         # 数据处理
    #         song_id = value.split('":"')[1][:-1]
    #         # 歌曲id
    #         item['song_id'] = song_id
    #         # 歌曲名字
    #         item['song_name'] = all_song_name[index]
    #         # 对应url
    #         url = 'http://music.163.com/api/v1/resource/comments/'+song_id
    #         yield scrapy.Request(url=url, meta=item, callback=self.parse_comment)

    # def parse_comment(self, response):
    #     # 创建一个item对象
    #     item = ScrapyWyyItem()
    #     # 歌曲id
    #     item['song_id'] = response.meta['song_id']
    #     # 歌曲名
    #     item['song_name'] = response.meta['song_name']
    #     # 数据处理
    #     response = response.text.split(',')
    #     test_toatl_comment = copy.deepcopy(response)
    #     for i in test_toatl_comment:
    #         if 'total' not in i:
    #             response.remove(i)
    #     # 歌曲总评论数
    #     item['total_comment'] = response[0].split(':')[1]
    #     yield item
    #
