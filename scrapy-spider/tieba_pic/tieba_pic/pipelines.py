# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from spiders.pic_spider import tiebaname
import os
import codecs
import json

class TiebaPicPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url,meta={'item': item})


    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        #item['image_paths'] = image_paths
        return item

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        # 从URL提取图片的文件名
        image_guid = request.url.split('/')[-1]
        # 拼接最终的文件名,格式:full/{书名}/{章节}/图片文件名.jpg
        filename = u'full/'+tiebaname+u'/{0[zhutiname]}/{0[tucename]}/{1}'.format(item, image_guid)
        return filename

class TiebaPicPipeline1(ImagesPipeline):
    def process_item(self, item, spider):
        filedir = u'full/'+tiebaname+u'/{0[zhutiname]}/{0[tucename]}'.format(item)
        if not os.path.exists(filedir):
            os.makedirs(filedir)
        with codecs.open(filedir+'/ticket5.json', 'a', encoding='utf-8') as f:
            line = json.dumps(item['image_urls'])+'\n'#dict(item)) + '\n'
            f.write(line.decode("unicode_escape"))
        return item