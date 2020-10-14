from services.test import test
from base.result import result
from flask import json
re = result()
def controller(app):
    @app.route('/a')
    def testa():
        s = test()
        re.getResult(s)

        return toJson(re)













def toJson(data):

    dic = data.__dict__
    dictToJson(dic)
    return json.dumps(dic)

def dictToJson(dic):
    for key in dic.keys():
        value = dic[key]
        if isinstance(value, list):
            dic[key] = arrayToJson(value)
        elif isinstance(value, dict):
            pass
        elif isinstance(value, int):
            pass
        elif isinstance(value, float):
            pass
        elif isinstance(value, str):
            pass
        else:
            dic[key] = value.__dict__
            dictToJson(dic[key])

def arrayToJson(array):
    arr = []
    for item in array:
        empty = {}
        if isinstance(item, list):
            empty = list
            arrayToJson(empty)
        elif isinstance(item, dict):
            empty = item
            dictToJson(empty)
        elif isinstance(item, int):
            empty = item
        elif isinstance(item, float):
            empty = item
        elif isinstance(item, str):
            empty = item
        else:
            empty = item.__dict__
            dictToJson(empty)

        arr.append(empty)
    return arr

