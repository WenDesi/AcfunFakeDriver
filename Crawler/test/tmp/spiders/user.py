import scrapy

from acfun.items import *

class user(scrapy.Spider):
    name = "tt"
    allowed_domains = ["1905.com"]

    def start_requests(self):
        basic_url = "http://www.1905.com/mdb/film/list/country-China/o0d0p%s.html"

        start,end = 0,485
        for i in range(start,end):
            url = basic_url.replace("%s",str(i))
            yield scrapy.http.Request(url,self.parse)

    def parse(self, response):
        pass

    def parse_movie(self, response):
        item = CommentItem()
        item['url'] = response.url
        item['html'] = response.body

        print response.url
        return item

