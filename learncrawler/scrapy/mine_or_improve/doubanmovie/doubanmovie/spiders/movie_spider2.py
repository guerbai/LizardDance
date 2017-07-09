# -*- coding:utf-8 -*-
__author__ = 'fybhp'
import scrapy
from scrapy.selector import Selector
from doubanmovie.items import DoubanmovieItem
import json,random
from selenium import webdriver
from selenium.webdriver.common.by import By

class GoodMovieSpider(scrapy.Spider):
    driver = webdriver.PhantomJS()
    name = "movie250"
    allowed_domains = ["douban.com"]
    start_urls = []
    i = 0
    while i < 250:
        start_urls.append('https://movie.douban.com/top250?start='+str(i))
        i += 25

    def parse(self,response):
        sel = Selector(response)
        road = sel.xpath('//div[@class="item"]')
        for yige in road:
            score = yige.xpath('.//span[@class="rating_num"]/text()').extract()[0]
            if str(score) >= str(9.0):
                url = yige.xpath('.//div[@class="hd"]/a/@href').extract()[0]
                request = scrapy.Request(url,callback=self.parse_a_movie)
                yield request
            else:
                pass

    def parse_a_movie(self,response):

        sel = Selector(response)
        item = DoubanmovieItem()
        item['movie'] = sel.xpath('//h1/span[1]/text()').extract()[0]
        item['score'] = sel.xpath('//div[@class="rating_self clearfix"]/strong/text()').extract()[0]
        item['url'] = response.url
        item['intro'] = ''
        jieshao = sel.xpath('//div[@id="link-report"]/span[1]/text()').extract()
        if jieshao[0].strip() != '':
            for yige in jieshao:
                item['intro'] = item['intro'] + yige.strip()+ '\n'
            i = 0
            length = len(item['intro'])
            while i < length:
                item['intro'] = item['intro'][:i]+'\n'+item['intro'][i:]
                i += 75
        else:
            self.driver.get(response.url)
            self.driver.find_element_by_xpath('//a[@class="j a_show_full"]').click()
            jieshao2 = self.driver.find_element_by_xpath('//span[@class="all hidden"]').text
            item['intro'] = jieshao2
            i = 0
            length = len(item['intro'])
            while i < length:
                item['intro'] = item['intro'][:i]+'\n'+item['intro'][i:]
                i += 75

        return item