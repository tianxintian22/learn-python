# -*- coding:utf-8 -*-

from urllib import request, parse

req = request.Request('http://www.thsrc.com.tw/tw/TimeTable/SearchResult')

# 携带agent和origin头，防止被认为是爬虫
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')
req.add_header('Origin', 'http://www.thsrc.com.tw')

# 使用urlencode生成post数据
postData = parse.urlencode([
    ('StartStation', '2f940836-cedc-41ef-8e28-c2336ac8fe68'),
    ('EndStation' , 'f2519629-5973-4d08-913b-479cce78a356'),
    ('SearchDate' , '2018/04/18'),
    ('SearchTime' , '16:30'),
    ('SearchWay' , 'DepartureInMandarin')
])
resp = request.urlopen(req, data=postData.encode('utf-8'))

print(resp.read().decode('utf-8'))
