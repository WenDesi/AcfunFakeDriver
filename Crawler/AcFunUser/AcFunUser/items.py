# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AcfunuserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    uid = scrapy.Field()
    currExp = scrapy.Field()
    stows = scrapy.Field()
    comments = scrapy.Field()
    gender = scrapy.Field()
    level = scrapy.Field()
    follows = scrapy.Field()
    posts = scrapy.Field()
    followed = scrapy.Field()
    nextLevelNeed = scrapy.Field()
    expPercent = scrapy.Field()
    isFriend = scrapy.Field()
    views = scrapy.Field()
    fans = scrapy.Field()
    sign = scrapy.Field()
    name = scrapy.Field()
    regTime = scrapy.Field()
    lastLoginDate = scrapy.Field()
    avatar = scrapy.Field()
