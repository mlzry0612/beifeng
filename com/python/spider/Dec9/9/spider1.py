import urllib.request
from lxml import etree as etree
import requests



response = urllib.request.urlopen("http://www.beautyleg.com/sample.php?no=1537",  timeout=100)
#print(response.read().decode())

#平常读中文可以用 decode(bgk)，基于网站自己的编码

#也可以先构建 request 对象, 这是原来 urllib2的功能。
request = urllib.request.Request("http://www.beautyleg.com/sample.php?no=1537")
urllib.request.urlopen(request)

#用requests
#content = requests.get("http://www.beautyleg.com/sample.php?no=1537").content
##htmlsource = etree.HTML(content)
#find = htmlsource.find('/html/body/table[2]/tbody/tr/td/table/tbody')
#print(find)
#