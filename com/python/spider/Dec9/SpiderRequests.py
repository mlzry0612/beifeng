import requests
import json

r = requests.get('http://www.baidu.com')

# 指定 encoding
r.encoding = 'uft-8'

# 字节的形式
print(r.content.decode())

# 文本
print(r.text)
print(type(r))
print(r.status_code)
print(r.encoding)
print(r.cookies.keys())

postdata = {'key': 'vv'}
headers_value = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
           'Accept - Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
           'Connection': 'Keep-Alive',
           'Host': 'zhannei.baidu.com',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
try:
    request_post = requests.get('http://www.ebay.com',  timeout=100, data=postdata)
    print(request_post)
except requests.HTTPError as e:
    print(e.errno)


try:
    request_post = requests.post('http://httpbin.org/post',  timeout=100, data=postdata)
    print(request_post)
except requests.HTTPError as e:
    print(e.errno)

try:
    request_post = requests.get('http://httpbin.org/cookies', cookies={'from-my': 'browser'})
    print(request_post.text)
    print(request_post.cookies)
except requests.HTTPError as e:
    print(e.errno)
