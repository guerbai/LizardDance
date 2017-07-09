# -*- coding:utf-8 -*-
__author__ = 'fybhp'
import scrapy
from scrapy.selector import Selector
from tieba_pic.items import TiebaPicItem
import json,sys
reload(sys)
sys.setdefaultencoding('utf-8')

class TiebapicSpider(scrapy.Spider):
    name = "tieba"
    allowed_domains = ["tieba.baidu.com"]
    #tiebaname = raw_input('name:')
    #start_urls = ['http://tieba.baidu.com/photo/g?kw='+tiebaname+'&ie=utf-8']
    start_urls = []

    def __init__(self):
        global tiebaname
        tiebaname = raw_input('name:').decode('gbk')
        self.tiebaname = tiebaname
        self.start_urls = ['http://tieba.baidu.com/photo/g?kw='+tiebaname+'&ie=utf-8']

    def parse(self,response):
        sel = Selector(response)
        for_zhuti = sel.xpath('//a[@class="grbh_left_title"]/@href').extract()
        if for_zhuti == []:
            request = scrapy.Request(response.url,callback=self.parse_zhuti)
            yield request
        else:
            for yige in for_zhuti:
                zhuti_url = self.start_urls[0]+'&cat_id='+yige[10:]
                #print zhuti_url
                request = scrapy.Request(zhuti_url, callback=self.parse_zhuti)
                yield request

    def parse_zhuti(self,response):
        sel = Selector(response)
        item = TiebaPicItem()
        for_tuce = sel.xpath('//div[@class="grbm_ele_wrapper"]')
        for yige in for_tuce:
            #item = TiebaPicItem()
            item['zhutiname'] = sel.xpath('//a[@class="grbh_left_title"]/text()').extract()
            if item['zhutiname'] == []:
                item['zhutiname'] = u'未分类图册'
            else:
                item['zhutiname'] = item['zhutiname'][0]
            item['tucename'] = yige.xpath('./div[@class="grbm_ele_title"]/a/text()').extract()[0]
            if item['tucename'][-3:] == '...':
                item['tucename'] = item['tucename'][:-3]
            tuce_id = yige.xpath('./a[@class="grbm_ele_a grbm_ele_big"]/@href').extract()[0][3:]
            #print item['tuce_id']
            pic_num = yige.xpath('./a[@class="grbm_ele_a grbm_ele_big"]/span[1]/text()').extract()[0]
            #print item['pic_num']
            json_url = 'http://tieba.baidu.com/photo/g/bw/picture/list?kw='+self.tiebaname+'&alt=jview&rn=200&tid='+ tuce_id+'&pn=1&ps=1&pe='+pic_num+'&info=1'
            yield scrapy.Request(json_url,meta={'item': item}, callback=self.parse_json)

    def parse_json(self,response):
        sel = json.loads(response.body,encoding='latin1')#response.body, encoding="unicode-escape",ensure_ascii=False)
        item = response.meta['item']
        for yige in sel['data']['pic_list']:
            image = yige['purl']
            pic1 = image[:30]
            pic2 = image[-44:]
            #item['image_urls']为列表而不是str.
            item['image_urls'] = [pic1+'pic/item/'+pic2]
            yield item


