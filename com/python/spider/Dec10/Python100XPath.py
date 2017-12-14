from lxml import etree
from bs4 import BeautifulSoup
import requests
import re


def get_info_list(url):
    text = requests.get(url).text
    structure = etree.HTML(text)
    # //*[@id="content"]/ul[1]/li/a
    title_li = structure.xpath('//*[@id="content"]/ul[1]/li/a/@href')
    for url in title_li:
        print(url)

        yield 'http://www.runoob.com' + url


def get_info_text(url_list):
    #因为传进来的是 generator,  所以要来重新遍历
    for temp_url in url_list:
        text = requests.get(temp_url)
        text.encoding = 'utf-8'
        structure = etree.HTML(text.text)
        title_li = structure.xpath('//*[@id="content"]/h1/text()')

        # string 是拿到所有的第一个符合这个内容的所有的文本内容
        xxs = structure.xpath('string(//*[@id="content"]/h1)')
        content_li = structure.xpath('//*[@id="content"]/p[position()<4 and position()>1]/text()')
        content = '\n'.join(content_li)
        print(title_li, content)
        yield content


#一定要注意 yield 的执行
xxx = get_info_list("http://www.runoob.com/python/python-100-examples.html")
context = get_info_text(xxx)
