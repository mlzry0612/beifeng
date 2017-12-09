import requests
import json


sfsf = {'vsvs':'sfs'}
try:
    request_post = requests.get('http://httpbin.org/cookies', cookies={'from-my': 'browser'})
    print(request_post.text)
    print(request_post.cookies)
except requests.HTTPError as e:
    print(e.errno)


r = requests.get('http://httpbin.org/stream/20', stream=True)

print(json.dumps(sfsf))

#loads. dumps 对应小块的 json

#load, dump 对应文件
with open("../config/record.json",'r') as load_f:
    load_dict = json.load(load_f)
    print(load_dict)
load_dict['smallberg'] = [8200,{1:[['Python',81],['shirt',300]]}]
print(load_dict)

with open("../config/record.json","w") as dump_f:
    json.dump(load_dict,dump_f)
