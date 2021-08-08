import json
import requests
from config import accesskeyid, access_secret, url, dbName

def post(sql: str):
    data = {"accesskeyid": accesskeyid, "access_secret": access_secret, "dbName": dbName, "action": "queryDB",
            "sparql": sql}
    # 字符串格式
    res = requests.post(url=url, data=data)
    # print(json.loads(res.text))
    return res


def get_answer_list_from_res(res, task_id, *args):
    try:
        results = json.loads(res.text)['data']['results']['bindings']
    except:
        print(res.text)
        print('Something unexpected happened!')
        exit()
    answer_list = []
    for i in range(len(results)):
        keys = list(results[i].keys())
        if task_id == 1:
            company1, company2 = args
            if 'x' in keys:
                answer_list.append([company1[1:-1], results[i]['x']['value'], company2[1:-1]])
            elif 'y' in keys:
                answer_list.append([company1[1:-1], company2[1:-1]])
        elif task_id == 2:
            company, = args
            answer = [company[1:-1]] + [results[i][key]['value'] for key in keys]
            answer_list.append(answer)
        elif task_id == 3:
            company1, company2 = args
            if set(keys) == {'a'}:
                answer_list.append([company1[1:-1], company2[1:-1], results[i]['a']['value']['value'], company1[1:-1]])
            elif set(keys) == {'a', 'b'}:
                answer_list.append([company1[1:-1], company2[1:-1], results[i]['a']['value'], results[i]['b']['value'], company1[1:-1]])
            elif set(keys) == {'a', 'b', 'c'}:
                answer_list.append([company1[1:-1], company2[1:-1], results[i]['a']['value'], results[i]['b']['value'], results[i]['c']['value'], company1[1:-1]])
            elif set(keys) == {'d'}:
                answer_list.append([company1[1:-1], results[i]['d']['value'], company2[1:-1], company1[1:-1]])
            elif set(keys) == {'a', 'd'}:
                answer_list.append([company1[1:-1], results[i]['a']['value'], company2[1:-1], results[i]['d']['value'], company1[1:-1]])
            elif set(keys) == {'a', 'd', 'c'}:
                answer_list.append([company1[1:-1], results[i]['a']['value'], company2[1:-1], results[i]['d']['value'], results[i]['c']['value'], company1[1:-1]])
            elif set(keys) == {'b', 'd'}:
                answer_list.append([company1[1:-1], results[i]['d']['value'], results[i]['b']['value'], company1[1:-1]])
            elif set(keys) == {'a', 'b', 'd'}:
                answer_list.append([company1[1:-1], results[i]['a']['value'], results[i]['b']['value'], company2[1:-1], results[i]['d']['value'], company1[1:-1]])
            elif set(keys) == {'b', 'd', 'c'}:
                answer_list.append([company1[1:-1], results[i]['d']['value'], results[i]['b']['value'], results[i]['c']['value'], company2[1:-1], company1[1:-1]])
            else:
                continue
        else:
            print('task_id error')
            exit()
        
    return answer_list


def print_answer(answer_list, short=False):
    for answer in answer_list:
        if short:
            print(' -> '.join([string[49:] for string in answer]))
        else:
            print(' -> '.join(answer))