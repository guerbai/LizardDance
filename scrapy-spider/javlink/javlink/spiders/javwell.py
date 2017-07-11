# -*- coding: utf-8 -*-
__author__ = 'fybhp'
import  scrapy
from scrapy.selector import Selector
from javlink.items import JavlinkItem

class JavSpider(scrapy.Spider):
    name = "javart4"
    allowed_domains = ["ja7lib.com",
                       "torrentkitty.me"]
    start_urls = ["http://www.ja7lib.com/cn/star_mostfav.php"]

    def parse(self, response):
        sel = Selector(response)
        road = sel.xpath('//div[@class="starbox"]/div')
        for yige in road:
            item = JavlinkItem()
            item['actress'] = yige.xpath('.//img/@title').extract()[0].encode('gbk','ignore')
            halfurl = yige.xpath('./a/@href').extract()[0]
            url = response.urljoin(halfurl)
            request = scrapy.Request(url, meta={'item':item}, callback=self.parse_page)
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
            request = scrapy.Request(url, meta={'item':item}, callback=self.parse_bike)
            yield request
        else:
            for i in range(pagenum):
                item = response.meta['item']
                urlroad = sel.xpath('.//div[@class="page_selector"]/a[last()]/@href').extract()[0]
                s = response.urljoin(urlroad)
                s = s.split('=')
                s[-1] = str(i+1)
                url = '='.join(s)
                request = scrapy.Request(url, meta = {'item':item},callback=self.parse_bike)
                yield request


    def parse_bike(self,response):
        sel = Selector(response)
        road = sel.xpath('//div[@class="videos"]/div')
        for yige in road:
            item = response.meta['item']
            halfurl = yige.xpath('./a/@href').extract()[0]
            url = 'http://www.ja7lib.com/cn'+halfurl[1:]
            request = scrapy.Request(url, meta={'item':item},callback=self.parse_link)
            yield request

    def parse_link(self,response):
        sel = Selector(response)
        item = response.meta['item']
        item2 = JavlinkItem()
        bango = sel.xpath('//div[@id="video_id"]//td[@class="text"]/text()').extract()[0]
        title = sel.xpath('//h3[@class="post-title text"]/a/text()').extract()[0].encode('gbk','ignore')
        posttime = sel.xpath('//div[@id="video_date"]//td[@class="text"]/text()').extract()[0]
        item2['bango'] = bango
        item2['posttime'] = posttime
        item2['title'] = title
        item2['actress'] = item['actress']
        url = 'http://www.torrentkitty.me/search/'+bango+'/'
        request = scrapy.Request(url,meta={'item':item2},callback=self.parse_last)
        yield request

    def parse_last(self,response):
        sel = Selector(response)
        item = response.meta['item']
        try:
            item['link'] = sel.xpath('//a[@rel="magnet"]/@href').extract()[0]
        except:
            item['link'] = 'none'
        yield item

