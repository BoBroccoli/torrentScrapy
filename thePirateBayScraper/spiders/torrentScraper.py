# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from thePirateBayScraper.items import *

class TorrentscraperSpider(CrawlSpider):
    name = 'torrentScraper'
    start_urls = ['http://thepiratebay3.org/?url=https://tpbship.org/recent/']

    rules = (
        Rule(LinkExtractor(allow='/?url=https://thepiratebay-org.prox.fun/torrent/', restrict_xpaths='//div[@class="detName"]'), callback='parse_item'),
        Rule(LinkExtractor(allow='/?url=https://thepiratebay-org.prox.fun/recent'))
    )

    def parse_item(self, response):
        item = torrentItem()
        item['title'] = response.xpath('//div[@id="title"]/text()').extract_first()
        item['magnet'] = response.xpath('//div[@class="download"]/a/@href').extract_first()
        yield item
