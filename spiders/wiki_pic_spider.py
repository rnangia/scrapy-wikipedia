import scrapy
import string
import csv
import sys
from scrapy.selector import Selector
from g_pic_places.items import GPicPlacesItem


class WikiPicSpider(scrapy.Spider):
	name = "wiki_pic_places"
	allowed_domains = ["en.wikipedia.org"]
	def start_requests(self):
		with open('/Users/jinxedin/Sites/scraped/data/wiki.csv','rb') as csvfile:
			cities = csv.reader(csvfile,delimiter=',')

			for i in xrange(4533):
				city = next(cities)
				ct = unicode(city[0],'utf-8')
				ind = ct.find('(')
				if (ind !=-1 ):
					ct = ct[:ind].strip()
				city_name = string.replace(ct,' ','_').lower().title()
				url = "https://en.wikipedia.org/wiki/"+ city_name
				yield self.make_requests_from_url(url)

	def parse(self, response):
		hxs = Selector(response)
		item = GPicPlacesItem()
		city = hxs.xpath('//h1/text()').extract()
		item['city_name'] = ''.join(city)
		urls = hxs.xpath('//img[1]/@src').extract()
		url = ''.join(urls)
		url = url.replace('/thumb','')
		url_lower = url.lower()
		ind = url_lower.find('jpg')
		if (ind != -1 ):
			url = url[:(ind+3)]
		else:
			ind1 = url_lower.find('jpeg')
			if ind1 != -1:
				url = url[:(ind1+4)]
		item['img_urls'] = "https:" + url
		return item




