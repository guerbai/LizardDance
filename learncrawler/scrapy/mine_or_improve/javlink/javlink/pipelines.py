# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import os

class JavlinkPipeline1(object):
    def __init__(self):
        self.file = codecs.open('javtest.json', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line.decode("unicode_escape"))
        return item

class JavlinkPipeline2(object):

    def process_item(self, item, spider):
        filedir = r'torrenttest/{0[actress]}/{0[posttime]}/{0[bango]}/{0[title]}'.format(item)
        if os.path.exists(filedir) :
            if item['link'] == 'none':
                pass
            else:
                with codecs.open(filedir+'/link.txt', 'wb') as f:
                    f.write(item['link'])
        else:
            os.makedirs(filedir)
            if item['link'] =='none':
                pass
            else:
                with codecs.open(filedir+'/link.txt', 'wb') as f:
                    f.write(item['link'])
        return item

