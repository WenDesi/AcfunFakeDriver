#encoding=utf-8

import json
import codecs
from SQLConnector import *

def read_db(sql):
    db = 'acfun'
    sqlConn = SqlConnector(db=db)
    results = sqlConn.select(sql)

    json_list = []
    for result in results:
        cid = result[0]
        content = result[1]

        json_list.append({'cid':cid,'content':content})
    return json_list

def write_file(filepath,json_data):
    file_object = codecs.open(filepath,'w','utf-8')
    file_object.write(json_data)
    file_object.close()


if __name__ == '__main__':
    filepath = 'comment_1000.json'
    sql = 'select cid,content from comment_withuser limit 0,1000'

    json_list = read_db(sql)
    json_data = json.dumps(json_list)
    write_file(filepath,json_data)
