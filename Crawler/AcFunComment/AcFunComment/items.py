# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AcfuncommentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cid = scrapy.Field()
    pageID = scrapy.Field()
    content = scrapy.Field()
    postDate = scrapy.Field()
    userID = scrapy.Field()
    userName = scrapy.Field()
    userImg = scrapy.Field()
    count = scrapy.Field()
    deep = scrapy.Field()
    refCount = scrapy.Field()
    ups = scrapy.Field()
    downs = scrapy.Field()
    nameRed = scrapy.Field()
    avatarFrame = scrapy.Field()
