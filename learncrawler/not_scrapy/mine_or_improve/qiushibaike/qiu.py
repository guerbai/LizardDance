# -*- coding:utf-8 -*-
__author__ = 'fybhp'
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
	
def get_pages(url):
    """
    获取糗事百科热帖页数。
    """
    soup=get_soup(url)
    nums=soup.find_all('span',class_='page-numbers')
    pages=int(nums[-1].text)
    return pages

def get_duanzi(url):
    '''
    获得url页面的所有段子,以列表形式保存，有图片的段子就不保存了。
    '''
    #duanzimen = []
    #soup = get_soup(url)
    #qianyibu = soup.find_all('div',class_="article block untagged mb15")
   # #print qianyibu
    #for item in qianyibu:
		#haveimg = item.find('img')
		#if haveimg == []:
        #duanzi = item.find_all('div',class_ = "content")
		#dangeduanzi = duanzi.text
        #duanzimen.append(dangeduanzi)
    #for item in duanzi:
        #dangeduanzi = item.text
        #duanzimen.append(dangeduanzi)
    #return duanzimen
    duanzimen = []
    soup=get_soup(url)
    qianyibu = soup.find_all('div',class_="article block untagged mb15")
    for i in qianyibu:
	    haveimg1 = i.find_all('img')
	    haveimg2 = haveimg1[1:2]
	    if haveimg2 ==[]:
		    s = i.find_all('div',class_="content")[0].text
#haveimg = qianyibu[0].find('img')
#need = soup.find_all('div',STYLE="min-height:22px")
		    duanzimen.append(s)
#print duanzimen
    return duanzimen

def getOneStory(duanzimen):
        #遍历一页的段子
    for story in duanzimen:
        #等待用户输入
        input = raw_input()
        #如果输入Q则程序结束
        if input != "Q":
            print story
        else:
            exit()
    return 0

def main(start_page):

    print u"正在读取糗事百科,按回车查看新段子，Q退出"
    while start_page <= page_num:
        url = 'http://www.qiushibaike.com/hot/page/'+str(start_page)
        soup = get_soup(url)
        duanzimen = get_duanzi(url)
        getOneStory(duanzimen)
        start_page += 1
    else:
        exit()


if __name__=='__main__':
    url='http://www.qiushibaike.com/hot/'
    page_num=get_pages(url)
    print u'***************糗事百科一共有 %d 页******************' %page_num
    start_page=input(u'Input the first page number:\n')
    if start_page<=page_num:
        main(start_page)
    else:
        print u"输入错误，起始页必须小于等于结束页\n"

