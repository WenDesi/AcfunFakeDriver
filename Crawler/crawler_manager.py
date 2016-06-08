#encoding=utf-8

import re
import codecs
from pyquery import PyQuery as pq

def download_page(url):
    d = pq(url)
    return d.html()

def write_file(llist,filepath='acfun/acfun/ac_url_list.txt'):
    file_object = codecs.open(filepath,'w','utf-8')
    for url in llist:
        page_id = re.findall('[0-9]+',url)[0]
        file_object.write(page_id+'\n')
    file_object.close()

def extract_pageId(content):
    llist = re.findall("http://www.acfun.tv/v/ac[0-9]+",content)

    no_duplicate_list = []
    for url in llist:
        if url not in no_duplicate_list:
            no_duplicate_list.append(url)

    return no_duplicate_list


if __name__ == '__main__':
    content = download_page('http://www.acfun.tv')
    url_list = extract_pageId(content)
    write_file(url_list)