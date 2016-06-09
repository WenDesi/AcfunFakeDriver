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
        self.read_in_user()

    def read_in_user(self):
        self.uids = {}
        sql = 'select uid from user;'
        results = self.SQLconn.select(sql)
        for result in results:
            uid = int(result[0])
            self.uids[uid] = 1

    def process_item(self, item, spider):
        sql = 'insert into comment_withuser(cid,pageID,content,postDate,userID,userName,userImg,count,deep,refCount,ups,downs,nameRed,avatarFrame) values(%d,%d,%s,%s,%d,%s,%s,%d,%d,%d,%d,%d,%d,%d)'
        sql = self.SQLconn.generateQuery(sql,[item['cid'],item['pageID'],item['content'],item['postDate'],item['userID'],item['userName'],item['userImg'],item['count'],item['deep'],item['refCount'],item['ups'],item['downs'],item['nameRed'],item['avatarFrame']])
        self.SQLconn.insert(sql)

        if item['userID'] not in self.uids:
            query = 'insert into user(uid,crawled) values(%d,%d)'
            query = self.SQLconn.generateQuery(query,[item['userID'],0])
            self.SQLconn.insert(query)
        print item['cid'],' add in database'
