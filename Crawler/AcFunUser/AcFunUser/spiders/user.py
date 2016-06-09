from __future__ import absolute_import

import re
import json
import scrapy
import codecs

from ..items import *
from ..SQLConnector import *

class Comment(scrapy.Spider):
    name = "user"
    allowed_domains = ["acfun.tv"]

    def read_uid(self):
        sqlConn = SqlConnector(db='acfun')
        sql = 'select uid from user where crawled = 0'
        results = sqlConn.select(sql)

        for result in results:
            uid = int(result[0])
            self.uids.append(uid)

    def start_requests(self):
        basic_url = "http://www.acfun.tv/usercard.aspx?uid=%d"
        self.uids = []
        self.read_uid()

        for id in self.uids:
            url = basic_url.replace("%d",str(id))
            yield scrapy.http.Request(url,self.parse)

    def anlysis_comment_json(self,json_data):
        results = []
        s = json.loads(json_data)

        if not s['success']:
            return results

        item = AcfunuserItem()
        print int(s['userjson']['uid'])
        item['uid'] = int(s['userjson']['uid'])
        item['currExp'] = int(s['userjson']['currExp'])
        item['stows'] = int(s['userjson']['stows'])
        item['comments'] = int(s['userjson']['comments'])
        item['gender'] = int(s['userjson']['gender'])
        item['level'] = int(s['userjson']['level'])
        item['follows'] = int(s['userjson']['follows'])
        item['posts'] = int(s['userjson']['posts'])
        item['followed'] = int(s['userjson']['followed'])
        item['nextLevelNeed'] = int(s['userjson']['nextLevelNeed'])
        item['expPercent'] = int(s['userjson']['expPercent'])
        item['isFriend'] = int(s['userjson']['isFriend'])
        item['views'] = int(s['userjson']['views'])
        item['fans'] = int(s['userjson']['fans'])
        try:
            item['sign'] = str(s['userjson']['sign']).encode('utf-8')
        except:
            item['sign'] = 'empty'
        item['name'] = str(s['userjson']['name']).encode('utf-8')
        item['regTime'] = str(s['userjson']['regTime']).encode('utf-8')
        item['lastLoginDate'] = str(s['userjson']['lastLoginDate']).encode('utf-8')
        item['avatar'] = str(s['userjson']['avatar']).encode('utf-8')

        return item

    def parse(self, response):
        json_data = response.body
        item = self.anlysis_comment_json(json_data)
        return item



