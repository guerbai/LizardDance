# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TtestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class HuxiuItem(scrapy.Item):
    title = scrapy.Field()    # 标题
    link = scrapy.Field()     # 链接
    desc = scrapy.Field()     # 简述
    posttime = scrapy.Field() # 发布时间

class QiuItem(scrapy.Item):
    duanzi = scrapy.Field()

class DoubanimageItem(scrapy.Item):
    # define the fields for your item here like:
    # name = Field()
    ImageAddress = scrapy.Field()
    pass

class ImageItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
    image_paths = scrapy.Field()

class MeizituItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    tags = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()

class TencentItem(scrapy.Item):
    name = scrapy.Field()                # 职位名称
    catalog = scrapy.Field()             # 职位类别
    workLocation = scrapy.Field()        # 工作地点
    recruitNumber = scrapy.Field()       # 招聘人数
    detailLink = scrapy.Field()          # 职位详情页链接
    publishTime = scrapy.Field()

class bbs(scrapy.Item):
    link = scrapy.Field()
    title = scrapy.Field()

class DuitangItem(scrapy.Item):
    # define the fields for your item here like:
    image_urls = scrapy.Field()
    images = scrapy.Field()

class CnblogsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    listUrl = scrapy.Field()
    pass

class FirstscrapyItem(scrapy.Item):
    title = scrapy.Field(serializer=str)
    link = scrapy.Field(serializer=str)