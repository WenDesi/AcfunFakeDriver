# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CommentItem(scrapy.Item):
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

# class UserItem(scrapy.Item):
#     currExp = scrapy.Field()
#     stows = scrapy.Field()
#     comments = scrapy.Field()
#     avatarFrame = scrapy.Field()
#     gender = scrapy.Field()
#     level = scrapy.Field()
#     sign = scrapy.Field()
#     follows = scrapy.Field()
#     lastLoginDate = scrapy.Field()
#     avatar = scrapy.Field()
#     posts = scrapy.Field()
#     followed = scrapy.Field()
#     lastLoginIp = scrapy.Field()
#     fans = scrapy.Field()
#     uid = scrapy.Field()
#     regTime = scrapy.Field()
#     nextLevelNeed = scrapy.Field()
#     name = scrapy.Field()
#     dTime = scrapy.Field()
#     expPercent = scrapy.Field()
#     isFriend = scrapy.Field()
#     views = scrapy.Field()

