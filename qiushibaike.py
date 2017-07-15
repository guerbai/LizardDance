# -*- coding:utf-8 -*-
__author__ = 'fybhp'

# get_text()获取span下的所有文字内容.
import json
import codecs
import requests
from bs4 import BeautifulSoup
from common import get_random_header


TARGET_URL = 'https://www.qiushibaike.com/'
NORMAL_FIX = '8hr/page/{}/?s=5000294'
HOT_URL = 'https://www.qiushibaike.com/hot/'
HOT_FIX = 'page/{}/?s=5000302'
TOTAL_PAGE = 35


def get_soup(url):
    header = get_random_header()
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.content, 'lxml')
    return soup


def get_page_urls():
    page_urls = []
    for i in range(TOTAL_PAGE):
        if i == 0:
            page_urls.append(TARGET_URL)
            continue
        page_urls.append(TARGET_URL+NORMAL_FIX.format(i+1))
    for i in range(TOTAL_PAGE):
        if i == 0:
            page_urls.append(HOT_URL)
            continue
        page_urls.append(HOT_URL+HOT_FIX.format(i+1))
    return page_urls


def get_page_duanzi_from_page_soup(page_soup):
    page_duanzi = []
    target_divs = page_soup('div', class_='article block untagged mb15')
    for div in target_divs:
        # print div('div', class_='content')[0].span.get_text()#[6:-7]
        # exit(1)
        duanzi = {
            'author': div('h2')[0].string,
            'content': div('div', class_='content')[0].span.get_text()
        }
        page_duanzi.append(duanzi)
    return page_duanzi


def main():
    all_duanzi = []
    page_urls = get_page_urls()
    print "糗事百科现有{}页".format(len(page_urls))
    print "将保存在项目根目录下糗事百科.json"
    for page_url in page_urls:
        page_soup = get_soup(page_url)
        page_duanzi = get_page_duanzi_from_page_soup(page_soup)
        all_duanzi.extend(page_duanzi)
        print "又爬取了一页"
    print "总共爬取了{}个段子".format(len(all_duanzi))

    with codecs.open(u'糗事百科.json', 'wb', encoding='utf-8') as f:
        f.write(json.dumps(all_duanzi, indent=4).decode('unicode_escape'))


if __name__ == '__main__':
    main()
