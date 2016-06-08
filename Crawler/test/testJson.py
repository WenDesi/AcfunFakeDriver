#encoding=utf-8

import json
import codecs

def read_json(filepath):
    myjson = ''
    file_obj = codecs.open(filepath,'r','utf-8')
    try:
        myjson = file_obj.read()
    finally:
        file_obj.close()
    return myjson

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

        result = []
        result.append(s['data']['commentContentArr'][id]['cid'])
        result.append(s['data']['commentContentArr'][id]['quoteId'])
        result.append(s['data']['commentContentArr'][id]['content'])
        result.append(s['data']['commentContentArr'][id]['postDate'])
        result.append(s['data']['commentContentArr'][id]['userID'])
        result.append(s['data']['commentContentArr'][id]['userName'])
        result.append(s['data']['commentContentArr'][id]['userImg'])
        result.append(s['data']['commentContentArr'][id]['count'])
        result.append(s['data']['commentContentArr'][id]['deep'])
        result.append(s['data']['commentContentArr'][id]['refCount'])
        result.append(s['data']['commentContentArr'][id]['ups'])
        result.append(s['data']['commentContentArr'][id]['downs'])
        result.append(s['data']['commentContentArr'][id]['nameRed'])
        result.append(s['data']['commentContentArr'][id]['avatarFrame'])

        results.append(result)

    return results

if __name__ == '__main__':
    json_filepath = 'comment_list_json.json'
    json_data = read_json(json_filepath)
    anlysis_comment_json(json_data)