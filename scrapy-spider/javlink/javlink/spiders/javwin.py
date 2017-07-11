# -*- coding: utf-8 -*-
import  scrapy
from scrapy.selector import Selector
from javlink.items import JavlinkItem

class JavSpider(scrapy.Spider):
    name = "javart"
    allowed_domains = ["ja7lib.com",
                       "javbus2.com"]
    start_urls = ["http://www.ja7lib.com/cn/star_mostfav.php"]

    def parse(self, response):
        sel = Selector(response)
        road = sel.xpath('//div[@class="starbox"]/div')
        for yige in road:
            item = JavlinkItem()
            item['actress'] = yige.xpath('.//img/@title').extract()[0]
            #print item['actress']
            halfurl = yige.xpath('./a/@href').extract()[0]
            url = response.urljoin(halfurl)
            #print url
            request = scrapy.Request(url, meta = {'item': item}, callback=self.parse_page)
            yield request

    def parse_page(self,response):
        sel = Selector(response)
        item = response.meta['item']
        pagenum = 1
        try:
            pageroad = sel.xpath('.//div[@class="page_selector"]/a[last()]/@href').extract()[0]
            pagenum = int(pageroad.split('=')[-1])
        except:
            pass
        if pagenum == 1:
            url = response.url
            request = scrapy.Request(url, meta = {'item': item}, callback=self.parse_bike)
            yield request
            #print url
        else:
            for i in range(pagenum):
                urlroad = sel.xpath('.//div[@class="page_selector"]/a[last()]/@href').extract()[0]
                s = response.urljoin(urlroad)
                s = s.split('=')
                s[-1] = str(i+1)
                url = '='.join(s)
                #print url
                request = scrapy.Request(url, meta = {'item': item}, callback=self.parse_bike)
                yield request
        #print pagenum


    def parse_bike(self,response):
        sel = Selector(response)
        item = response.meta['item']
        item['artwork'] = []
        road = sel.xpath('//div[@class="videos"]/div')
        for yige in road:
            #item = response.meta['item']
            dict = {}
            bango = yige.xpath('./a/div[1]/text()').extract()[0]+'\n'
            #print bango
            dict['bango'] = bango
            title = yige.xpath('./a/div[2]/text()').extract()[0]+'\n'#.encode('gbk','ignore')+'\n'
            #print title
            dict['title'] = title
            item['artwork'].append(dict)
        return item

