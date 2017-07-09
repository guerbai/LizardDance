# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

class FybSpider(scrapy.Spider):
    name = "fyb"
    allowed_domains = ["torrentkitty.me"]
    start_urls = [
        'http://www.torrentkitty.me/search/tek-073/',
    ]

    def parse(self, response):
        sel = Selector(response)
        link = sel.xpath('//a[@rel="magnet"]/@href').extract()[0]
        print link

