# -*- coding: utf-8 -*-

#dictionary
d = {'xiaohua': 54, 'xiaoli': 90, 'xiaoliu': 87}

print(d['xiaohua'])
d['xiaohua'] = 100
print(d.get('xiaohua'))

print('xiaol' in d)

print(d.get('xiaol'))
print(d.get('xiaol', 66))
print(d)

d.pop('xiaohua')
print(d)

# set
s = {1, 2, 2 , 3}
s1 = {1, 4, 6, 7}
print(s)
print(set('abcdef'))
s.add(4)
print(s)
s.remove(2)
print(s)
print(len(s))

print(set([1, 2, 3]))
