# -*- coding: utf-8 -*-

# Scrapy settings for ttest project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'meizitu'

SPIDER_MODULES = ['ttest.spiders']
NEWSPIDER_MODULE = 'ttest.spiders'

ITEM_PIPELINES = {"ttest.pipelines.HuxiuPipeline" : 1}
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36'
