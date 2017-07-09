# -*- coding:utf8 -*-
# Python:         2.7.8
# Platform:       Windows
# Author:         wucl
# Version:        1.0
# Program:        自动下载妹子图的图片并保存到本地
# History:        2015.5.31
#                 2015.6.2  发现被禁止抓取了，增加了随机的浏览器头部信息，模拟浏览器抓取。
 
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
    soup=BeautifulSoup(html)
    return soup
     
def get_pages(url):
    """
    获取妹子图网站的页数
    """
    soup=get_soup(url)
    nums=soup.find_all('a',class_='page-numbers')
    pages=int(nums[-2].text)
    return pages
 
     
def get_menu(url):
    """
    获取页面的所有妹子图主题的链接名称和地址，记入列表
    """
    soup=get_soup(url)
    menu=[]
    menu_list=soup.find_all('a',target='_blank')
    for i in menu_list:
        result=i.find_all('img',class_='lazy')
        if result:
            name=result[0]['alt']
            address=i['href']
            menu.append([name,address])
    return menu
 
def get_links(url):
    """
    获取单个妹子图主题一共具有多少张图片
    """
    soup=get_soup(url)
    all_=soup.find_all('a')
    nums=[]
    for i in all_:
        span=i.find_all('span')
        if span:
            nums.append(span[0].text)
    return nums[-2]
             
def get_image(url,filename):
    """
    从单独的页面中提取出图片保存为filename
    """
    soup=get_soup(url)
    image=soup.find_all('p')[0].find_all('img')[0]['src']
    urllib.urlretrieve(image,filename)
 
def main(page):
    """
    下载第page页的妹子图
    """
    print u'正在下载第 %d 页' % page
    page_url=url+'/page/'+str(page)
    menu=get_menu(page_url)
    print u'@@@@@@@@@@@@@@@@第 %d 页共有 %d 个主题@@@@@@@@@@@@@@@@' %(page,len(menu))
    for i in menu:
        dir_name=os.path.join('MeiZiTu',i[0])
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        pic_nums=int(get_links(i[1]))
        print u'\n\n\n*******主题 %s 一共有 %d 张图片******\n' %(i[0],pic_nums)
        for pic in range(1,pic_nums+1):
            basename=str(pic)+'.jpg'
            filename=os.path.join(dir_name,basename)
            pic_url=i[1]+'/'+str(pic)
            if not os.path.exists(filename):
                print u'......%s' % basename,
                get_image(pic_url,filename)
            else:
                print filename+u'已存在，略过'
     
if __name__=='__main__':
    url='http://www.mzitu.com/'
    pages=get_pages(url)
    print u'***************妹子图一共有 %d 页******************' %pages
    if not os.path.exists('MeiZiTu'):
        os.mkdir('MeiZiTu')
    page_start=input(u'Input the first page number:\n')
    page_end=input(u'Input the last page number:\n')
    if page_end>page_start:
        for page in range(page_start,page_end):
            main(page)
    elif page_end==page_start:
        main(page_end)
    else:
        print u"输入错误，起始页必须小于等于结束页\n"