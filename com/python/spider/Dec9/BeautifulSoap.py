from bs4 import BeautifulSoup
import bs4.element
import requests
from lxml import etree

soup = BeautifulSoup(open('html'), 'lxml')
print(soup.prettify())

print(soup.head)
print(soup.title)
print(soup.a)
print(soup.a.attrs)  # 返回 tag 的属性
print(soup.a.get("class"))

# 返回的是 navigableString
print(soup.a.string)

# BeautifulSoup
print(soup.attrs)

# comment
if type(soup.a.string) == bs4.element.Comment:
    print(soup.a.string)

print("==============父子关系树===============")
print(soup.body.contents)  #以列表的形式返回每一层子节点

for child in soup.body.chindren:  #返回当前的所有的子节点
    print(child)

#返回所有的子孙节点，自动遍历
for child in soup.descendants:
    print(child)

print(soup.title.string)
#返回最内层的文本,通俗点说就是：如果一个标签里面没有标签了，那么 .string 就会返回标签里面的内容。如果标签里面只有唯一的一个标签了，那么 .string 也会返回最里面的内容。例如

print(soup.strings)#返回多个内容
for string in soup.stripped_strings:  #去空化处理
    print(string)

print(soup.find_all('p'))

#正则
import re
for tag in soup.find_all(re.compile("^a")):
    print(tag)

#全部
print(soup.find_all(True))

print("=============CSS ==================")
# Select css class
print(soup.select('.story'))

# 『#』是用来找 ID 的
print(soup.select('#02'))

#逐层选
print(soup.find_all('a', re.compile("^k"), class_= "XXX"))

print(soup.find_all(text=["io","vvv"]))

print(soup.find_all('a', limit=10))