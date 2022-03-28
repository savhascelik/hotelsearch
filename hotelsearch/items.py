# -*- coding: utf-8 -*-
import scrapy

class hotelsearchitems(scrapy.Item):
    hotel_name = scrapy.Field()
    hotel_url = scrapy.Field()
    hotel_category=scrapy.Field()
    hotel_comment_count=scrapy.Field()
    hotel_star=scrapy.Field()
    hotel_adress = scrapy.Field()
    crawl_time = scrapy.Field()
    crawl_date = scrapy.Field()
