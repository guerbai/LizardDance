# -*- coding: utf-8 -*-
import  scrapy
from scrapy.selector import Selector
from javlink.items import JavlinkItem
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class JavSpider(scrapy.Spider):
    name = "javart3"
    #driver = webdriver.PhantomJS()
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
            #halfurl = yige.xpath('./a/@href').extract()[0]
            bango = yige.xpath('./a/div[1]/text()').extract()[0]
            url = 'https://www.javbus2.com/'+bango
            #url = 'http://www.javli6.com/cn'+halfurl[1:]
            request = scrapy.Request(url, meta = {'item':item}, callback=self.parse_link)
            yield request
            #yield item

    def parse_link(self,response):
        sel = Selector(response)
        item = response.meta['item']
        #item['bango'] = sel.xpath('//div[@id="video_id"]//td[@class="text"]/text()').extract()[0]
        #item['title'] = sel.xpath('//h3[@class="post-title text"]/a/text()').extract()[0].encode('gbk','ignore')
        #item['posttime'] = sel.xpath('//div[@id="video_date"]//td[@class="text"]/text()').extract()[0]
        item['bango'] = sel.xpath('//div[@class="col-md-3 info"]/p[1]/span[2]/text()').extract()[-1]
        item['posttime'] = sel.xpath('//div[@class="col-md-3 info"]/p[2]/text()').extract()[-1]
        item['title'] = sel.xpath('//h3/text()').extract()[0].encode('gbk','ignore')
        '''if item['posttime'] == '':
            item['posttime'] = 'not_having'
            item['bango'] = response.url.split('/')[-1]
            item['title'] = 'whatever' '''
        item['link'] = []
        driver = webdriver.PhantomJS()
        driver.get(response.url)
        try:
            #WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, \
                                            #"//table[magnet-table]/tr")))
            time.sleep(1)
            elem1 = driver.find_element_by_id('magnet-table')
            elem2 = elem1.find_element_by_xpath('./tr/td/a')
            ed2k = elem2.get_attribute('href')
            item['link'].append(ed2k)
        except:
            pass
        driver.close()
        if item['link'] == []:
            item['link'] = ['may_not_having']
        return item




