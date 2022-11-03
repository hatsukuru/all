# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from  all.settings import MONGODB_URL
from pymongo import MongoClient
from all.items import AllItem


class AllPipeline:
    def process_item(self, item, spider):

        if isinstance(item,AllItem):
            self.client = MongoClient(MONGODB_URL)
            self.collection = self.client['collect_data']['public_notice']
            self.collection.insert_one(dict(item))

        else:
            print("数据存储失败")


