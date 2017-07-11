# -*- coding: utf-8 -*-
import  scrapy
from scrapy.selector import Selector
from javlink.items import JavlinkItem

class JavSpider(scrapy.Spider):
    name = "javart2"
    allowed_domains = ["ja7lib.com",
                       "javbus2.com"]
    start_urls = ["http://www.ja7lib.com/cn/star_mostfav.php"]

    def parse(self, response):
        sel = Selector(response)
        road = sel.xpath('//div[@class="starbox"]/div')
        for yige in road:
            item = JavlinkItem()
            item['actress'] = yige.xpath('.//img/@title').extract()[0].encode('gbk','ignore')
            halfurl = yige.xpath('./a/@href').extract()[0]
            url = response.urljoin(halfurl)
            request = scrapy.Request(url, meta = {'item': item}, callback=self.parse_page)
            yield request

    def parse_page(self,response):
        sel = Selector(response)
        pagenum = 1
        try:
            pageroad = sel.xpath('.//div[@class="page_selector"]/a[last()]/@href').extract()[0]
            pagenum = int(pageroad.split('=')[-1])
        except:
            pass
        if pagenum == 1:
            item = response.meta['item']
            url = response.url+'&page=1'
            print url
            request = scrapy.Request(url, meta = {'item': item}, callback=self.parse_bike)
            yield request
        else:
            for i in range(pagenum):
                item = response.meta['item']
                urlroad = sel.xpath('.//div[@class="page_selector"]/a[last()]/@href').extract()[0]
                s = response.urljoin(urlroad)
                s = s.split('=')
                s[-1] = str(i+1)
                url = '='.join(s)
                request = scrapy.Request(url, meta = {'item': item}, callback=self.parse_bike)
                yield request


    def parse_bike(self,response):
        sel = Selector(response)
        road = sel.xpath('//div[@class="videos"]/div')
        for yige in road:
            item = response.meta['item']
            item['bango'] = yige.xpath('./a/div[1]/text()').extract()[0]
            item['title'] = yige.xpath('./a/div[2]/text()').extract()[0].encode('gbk','ignore')
            yield item
