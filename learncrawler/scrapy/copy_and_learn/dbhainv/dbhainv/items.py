# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DbhainvItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    name = scrapy.Field()

class DoubanimageItem(scrapy.Item):
    # define the fields for your item here like:
    # name = Field()
    ImageAddress = scrapy.Field()
    pass
