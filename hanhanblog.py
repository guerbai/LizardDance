# -*- coding:utf-8 -*-
__author__ = 'fybhp'

import requests
from bs4 import BeautifulSoup
from common import FILE_DIR, make_file_dir

PER_PAGE = 50
URL_TEMPLATE = 'http://blog.sina.com.cn/s/articlelist_1191258123_0_{}.html'
TOTAL_PAGE = 7

def create_file_dir():
    # 建立此脚本在file下的目录，并在其下每一页建立一个目录.
    make_file_dir(FILE_DIR)
    make_file_dir('./file/hanhanblog')


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


def download_page(artical_url, artical_name):
    content = requests.get(artical_url).content
    with open(artical_name, 'w') as f:
        f.write(content)


def main():
    create_file_dir()
    catelog_links = generate_catalog_links()
    blog_urls = []
    for page, catelog_link in enumerate(catelog_links):
        blog_urls += get_page_blog_urls(catelog_link)
        for artical_index, blog_url in enumerate(blog_urls):
            artical_name = './file/hanhanblog/{}.html'.format(artical_index)
            download_page(blog_url, str(artical_name) + '.html')
            print "download ", blog_url


if __name__ == "__main__":
    main()
