# -*- coding: utf-8 -*-


from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from putin_mysql.items import PutinMysqlItem

class baiduyuedu(CrawlSpider):
    name = "bdyd"
    allowed_domains = ["yuedu.baidu.com"]
    start_urls = ["http://yuedu.baidu.com/book/list/0?od=0&show=1&pn=0"]
    rules = [Rule(SgmlLinkExtractor(allow=('/ebook/[^/]+fr=booklist')), callback='myparse'),
             Rule(SgmlLinkExtractor(allow=('/book/list/[^/]+pn=[^/]+', )), follow=True)]

    def myparse(self, response):
        x = HtmlXPathSelector(response)
        item = PutinMysqlItem()

        # get item
        item['link'] = response.url
        item['title'] = ""
        strlist = x.select("//h1/@title").extract()
        if len(strlist) > 0:
            item['title'] = strlist[0]
        # return the item
        return item