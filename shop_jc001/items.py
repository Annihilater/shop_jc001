# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ShopJc001Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class GoodItem(scrapy.Item):
    url = scrapy.Field()
    image = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
