# -*- coding:utf-8 -*-
__author__ = 'fybhp'
import scrapy
from scrapy.selector import Selector
from mzitu.items import MzituItem
import json

class MeizituSpider(scrapy.Spider):
    name = "meizitu"
    allowed_domains = ["meizitu.com"]
    start_urls = ['http://www.meizitu.com/a/list_1_1.html']

    def parse(self,response):
        sel = Selector(response)
        for_xijie = sel.xpath('//ul[@class="wp-list clearfix"]/li')
        for yige in for_xijie:
            xijieurl = yige.xpath('.//a[1]/@href').extract()[0]
            #print xijieurl
            request = scrapy.Request(xijieurl, callback=self.parse_xijie)
            yield request

    def parse_xijie(self,response):
        sel = Selector(response)
        item = MzituItem()
        rawdate1 = sel.xpath('//div[@class="month_Year"]/text()').extract()[0]
        rawdate2 = sel.xpath('//div[@class="day"]/text()').extract()[0]
        date = rawdate1[-4:] + '-' + rawdate1[:2] + '-' + rawdate2
        title = sel.xpath('//div[@class="metaRight"]/h2/a/text()').extract()[0]
        for_pic = sel.xpath('//div[@id="picture"]//img')
        for yige in for_pic:
            item['date'] = date
            item['title'] = title
            item['image_urls'] = [yige.xpath('./@src').extract()[0]]
            yield  item
