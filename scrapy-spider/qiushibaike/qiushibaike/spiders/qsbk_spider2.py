# -*- encoding: utf-8 -*-
__author__ = 'fybhp'
from qiushibaike.items import QiushibaikeItem
import scrapy

class QiushibaikeSpider(scrapy.Spider):
    name = "qsbk2"
    allowed_domains = ["qiushibaike.com"]
    start_urls = ['http://www.qiushibaike.com/hot/page/1/']

    def parse(self,response):
        for sel in response.xpath('//div[@class="article block untagged mb15"]'):
            item = QiushibaikeItem()
            item['author'] = sel.xpath('.//h2/text()')[0].extract()
            item['duanzi'] = sel.xpath('div[@class="content"]/text()').extract()
            yield item
        sel2 = response.xpath('//ul[@class="pagination"]/li/a/@href').extract()
        sel3 = sel2[-1]
        print sel3
        url = response.url.replace(response.url[26:],sel3)
        print url
        yield scrapy.Request(url, callback=self.parse)


