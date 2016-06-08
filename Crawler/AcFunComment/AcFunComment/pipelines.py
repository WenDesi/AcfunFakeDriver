# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from SQLConnector import *

class AcfuncommentPipeline(object):
    db = "acfun"                                    # 数据库名

    def __init__(self):
        self.SQLconn = SqlConnector(db=self.db)

    def process_item(self, item, spider):
        sql = 'insert into comment(cid,pageID,content,postDate,userID,userName,userImg,count,deep,refCount,ups,downs,nameRed,avatarFrame) values(%d,%d,%s,%s,%d,%s,%s,%d,%d,%d,%d,%d,%d,%d)'
        sql = self.SQLconn.generateQuery(sql,[item['cid'],item['pageID'],item['content'],item['postDate'],item['userID'],item['userName'],item['userImg'],item['count'],item['deep'],item['refCount'],item['ups'],item['downs'],item['nameRed'],item['avatarFrame']])
        self.SQLconn.insert(sql)
