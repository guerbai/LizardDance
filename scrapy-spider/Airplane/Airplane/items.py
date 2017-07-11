# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AirplaneItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    corpn = scrapy.Field()    #航空公司
    fltno = scrapy.Field()    #航空公司编号
    plane = scrapy.Field()    #飞机型号
    pk = scrapy.Field()       #飞机大小
    dportn = scrapy.Field()   #出发机场
    aportn = scrapy.Field()   #到达机场
    dtime = scrapy.Field()    #出发时间
    atime = scrapy.Field()    #到达时间
    meat = scrapy.Field()     #是否有餐食
    on = scrapy.Field()       #历史准点率
    minp = scrapy.Field()     #该航班最低票价
    tax = scrapy.Field()      #民航基金
    remainnum = scrapy.Field()#剩余票数
    pass
