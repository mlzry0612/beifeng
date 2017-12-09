import urllib.parse as url_pa
import urllib.request as url_re
import urllib
from lxml import etree as etree
import requests


post_data = {'username':'admin','passwordd':'123'}


#data 类型必是字节型的字符串
data = url_pa.urlencode(post_data).encode('utf-8')

headers2 = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}

request = url_re.Request("http://www.zhihu.com", headers=headers2)
response = urllib.request.urlopen(request, data=data,  timeout=100)


print(response.read().decode())