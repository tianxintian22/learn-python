#coding=utf-8
#if else elif
age = 20
print 'your age is', age
if age >= 18:
    print 'adult'
elif age >= 6:
    print 'teenager'
else :
    print 'kid'

score = 5
if score >= 60:
    print 'passed'
else :
    print 'failed'

#for
L = ['a', 'b', 'c', 'd'];
for name in L:
    print name,

L1 = [75, 92, 59, 68]
s = 0
for num in L1:
    s = s + num
print s / len(L1)

#while
x = 1
s = 0
while x <= 100 :
    s = s + x
    x = x + 2
print s

#break
x1 = 1
s1 = 0
n = 1
while True:
    if n > 20:
        break
    n = n + 1
    s1 = s1 + x1
    x1 = 2 * x1
print s1

#continue
x2 = 0
s2 = 0
while True:
    x2 = x2 + 1
    if x2 > 100:
        break
    if x2 % 2 == 0:
        continue
    s2 = s2 + x2
print s2

# 多重循环
x = 1
while x < 10:
    y = 0
    while y < 10:
        if x < y:
            print x * 10 + y
        y = y + 1
    x = x + 1
