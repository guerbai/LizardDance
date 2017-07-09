# -*- coding:utf-8 -*-
__author__ = 'fybhp'
import scrapy
from scrapy.selector import Selector
from Airplane.items import AirplaneItem
import json,random
from dict import abbr
import datetime

class TicketSpider(scrapy.Spider):
    name = "ticket"
    allowed_domains = ["flight.elong.com"]
    start_urls = []

    def __init__(self):
        DepartCity = raw_input('DepartCity:').encode('utf-8')
        ArriveCity = raw_input('ArriveCity:').encode('utf-8')
        your_price = raw_input('Please give your willing price:')
        self.your_price = your_price
        for i in range(31):
            DepartDate = str(datetime.date.today() +datetime.timedelta(days = i))
            self.start_urls.append('http://flight.elong.com/isajax/OneWay/S?_='+str(random.randint(1000000000000,
                                    1999999999999))+'&PageName=list&FlightType=OneWay&DepartCity='+\
                                    abbr[DepartCity.decode('utf-8')]+'&ArriveCity='+\
                                    abbr[ArriveCity.decode('utf-8')]+'&DepartDate='+DepartDate)

    def parse(self,response):
        sel = json.loads(response.body,encoding='utf-8')
        item = AirplaneItem()
        for yige in sel['value']['MainLegs']:
            item['minp'] = yige['minp']
            if str(item['minp']) <= self.your_price:
                item['corpn'] = yige['segs'][0]['corpn']
                item['dtime'] = yige['segs'][0]['dtime']
                item['atime'] = yige['segs'][0]['atime']
                item['remainnum'] = yige['cabs'][0]['tc']
                #item['fltno'] = yige['segs'][0]['fltno']
                #item['plane'] = yige['segs'][0]['plane']
                #item['pk'] = yige['segs'][0]['pk']
                #item['dportn'] = yige['segs'][0]['dportn']
                #item['aportn'] = yige['segs'][0]['aportn']
                #item['meat'] = yige['segs'][0]['meat']
                #item['on'] = str(yige['segs'][0]['on']) + '%'
                #item['tax'] = yige['tax']
                yield item
            else:
                continue
