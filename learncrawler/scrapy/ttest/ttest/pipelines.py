# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import log
from twisted.enterprise import adbapi
from scrapy.http import Request
from scrapy.exceptions import DropItem
from scrapy.contrib.pipeline.images import ImagesPipeline
import time
import MySQLdb
import MySQLdb.cursors
import socket
import select
import sys
import os
import errno
import codecs
import json

class HuxiuPipeline(object):
    '''def __init__(self):
        dir_name = 'full'
        if not os.path.exists(dir_name):
		    os.makedirs(dir_name)
        #filename = u'full/'+u'/{0[date]}/{0[link]}/{0[title]}'.format(item)
        self.file = codecs.open(dir_name+'/ticket5.json', 'wb', encoding='utf-8')'''

    def process_item(self, item, spider):
        filedir = u'full/{0[title]}/{0[link]}/{0[posttime]}'.format(item)
        if not os.path.exists(filedir):
            os.makedirs(filedir)
        with codecs.open(filedir+'/ticket5.json', 'wb', encoding='utf-8') as f:
            line = json.dumps(dict(item)) + '\n'
            f.write(line.decode("unicode_escape"))
        return item

# connect to database
'''class HuxiuPipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
                db = 'bookinfo',
                user = 'root',
                passwd = '501826',
                cursorclass = MySQLdb.cursors.DictCursor,
                charset = 'utf8',
                use_unicode = False
        )

    # pipeline dafault function
    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        return item

    # insert the data to databases
    def _conditional_insert(self, tx, item):
        """
        if item.get('title'):
           for i in range(len(item['title'])):
               tx.execute('insert into book values (%s, %s)', (item['title'][i], item['link'][i]))
        """
        sql = "insert into book values (%s, %s)"
        tx.execute(sql, (item["title"], item["link"]))'''