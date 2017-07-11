# -*- coding:utf-8 -*-
import requests, json
from lxml import etree
from time import ctime
import random

global s
s = requests.session()
url = 'http://flight.elong.com/isajax/OneWay/S?_='+str(random.randint(1000000000000,1999999999999))+'&PageName=\
list&FlightType=OneWay&\
DepartCity=dlc&DepartCityName=%E5%A4%A7%E8%BF%9E&DepartCityNameEn=Dalian&ArriveCity=cgo&\
ArriveCityName=%E9%83%91%E5%B7%9E&ArriveCityNameEn=Zhengzhou&DepartDate=2016-04-10'
h = s.get(url)
html = h.content.decode('utf-8')
target = json.loads(html)
mainlegs=  target['value']['MainLegs']
lowestprice = []
for i in mainlegs:
    lowestprice.append(i['minp'])
print lowestprice


