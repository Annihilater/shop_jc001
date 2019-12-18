# -*- coding: utf-8 -*-
import scrapy

from shop_jc001.items import GoodItem


class ShopSpider(scrapy.Spider):
    name = 'shop'
    allowed_domains = ['shop.jc001.cn']
    start_urls = ['http://shop.jc001.cn/1373528/goods/']

    def parse(self, response):
        goods = response.css('.goods-list li')
        for good in goods:
            url = good.css('a::attr(href)').extract_first()
            image = good.css('a img::attr(src)').extract_first()
            title = good.css('h4 a::attr(title)').extract_first()
            price = good.css('p strong::text').extract_first()

            item = GoodItem()
            for field in item.fields:
                try:
                    item[field] = eval(field)
                except NameError:
                    self.logger.debug('Field is not Defined' + field)
            yield item

        _url = response.css('.pagination li:last-child a::attr(href)').extract_first()
        if _url != '#none':
            next_page = 'http://' + self.allowed_domains[0] + _url
            yield scrapy.Request(url=next_page, callback=self.parse)
