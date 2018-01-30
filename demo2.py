#coding=utf-8
#dict
d = {
    'a' : 95,
    'b' : 85,
    'c' : 59
}
print len(d)
print d['a']
print d.get('a')
d['d'] = 75
d['a'] = 10
print d

if 'b' in d:
    print d['b']

for index in d:
    print index,':',d[index]

for letter in 'Python':     # 第一个实例
    print u'当前字母 :', letter

d = {
    '123': [1, 2, 3],  # key 是 str，value是list
    123: '123',  # key 是 int，value 是 str
    ('a', 'b'): True  # key 是 tuple，并且tuple的每个元素都是不可变对象，value是 boolean
}
print d

#set
s = set(['a', 'b', 'c', 'c'])
print s
print len(s)
print 'a' in s
print 'A' in s
s.add('d')
s.remove('d')
print s

weekdays = set(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
if 'MON' in weekdays:
    print 'input ok'
else :
    print 'input error'

for name in weekdays:
    print name

s = set([('Admin', 95), ('Lisa', 85), ('Bart', 59)])
for v in s:
    print v[0], ':', v[1]

s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for v in L :
    print v
    if v in s:
        s.remove(v)
    else :
        s.add(v)
print s