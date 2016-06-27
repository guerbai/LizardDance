# -*- coding:utf-8 -*-
__author__ = 'fybhp'

import urllib2
from allfiledir import allfilrdir
import os

links = [''] * 7
n = 0
page = 0

while n < 7:
    #将七页博客目录的url放入links列表中.
    links[n] = 'http://blog.sina.com.cn/s/articlelist_1191258123_0_' + str(n + 1) + '.html'
    n += 1

while page < 7:

    # 定义要创建的目录
    mkpath = allfilrdir + '/' + str(page + 1)
    if not os.path.exists(mkpath):
        print mkpath + u' 创建成功'
        os.mkdir(mkpath)
    else:
        print mkpath + u' 目录已存在'

    #content为博客目录页面的html代码字符串
    content = urllib2.urlopen(links[page]).read()
    #一页最多50篇文章,这里用了100.
    url = [''] * 100
    filename = [''] * 100
    i = 0
    #字符串的find方法抽取出博客文章的链接url.
    set_local = content.find(r'<a title')
    start = content.find(r'href', set_local)
    end = content.find(r'html', start)
    #从这个循环中出来后,url列表中有着该页面目录中所有文章的链接url.
    while set_local != 0 and i < 100:
        url[i] = content[start + 6:end + 4]
        #通过find方法的第二个参数指定开始位置,使得对字符串的操作一直在往后进行.
        set_local = content.find(r'<a title', end)
        start = content.find(r'href', set_local)
        end = content.find(r'html', start)
        i += 1
    #设定j,重新对url列表进行遍历,进行下载.
    j = 0
    while url[j] != '' and j < 50:
        filename = url[j][url[j].find(r'blog_'):]
        con = urllib2.urlopen(url[j]).read()
        open(mkpath + '/' + filename, 'w').write(con)
        print 'downloading', url[j]
        j += 1
    else:
        print 'page' + str(page + 1) + 'ok'
    page += 1
else:
    print 'all finished!'