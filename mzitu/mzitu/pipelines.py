# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

class MzituPipeline(ImagesPipeline):
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
        filename = u'full/'+u'/{0[date]}/{0[title]}/{1}'.format(item, image_guid)
        return filename

