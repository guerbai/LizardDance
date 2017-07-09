# -*- coding:utf-8 -*-
import scrapy
from scrapy.selector import Selector
from doubanmovie.items import DoubanmovieItem
import json,random
from selenium import webdriver
from selenium.webdriver.common.by import By

class GoodMovieSpider(scrapy.Spider):
    driver = webdriver.PhantomJS()
    name = "goodmovie"
    allowed_domains = ["douban.com"]
    start_urls = ['https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=time&page_limit=10000&page_start=0',]

    def parse(self,response):
        sel = json.loads(response.body,encoding='utf-8')
        subjects = sel['subjects']
        for yige in subjects:
            score = yige['rate']
            if str(score) >= str(8.3):
                url = yige['url']
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
        else:
            self.driver.get(response.url)
            self.driver.find_element_by_xpath('//a[@class="j a_show_full"]').click()
            jieshao2 = self.driver.find_element_by_xpath('//span[@class="all hidden"]').text
            item['intro'] = jieshao2

        return item