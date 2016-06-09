from __future__ import absolute_import

import re
import json
import scrapy
import codecs

from ..items import *
from ..SQLConnector import *

class Comment(scrapy.Spider):
    name = "comment"
    allowed_domains = ["acfun.tv"]
    pageId_filepath = 'AcFunComment/ac_url_list.txt'

    def read_pageId(self):
        result = []
        file_obj = codecs.open(self.pageId_filepath,'r','utf-8')
        while True:
            line = file_obj.readline()
            line=line.strip('\r\n')
            if not line:
                break
            result.append(line)
        file_obj.close()
        return result

    def read_cid(self):
        sqlConn = SqlConnector(db='acfun')
        sql = 'select cid from comment'
        results = sqlConn.select(sql)

        for result in results:
            cid = int(result[0])
            self.cids[cid] = 1

    def start_requests(self):
        basic_url = "http://www.acfun.tv/comment_list_json.aspx?contentId=%d&currentPage=1"
        self.cids = {}
        self.read_cid()

        page_Id = self.read_pageId()
        for id in page_Id:
            url = basic_url.replace("%d",id)
            yield scrapy.http.Request(url,self.parse)

    def anlysis_comment_json(self,json_data,url):
        results = []
        s = json.loads(json_data)

        if not s['success']:
            return results

        pageId = re.findall('[0-9]+',url)[0]
        comment_id_list = s['data']['commentList']

        for id in comment_id_list:
            id = 'c'+str(int(id))
            if s['data']['commentContentArr'][id]['isDelete']:
                continue

            item = AcfuncommentItem()
            item['cid'] = int(s['data']['commentContentArr'][id]['cid'])

            if item['cid'] in self.cids:
                continue
            
            item['pageID'] = str(pageId)
            item['content'] = str(s['data']['commentContentArr'][id]['content']).encode('utf-8')
            item['postDate'] = s['data']['commentContentArr'][id]['postDate']
            item['userID'] = int(s['data']['commentContentArr'][id]['userID'])
            item['userName'] = str(s['data']['commentContentArr'][id]['userName']).encode('utf-8')
            item['userImg'] = s['data']['commentContentArr'][id]['userImg']
            item['count'] = int(s['data']['commentContentArr'][id]['count'])
            item['deep'] = int(s['data']['commentContentArr'][id]['deep'])
            item['refCount'] = int(s['data']['commentContentArr'][id]['refCount'])
            item['ups'] = int(s['data']['commentContentArr'][id]['ups'])
            item['downs'] = int(s['data']['commentContentArr'][id]['downs'])
            item['nameRed'] = int(s['data']['commentContentArr'][id]['nameRed'])
            item['avatarFrame'] = int(s['data']['commentContentArr'][id]['avatarFrame'])

            results.append(item)

        return results

    def parse(self, response):
        json_data = response.body
        item_list = self.anlysis_comment_json(json_data,response.url)
        for my_item in item_list:
            yield my_item



