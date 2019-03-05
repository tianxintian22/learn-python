#coding=utf-8

print 'hello world'

print 45678+0x12fd2
print 'Learn Python in imooc'
print 100 < 99
print 0xff == 255

print 'hello', 'i am here'

# 这是一行注释
print '1 + 2 =', 1 + 2

x = 10
x = x + 2
print x

a = 'ABC'
b = a
a = 'XYZ'
print b

# 等差数列求和
x1 = 1
d = 3
n = 100
x100 = x1 + (n - 1) * d
print x100
s100 = n * x1 + n * (n - 1) * d / 2
print s100

print 'Python was started in 1989 by "Guido".\nPython is free and easy to learn.'
print 'Bob said \"I\'m OK\".'
print r'''Bob said "I'm OK".'''


print r'\(~_~)/ \(~_~)/'
print r'''"To be, or not to be": that is the question.
Whether it's nobler in the mind to suffer.'''

print u'中文'

print u'''第一行
第二行'''

print ur'''Python的Unicode字符串支持"中文",
"日文",
"韩文"等多种语言'''

print 1.0 + 2.0  # => 3.0
print 1 + 2.0    # => 3.0
print 11 / 4     # => 2 
print 11.0 / 4   # => 2.75
print 11 % 4

print 2.5 + 10.0 / 4

a = True
print a and 'a=T' or 'a=F'

A = 'python'
print 'hello,', A or 'world'
B = ''
print 'hello,', B or 'world'

#list
L = [95.5, 85, 59]
print L[1]
print L[-1]

C = ['Adam', 'Lisa', 'Bart']
C.append('Paul')
print C
print '================'
C.insert(-1, 'Tom')
print C
print C.pop()
print C
print C.pop(1)
print C
C[-1] = 'Paul'
print C

#tuple
D = ('a', 'b', 'c')
print D[1]
# D[0] = 'A'

t = (1,)
print t
t1 = ('Admin',)
print t1
t2 = ('a', 'b', ['A', 'B'])
T = t2[2]
T[1] = 'Y'
print t2