# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IndianmoviecelebritiesItem(scrapy.Item):
    # define the fields for your item here like:
    celebrity_name = scrapy.Field()
    celebrity_image_link = scrapy.Field()
    celebrity_role = scrapy.Field()
    celebrity_detail = scrapy.Field()
                             