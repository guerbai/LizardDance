# -*- coding:utf-8 -*-
__author__ = 'fybhp'

import requests
from bs4 import BeautifulSoup
from common import FILE_DIR, make_file_dir

PER_PAGE = 50
SPIDER_BASE_DIR = "/".join(__file__.split("/")[:-1]) + FILE_DIR + '/' + __file__.split("/")[-1].split(".")[0]
URL_TEMPLATE = 'http://blog.sina.com.cn/s/articlelist_1191258123_0_{}.html'
TOTAL_PAGE = 7


def create_file_dir():
    # 建立此脚本在file下的目录，并在其下每一页建立一个目录.
    make_file_dir(SPIDER_BASE_DIR)
    for i in range(TOTAL_PAGE):
        page_file_dir = SPIDER_BASE_DIR + '/' + str(i + 1)
        make_file_dir(page_file_dir)


def generate_catalog_links():
    return [URL_TEMPLATE.format(i + 1) for i in range(TOTAL_PAGE)]


def get_page_blog_urls(page_url):
    urls = []
    content = requests.get(page_url).content
    soup = BeautifulSoup(content, "lxml")
    with open('1.html', 'w') as f:
        f.write(content)
    for i in soup.find_all("span", class_='atc_title'):
        urls.append(i.a['href'])
    return urls


def download_page(page, artical_url, artical_name):
    content = requests.get(artical_url).content
    with open(artical_name, 'w') as f:
        f.write(content)


def main():
    create_file_dir()
    catelog_links = generate_catalog_links()
    for index, catelog_link in enumerate(catelog_links):
        blog_urls = get_page_blog_urls(catelog_link)
        for artical_name, blog_url in enumerate(blog_urls):
            download_page(index, blog_url, str(artical_name) + '.html')
            print "download ", index, blog_url


if __name__ == "__main__":
    main()
