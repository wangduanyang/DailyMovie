# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YangscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class DailyMoiveItem(scrapy.Item):
    # define the fields for your item here like:
    # 电影名称
    movie_name = scrapy.Field()
    movie_desc = scrapy.Field()
