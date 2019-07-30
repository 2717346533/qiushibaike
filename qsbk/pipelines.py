# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#第一个存储方式
import json

# class QsbkPipeline(object):
#     def __init__(self):
#         self.fp = open("duanzi.json",'w',encoding='utf-8')
#
#     def open_spider(self,spider):
#         print("开始爬虫...")
#
#     def process_item(self, item, spider):
#         item_json = json.dumps(dict(item),ensure_ascii=False)
#         self.fp.write(item_json + '\n')
#         return item
#
#     def close_spider(self,spider):
#         self.fp.close()
#         print("爬虫结束了...")

#第二个存储方式
# from scrapy.exporters import JsonItemExporter
# class QsbkPipeline(object):
#     def __init__(self):
#         self.fp = open("duanzi.json",'wb')
#         self.exporter = JsonItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')
#         self.exporter.start_exporting()
#
#     def open_spider(self,spider):
#         print("开始爬虫...")
#
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item
#
#     def close_spider(self,spider):
#         self.exporter.finish_exporting()
#         self.fp.close()
#         print("爬虫结束了...")

#第三个存储方式

from scrapy.exporters import JsonLinesItemExporter
class QsbkPipeline(object):
    def __init__(self):
        self.fp = open("duanzi.json",'wb')
        self.exporter = JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')

    def open_spider(self,spider):
        print("开始爬虫...")

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self,spider):
        self.fp.close()
        print("爬虫结束了...")