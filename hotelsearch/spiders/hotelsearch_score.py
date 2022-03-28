# -*- coding: utf-8 -*-
import scrapy
from hotelsearch.items import hotelsearchitems
import datetime


class HotelSearchSpider(scrapy.Spider):
    name = 'hotelsearch_score'
    print("Crawl starting...")
    start_urls = ['https://www.tripadvisor.com.tr/Hotels-g2669736-Kesan_Edirne_Province-Hotels.html']
    

    def __init__(self, *args, **kwargs):
        super(HotelSearchSpider, self).__init__(*args, **kwargs)
        self.start_urls = [kwargs.get('start_url')]
  
    
    

    def parse(self, response):
        for href in response.css('.listing_title a::attr(href)'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_score)

        next_page = response.css('.nav.next.ui_button.primary::attr(href)').extract()
            


        if next_page:
            _rl = response.url
            url = _rl.split("/")[2]
            url=''.join(url)
            next_page=''.join(next_page)
            url =  "https://"+url+next_page
            yield scrapy.Request(url, self.parse)
       
    def parse_score(self, response):
        item = hotelsearchitems()
        
        # Hotel name
        try:
            item['hotel_name'] = response.css('#HEADING::text').extract()
        except Exception as e:
            pass
        
        # Hotel URL
        try:
            item['hotel_url'] = response.url
        except:
            pass

        # Hotel Adres
        try:
            item['hotel_adress'] = response.css('.ceIOZ.yYjkv::text').extract()
        except:
            pass

        # Hotel category
        try:
            item['hotel_category'] = response.css('.drcGn._R.MC.S4._a.H::text').extract()
        except:
            pass

        # Hotel comment count
        try:
            item['hotel_comment_count'] = response.css('.btQSs.q.Wi.z.Wc::text').extract()
        except:
            pass

        # Hotel star
        try:
            item['hotel_star'] = response.css('.bvcwU.P::text').extract()
        except:
            pass
        
        # Time
        try:
            item['crawl_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        except:
            pass
        
        # Date
        try:
            item['crawl_date'] = datetime.datetime.now().strftime('%Y-%m-%d')
        except:
            pass

        return item
