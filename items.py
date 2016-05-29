# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html/Users/jinxedin/Sites/scraped/g_pic_places/g_pic_places/pipelines.py
/Users/jinxedin/Sites/scraped/g_pic_places/g_pic_places/spiders/wiki_pic_spider.py
import scrapy
/Users/jinxedin/Sites/scraped/g_pic_places/g_pic_places/settings.py

class GPicPlacesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city_name = scrapy.Field()
    img_urls = scrapy.Field()
    pics = scrapy.Field()

