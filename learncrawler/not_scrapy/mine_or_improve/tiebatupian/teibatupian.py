# -*- coding:utf-8 -*-
__author__ = 'fybhp'
import requests, json
from bs4 import BeautifulSoup
import os
import os.path
import urllib

global s
s = requests.session()
def get_soup(url):
	#soup一下
    h = s.get(url)
    html = h.content
    soup = BeautifulSoup(html,"html.parser")
    return soup

def path(f,z,y):
	dir_name=os.path.join(f,z)
	if not os.path.exists(dir_name):
		print u'---正在创建目录\"'+z+'\"---'
		os.makedirs(dir_name)
	else:
		pass
	dir_name2 = os.path.join(dir_name,y)
	if not os.path.exists(dir_name2):
		print u'---正在创建目录\"'+y+'\"---'
		os.makedirs(dir_name2)
	else:
		pass
	return dir_name2

def check_xuanze_zhuti(xuanze_zhuti,zhuti):
	add_url = ''
	for yigezhuti in zhuti:
		if xuanze_zhuti == yigezhuti[0]:
			add_url = yigezhuti[1]
	while add_url == '':
		print u'该主题不存在，请重新输入。\n'
		xuanze_zhuti = raw_input(u'请选择主题：\n').decode('utf-8')
		add_url,xuanze_zhuti = check_xuanze_zhuti(xuanze_zhuti,zhuti)
	else:
		return add_url,xuanze_zhuti

def check_xuanze_tuce(xuanze_tuce,tuce):
	tid = ''
	pe = ''
	for yigetuce in tuce:
		if xuanze_tuce == yigetuce[0]:
			tid = yigetuce[1]
			pe = yigetuce[2][:-1]
	while tid  == '':
		print u'图册不存在，请重新输入。\n'
		xuanze_tuce = raw_input(u'请选择图册：\n').decode('utf-8')
		tid,pe,xuanze_tuce  = check_xuanze_tuce(xuanze_tuce,tuce)
	else:
		return tid,pe,xuanze_tuce

def get_zhuti_neirong(main_url):
	#得到1，主题名；2，主题url；3，某主题图册数
	zhuti_neirong = []
	soup =get_soup(main_url)
	zhuti_tag = soup.find_all('div',class_="grbh_left")
	for item in zhuti_tag:
		yige_zhutiming = item.a.text
		yige_zhutiurl = item.a['href']
		yige_tuceshu = item.span.text
		zhuti_neirong.append([yige_zhutiming,yige_zhutiurl,yige_tuceshu])
	return zhuti_neirong
	
def get_tuce_neirong(zhuti_url):
	#得到1，图册名；2，图册id；3，某图册中图片个数
	tuce_neirong = []
	soup = get_soup(zhuti_url)
	tuce_tag = soup.find_all('div',class_="grbm_ele_wrapper")
	for item in tuce_tag:
		yige_tuceming = item.div.a.text
		#若图册最后为...，在创建目录时会出现差异，导致错误，在这里将...去掉。
		if yige_tuceming[-3:] == '...':
			yige_tuceming = yige_tuceming[:-3]
		yige_tuceid = item.a['href']
		yige_tupiangeshu = item.span.text
		tuce_neirong.append([yige_tuceming,yige_tuceid,yige_tupiangeshu])
	return tuce_neirong

#处理json，得到所需要信息。
def get_pic_address(json_url):
	pic_addres = []
	h = s.get(json_url)
	html = h.content.decode('unicode-escape')
	target = json.loads(html)
	for item in target['data']['pic_list']:
		pic_addres.append(item['purl'])
	return pic_addres

def pic_download(pic_address,dir_name2):
	i = 1
	for pic in pic_address:
		pic1 = pic[:30]
		pic2 = pic[-44:]
		new_pic = pic1+'pic/item/'+pic2   #获得高清图地址
		basename=str(i) + '.jpg'
		filename=os.path.join(dir_name2,basename)
		if not os.path.exists(filename):
			print 'Downloading '+filename + '......'
			urllib.urlretrieve(new_pic,filename)
		else:
			print filename+u'已存在，略过'
		i += 1

def main():
	tieba_name = raw_input(u'请输入贴吧名称：\n').decode('utf-8')
	main_url = 'http://tieba.baidu.com/photo/g?kw=' + tieba_name + '&ie=utf-8'
	zhuti = get_zhuti_neirong(main_url)
	if zhuti == []:
		print u'抱歉，该贴吧图片区是空的。\n'
		exit()
	#print zhuti
	for yigezhuti in zhuti:
		print yigezhuti[0] + '   ' + yigezhuti[2] + u'个图册'
	xuanze_zhuti = raw_input(u'请选择主题：\n').decode('utf-8')
	add_url,xuanze_zhuti = check_xuanze_zhuti(xuanze_zhuti,zhuti)
	zhuti_url = 'http://tieba.baidu.com/photo/g?kw=' + tieba_name + '&ie=utf-8&cat_id='+ str(add_url[10:])
	tuce = get_tuce_neirong(zhuti_url)
	#print tuce
	for yigetuce in tuce:
		print yigetuce[0] + '   ' + yigetuce[2] + u'图片'
	xuanze_tuce = raw_input(u'请选择图册：\n').decode('utf-8')
	tid, pe,xuanze_tuce = check_xuanze_tuce(xuanze_tuce,tuce)
	json_url = 'http://tieba.baidu.com/photo/g/bw/picture/list?kw='+tieba_name+'&alt=jview&rn=200&tid='+str(tid[3:])+'&pn=1&ps=1&pe='+str(pe)+'&info=1'
	#print json_url
	pic_address = get_pic_address(json_url)
	#print  pic_address
	dir_name2 = path(tieba_name,xuanze_zhuti,xuanze_tuce)
	pic_download(pic_address,dir_name2)

if __name__=='__main__':
	main()
