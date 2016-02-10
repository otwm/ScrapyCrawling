# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys

import datetime
from scrapy import signals
from scrapy.exporters import JsonLinesItemExporter, XmlItemExporter

from settings import EXPORT_PATH

reload(sys)
sys.setdefaultencoding('utf-8')


class ScrapycrwalingPipeline(object):
    def process_item(self, item, spider):
        print item
        return item


class PrintItem(object):
    def process_item(self, item, spider):
        print '============= start ============='
        print item
        print '============= end ============='
        return item


class Exporter(object):
    def __init__(self):
        self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        # todo: json 변경에 대해 검토하자.(현재는 인코딩 깨짐)
        # file = open('%s.civilAppeal.json' % spider.allowed_domains[0], 'w+b')
        print 'path %s/%s.%s.civilAppeal.xml' % (
        EXPORT_PATH, spider.allowed_domains[0], datetime.date.today().isoformat())
        file = open(
            '%s/%s.%s.civilAppeal.xml' % (EXPORT_PATH, spider.allowed_domains[0], datetime.date.today().isoformat()),
            'w+b')
        self.files[spider] = file
        # self.exporter = JsonLinesItemExporter(file )
        self.exporter = XmlItemExporter(file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
