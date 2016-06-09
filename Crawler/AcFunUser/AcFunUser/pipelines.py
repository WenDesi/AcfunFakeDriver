# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from SQLConnector import *

class AcfunuserPipeline(object):
    db = "acfun"

    def __init__(self):
        self.SQLconn = SqlConnector(db=self.db)

    def process_item(self, item, spider):
        sql = 'update user set currExp = %d,stows=%d,comments=%d,gender=%d,level=%d,sign=%s,follows=%d,avatar=%s,posts=%d,followed=%d,fans=%d,regTime=%s,nextLevelNeed=%d,name=%s,expPercent=%d,isFriend=%d,views=%d,crawled=1 where uid = %d'
        sql = self.SQLconn.generateQuery(sql,[item['currExp'],item['stows'],item['comments'],item['gender'],item['level'],item['sign'],item['follows'],item['avatar'],item['posts'],item['followed'],item['fans'],item['regTime'],item['nextLevelNeed'],item['name'],item['expPercent'],item['isFriend'],item['views'],item['uid']])
        self.SQLconn.update(sql)
