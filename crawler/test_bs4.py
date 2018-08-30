#coding=utf-8
import re

from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
# 创建BeautifulSoup对象，将文档字符串加载成为dom树
soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')
print soup.prettify()
print '获取所有的链接'
# find_all()搜索出所有满足要求的节点
links = soup.find_all('a')
for link in links:
    print link.name, link['href'], link.get_text()

print '获取lacie的链接'
# find()只会搜索出满足要求的第一个节点
link_node = soup.find('a', href='http://example.com/lacie')
print link_node.name, link_node['href'], link_node.get_text()

print '正则匹配'
link_node = soup.find('a', href=re.compile(r'ill'))
print link_node.name, link_node['href'], link_node.get_text()

print '获取p段落文字'
p_node = soup.find('p', class_='title')
print p_node