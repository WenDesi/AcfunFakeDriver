from __future__ import absolute_import

import json
import scrapy
import codecs

from ..items import *


class Comment(scrapy.Spider):
    name = "comment"
    allowed_domains = ["acfun.tv"]
    pageId_filepath = '../ac_url_list.txt'

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

    def start_requests(self):
        basic_url = "http://www.acfun.tv/comment_list_json.aspx?contentId=%d&currentPage=1"

        page_Id = self.read_pageId()
        for id in page_Id:
            url = basic_url.replace("%d",id)
            yield scrapy.http.Request(url,self.parse)

    def anlysis_comment_json(json_data):
        results = []
        s = json.loads(json_data)

        if not s['success']:
            return results

        comment_id_list = s['data']['commentList']

        for id in comment_id_list:
            id = 'c'+str(int(id))
            if s['data']['commentContentArr'][id]['isDelete']:
                continue

            item = CommentItem()
            item['cid'] = s['data']['commentContentArr'][id]['cid']
            item['quoteId'] = s['data']['commentContentArr'][id]['quoteId']
            item['content'] = s['data']['commentContentArr'][id]['content']
            item['postDate'] = s['data']['commentContentArr'][id]['postDate']
            item['userID'] = s['data']['commentContentArr'][id]['userID']
            item['userName'] = s['data']['commentContentArr'][id]['userName']
            item['userImg'] = s['data']['commentContentArr'][id]['userImg']
            item['count'] = s['data']['commentContentArr'][id]['count']
            item['deep'] = s['data']['commentContentArr'][id]['deep']
            item['refCount'] = s['data']['commentContentArr'][id]['refCount']
            item['ups'] = s['data']['commentContentArr'][id]['ups']
            item['downs'] = s['data']['commentContentArr'][id]['downs']
            item['nameRed'] = s['data']['commentContentArr'][id]['nameRed']
            item['avatarFrame'] = s['data']['commentContentArr'][id]['avatarFrame']

            results.append(item)

        return results

    def parse(self, response):
        json_data = response.body
        item_list = self.anlysis_comment_json(json_data)
        for my_item in item_list:
            yield my_item



