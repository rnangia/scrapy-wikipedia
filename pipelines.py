# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import csv
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from g_pic_places import settings

def write_to_csv(item):
	writer = csv.writer(open('/Users/jinxedin/Sites/scraped/data/wiki_pics.csv','a'), lineterminator='\n')
	print "Writing to CSV ..." 
	city = item['city_name']
	url = item['img_urls']
	pic = item['pics']
	print item['city_name']
	print item['img_urls']
	print item['pics']
	writer.writerow([city.encode('utf-8'),url.encode('utf-8'),pic])
	print "Done"


class GPicPlacesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['img_urls'])

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['pics'] = image_paths
        write_to_csv(item)
        return item