from lxml import etree
from bs4 import BeautifulSoup
import requests
import re


def get_block_url(baseUrl):
    x = requests.get("http://www.runoob.com/python/python-100-examples.html")
    x.encoding = 'utf-8'
    # 先用 text 来读取内容呀
    soup = BeautifulSoup(x.text, 'lxml')
    for i in soup.find_all('a', href=re.compile('^/python/python-exe')):
        url = i.get('href')
        print(url)
        yield url


def get_context(burl):
    for rurl in burl:
        whole_url = 'http://www.runoob.com' + rurl
        x = requests.get(whole_url)
        x.encoding = 'utf-8'
        soup = BeautifulSoup(x.text, 'lxml')
        sub_title = soup.find('div', class_='article-intro').h1.string
        print(sub_title)
        yield (sub_title, 'ssssss')


get_block_url("http://www.runoob.com/python/python-100-examples.html")
