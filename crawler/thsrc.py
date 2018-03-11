# coding=utf-8

import urllib2
import urllib

url = 'http://www.thsrc.com.tw/tw/TimeTable/SearchResult'
request = urllib2.Request(url)

request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36')

post_data = {
    'StartStation' : '9c5ac6ca-ec89-48f8-aab0-41b738cb1814',
    'EndStation' : '977abb69-413a-4ccf-a109-0272c24fd490',
    'SearchDate' : '2018/03/12',
    'SearchTime': '16:30',
    'SearchWay' : 'DepartureInMandarin',
    'RestTime': '',
    'EarlyOrLater': ''
}
data = urllib.urlencode(post_data)
request.add_data(data)

response = urllib2.urlopen(request)

output = response.read()
f = open('test.html', 'w')
f.write(output)