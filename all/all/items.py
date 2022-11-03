# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AllItem(scrapy.Item):#####公告表
    # define the fields for your item here like:
    # name = scrapy.Field()
    cid = scrapy.Field()
    company = scrapy.Field()
    ann_content = scrapy.Field()
    ann_title = scrapy.Field()
    ann_date = scrapy.Field()
    ann_addr = scrapy.Field()
    ann_type = scrapy.Field()
    publisher = scrapy.Field()
    source = scrapy.Field()
    data_update_date = scrapy.Field()
    related_id = scrapy.Field()
    attachment = scrapy.Field()
