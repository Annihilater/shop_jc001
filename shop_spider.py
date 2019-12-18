#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/12/18 2:30 下午
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : shop_spider.py

from scrapy import cmdline

cmdline.execute('scrapy crawl shop'.split())
