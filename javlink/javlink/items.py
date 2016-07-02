# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JavlinkItem(scrapy.Item):

    actress = scrapy.Field()
    artwork = scrapy.Field()
    bango = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    posttime = scrapy.Field()
