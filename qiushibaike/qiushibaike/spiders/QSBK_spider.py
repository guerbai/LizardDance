# -*- encoding: utf-8 -*-
__author__ = 'fybhp'
from qiushibaike.items import QiushibaikeItem
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

class QiushibaikeSpider(CrawlSpider):
    name = "qsbk"
    allowed_domains = ["qiushibaike.com"]
    start_urls = ['http://www.qiushibaike.com/hot/']
    rules = [
        Rule(LinkExtractor(allow=r'http://www.qiushibaike.com/hot/.*?'), callback='parse_item', follow=True),
    ]
    def parse_item(self,response):
        for sel in response.xpath('//div[@class="article block untagged mb15"]'):
            item = QiushibaikeItem()
            item['author'] = sel.xpath('.//h2/text()')[0].extract()
            item['duanzi'] = sel.xpath('div[@class="content"]/text()').extract()
            yield item
