# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import pymongo

from redis_project.settings import MONGODB_HOST, MONGODB_PORT, MONGODB_DBNAME, MONGODB_DOCNAME


# class RedisProjectPipeline(object):
#     datas = []
#
#     def __init__(self):
#         self.file = codecs.open('data.json', 'w+', 'utf-8')
#
#     def process_item(self, items, spider):
#         self.datas.append(items)
#         data = json.dumps(self.datas, ensure_ascii=False) + '\n'
#         self.file.seek(0)
#         self.file.write(data)
#
#     def close_spider(self, spider):
#         self.file.close()


class JsonPipeline(object):

    def __init__(self):
        host = MONGODB_HOST
        port = MONGODB_PORT
        dbname = MONGODB_DBNAME
        docname = MONGODB_DOCNAME
        # 建立MongoDB数据库连接
        client = pymongo.MongoClient(host=host, port=port)
        # 连接所需数据库,dbname为数据库名
        tdb = client[dbname]
        # 连接所用集合，也就是我们通常所说的表，docname为表名
        self.client = tdb[docname]

    def process_item(self, item, spider):
        data = dict(item)
        self.client.insert(data)
        print(data)
