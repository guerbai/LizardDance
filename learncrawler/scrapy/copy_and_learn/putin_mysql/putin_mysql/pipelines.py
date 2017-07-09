# -*- coding: utf-8 -*-

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

# connect to database
class PutinMySQLPipeline(object):
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
        tx.execute(sql, (item["title"], item["link"]))