# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from .test import list

class MoviesSpider(scrapy.Spider):
    name = 'frontpage_latest'
    start_urls = ['https://fmovies.pe/']

    def parse(self, response):
        # follow links to author pages
        for href in response.xpath('//figure/a/@href'):
            yield response.follow(href, self.parse_author)


    def parse_author(self, response):
        def extract_with_css(query):
            return response.xpath(query).extract_first().strip()

        yield {
            'title': extract_with_css('//title/text()'),
            'name':extract_with_css('//div[@class="detail"]/div[@class="detail-l"]/img/@title'),
            'png': extract_with_css('//div[@class="detail"]/div[@class="detail-l"]/img/@src'),
            'link':extract_with_css('//div[@data-video]/@data-video'),
            'gener':extract_with_css('//div[@class="detail"]/div[@class="detail-r"]/div[5]/div[1]/a[1]/text()'),
            'country':extract_with_css('//div[@class="detail"]/div[@class="detail-r"]/div[5]/div[4]/a/text()'),
            'release':extract_with_css('//div[@class="detail"]/div[@class="detail-r"]/div[6]/div[2]'),
            'image':extract_with_css('//article[@id="server-f2"]/div[@class="big-cover"]/@style'),
            #'actors':extract_with_css('//div[@class="detail"]/div[@class="detail-r"]/div[5]/div[2]/a/text()'),

        }



























