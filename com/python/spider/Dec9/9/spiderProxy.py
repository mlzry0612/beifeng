import urllib.parse as url_pa
import urllib.request as url_re
import urllib

post_data = {'username': 'admin', 'passwordd': '123'}

request = url_re.Request("http://www.zhihu.com")

# data 类型必是字节型的字符串
data = url_pa.urlencode(post_data).encode('utf-8')
# Define handler
proxy_sp = url_re.ProxyHandler({'http': '61.135.217.7:80'})
# Define openner
build_opener = url_re.build_opener(proxy_sp)
#也可以直接用 opener open
#build_opener.open(request, data=data, timeout=100)

# 注意这个 add header 是属性
build_opener.addheaders = [('User-Agent',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')]
# Install openner
url_re.install_opener(build_opener)

try:

    response = urllib.request.urlopen(request, data=data, timeout=100)
except url_re.HTTPError as e:
    if hasattr(e, 'code'):
        print(e.getcode())
print(response.read().decode())
