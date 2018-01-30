#coding=utf-8
#函数
import math
L = []
x = 1
while x <= 100:
    L.append(x * x)
    x = x + 1
#print L
print sum(L)

#参数类型？
def my_abs(x):
    if x > 0:
        return x
    else :
        return -x
print my_abs('-a')
#print abs('a')

# ax^2 + bx + c = 0 [-b±√(b^2-4ac)]/2a
def quadratic_equation(a, b, c):
    tmp = math.sqrt(b * b - 4 * a * c)
    x1 = (-b + tmp) / (2 * a)
    x2 = (-b - tmp) / (2 * a)
    return x1, x2
print quadratic_equation(1, 1, 0)

#n!
def fact(n):
    if n == 1 :
        return 1
    else :
        return n * fact(n - 1)
print fact(5)

#默认参数
print int('123')
print int('123', 8)

def power(x, n = 2):
    s = 1
    while n > 0:
        s = s * x
        n = n - 1
    return s
print power(5, 3)

#可变参数
def fn(*args):
    print args
fn(1, 2, 3)

def average(*args):
    s = 0
    for v in args:
        s = s + v
    return s / len(args)
print average(1, 2, 3, 4, 5)
