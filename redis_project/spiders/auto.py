# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from redis_project.items import RedisProjectItem


class AutoSpider(RedisSpider):
    name = 'auto'
    allowed_domains = ['12365auto.com']
    # start_urls = ['http://12365auto.com/']
    redis_key = 'auto:start_urls'

    def parse(self, response):
        item = RedisProjectItem()
        for i in response.xpath('//div[@class="tslb_b"]//tr[1]/following-sibling::*'):
            item['brand'] = i.xpath('.//td[2]/text()').extract()
            item['line'] = i.xpath('.//td[3]/text()').extract()
            item['car'] = i.xpath('.//td[4]/text()').extract()
            item['details'] = i.xpath('.//td[5]//text()').extract()
            item['problems'] = i.xpath('.//td[6]/text()').extract()
            item['date'] = i.xpath('.//td[7]/text()').extract()
            yield item

        for i in range(2, 5):
            # http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-1.shtml
            url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-' + str(i) + '.shtml'
            yield scrapy.Request(url, callback=self.parse)