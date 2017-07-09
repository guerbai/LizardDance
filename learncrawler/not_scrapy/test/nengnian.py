# -*- coding:utf8 -*-

import urllib2, os, os.path, urllib, random
from bs4 import BeautifulSoup

def get_soup(url):
    """
    获取网站的soup对象
    """
    my_headers = [
    'Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30',
    'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)',
    'Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)']
    header={"User-Agent":random.choice(my_headers)}
    req=urllib2.Request(url, headers=header)
    html=urllib2.urlopen(req).read()
    soup=BeautifulSoup(html,"html.parser")
    return soup

def zhutishu(url):
    zhuti = []
    soup = get_soup(url)
    zhaozhuti = soup.find_all('a',class_="grbh_left_title")
    for i in zhaozhuti:
        yigezhuti = i.text
        zhuti.append(yigezhuti)
    return zhuti

#def tujishu(url):


def download(url):
    soup = get_soup(url)
    zhaotupian = soup.find_all('img',id="dlg_pi_img")
    print zhaotupian
    #print u"共有d%张图片。"%len(zhaotupian)
    i = 1
    for yigetupian in zhaotupian:
        filename = i+'.jpg'
        image=yigetupian['src']
        print image
        urllib.urlretrieve(image,filename)
        i += 1





url = 'http://tieba.baidu.com/p/3216382271#!/l/p1'
download(url)