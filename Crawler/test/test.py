#encoding=utf-8

import codecs
from pyquery import PyQuery as pq

def download_page(url):
    d = pq(url)
    return d.html()

def write_file(filepath,content):
    file_object = codecs.open(filepath,'w','utf-8')
    file_object.write(content)
    file_object.close()

if __name__ == '__main__':
    content = download_page('http://www.acfun.tv/v/ac2799504')
    write_file('downloadpage/wds.html',content)