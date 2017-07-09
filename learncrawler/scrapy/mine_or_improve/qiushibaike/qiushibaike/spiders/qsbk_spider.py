# -*- encoding: utf-8 -*-
from qiushibaike.items import QiushibaikeItem
import scrapy
#该脚本不好用的，下的全是第1页的内容。
class QiushibaikeSpider(scrapy.Spider):
    name = "qsbk"
    allowed_domains = ["qiushibaike.com"]
    start_urls = []
    for i in range(35):
        start_urls.append("http://www.qiushibaike.com/hot/page/"+str(i+1)+"/")


    def parse(self,response):
        for sel in response.xpath('//div[@class="article block untagged mb15"]'):
            item = QiushibaikeItem()
            item['author'] = sel.xpath('.//h2/text()')[0].extract()
            item['duanzi'] = sel.xpath('div[@class="content"]/text()').extract()
            #yield item
            yield item
    '''
    def parse_duanzi(self,response):
        for sel in response.xpath('//div[@class="article block untagged mb15"]'):
            item = QiushibaikeItem()
            item['author'] = sel.xpath('.//h2/text()')[0].extract()
            item['duanzi'] = sel.xpath('div[@class="content"]/text()').extract()
            yield item

        next_page = response.xpath('//ul[@class="pagination"]')
        add_link = next_page.xpath('./li/a/@href')[0].extract()
        url = response.urljoin(add_link)
        if url:
            #url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse_duanzi())
    '''