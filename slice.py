#coding=utf-8
L = ['a', 'b', 'c', 'd']
print L[0:3:3]
print L[-3:-1]

L = range(1, 101)
print L[90: 101]
print L[-46::5]

def upperFirstChar(s):
    first = s[0].upper()
    return first + s[1:]

print upperFirstChar('hello')
