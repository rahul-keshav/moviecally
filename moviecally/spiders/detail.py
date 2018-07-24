# -*- coding: utf-8 -*-
import scrapy

class DetailSpider(scrapy.Spider):
    name = 'detail'
    allowed_domains = ['www.fmovies.pe']
    start_urls = ['http://www.fmovies.pe/']

    def parse(self, response):
        pass
