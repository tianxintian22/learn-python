#coding=utf-8
L = ['a', 'b', 'c', 'd']
for v in L:
    print v,
for i, v in enumerate(L):
    print i, v

print '========='
T = (1, 2, 3, 4, 5)
for v in T:
    print v,
for i, v in enumerate(T):
    print i, v
print '========='

D = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4}
for v in D:
    print v,
for v in D.values():
    print v
for v in D.itervalues():
    print v
for k, v in D.items():
    print k , ':' , v
for k, v in D.iteritems():
    print k, v
print '========='

S = set(['1', '2', '3', '4'])
for v in S:
    print v,
for i, v in enumerate(S):
    print i, v

#生成列表
print [x + x for x in range(1, 11)]
print [x * (x + 1) for x in range(1, 100, 2)]

tds = ['<tr><td>%s</td><td>%s</td></tr>' % (name, score) for name, score in D.iteritems()]
print '<table>\n<th>Name</th><th>Score</th>'
print '\n'.join(tds)
print '</table>'

print [x * x for x in range(1, 11) if x % 2 == 0]

def toUppers(L):
    return [v.upper() for v in L if isinstance(v, str)]
print toUppers(['Hello', 'world', 101])

print [x * 100 + y * 10 + z for x in range(1, 10) for y in range(0, 10) for z in range(0, 10) if x == z]