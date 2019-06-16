# -*- coding: utf-8 -*-
import scrapy
from dangdang.items import DangdangItem
from scrapy.http import Request


class AutopjtSpider(scrapy.Spider):
    name = 'autopjt'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/pg1-cid4011029.html']
    def parse(self, response):
        # item=DangdangItem()
        # print("*************************调试************************")
        # item["name"]=response.xpath("//a[@class='pic']/@title").extract()
        # item["price"]=response.xpath("//span[@class='price_n']/text()").extract()
        # item["link"]=response.xpath("//a[@class='pic']/@href").extract()
        # item["comments"]=response.xpath("//a[@name='itemlist-review']/text()").extract()
        # # return item
        # yield item
        for i in range(1,10):
        	url='http://category.dangdang.com/pg'+str(i)+'-cid4011029.html'
        	yield Request(url,callback=self.parse_book)
    def parse_book(self,response):
        item=DangdangItem()
        print("*************************调试************************")
        item["name"]=response.xpath("//a[@class='pic']/@title").extract()
        item["price"]=response.xpath("//span[@class='price_n']/text()").extract()
        item["link"]=response.xpath("//a[@class='pic']/@href").extract()
        item["comments"]=response.xpath("//a[@name='itemlist-review']/text()").extract()
        yield item
# http://category.dangdang.com/pg2-cid4011029.html
# pat1="//a[class='pic']/@title"
# pat2="//span[@class='price_n']/text()"
# pat3="//a[@class='pic'/@href]"
# pat4="//a[@name='itemlist-review']"
# https://detail.tmall.com/item.htm?id=580598531793&ali_refid=a3_430673_1006:1182090123:N:hkvM8FoL/6AKeIuJU26hTA==:7f1e0216310dedea20661c567223b13a&ali_trackid=1_7f1e0216310dedea20661c567223b13a&spm=a2e15.8261149.07626516002.8