# -*- coding: utf-8 -*-

print(abs(-100))
# 函数名指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给函数起了个别名
a = abs
print(a(-1.2))

def my_abs(v):
    # 对参数类型做检查
    if not isinstance(v, (int, float)):
        raise TypeError('bad operand type')
    if v > 0:
        return v
    else:
        return -v
print(my_abs(0))
# print(my_abs('a'))

# 空函数,pass语句什么都不做，可以用来作占位符
def nop():
    pass

# 返回多个值
import math
def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
r = x, y = move(100, 100, 60, math.pi/6)
print(r)
print(x, y)

# 默认参数(默认参数必须指向不变对象)
def enroll(name, gender, age = 6, city = 'beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
enroll('lili', 'Male')
enroll('lucy', 'Male', city='NewYork')

# 可变参数（参数个数可变）
# calc()传入list或touple参数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    print(sum)
calc([1, 2, 3])
calc((1, 2, 3, 4))

def calc1(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    print(sum)
calc1(1, 2, 3)

# 在list或tuple前面加一个*号，把list或tuple的元素变成可变参数
nums = [1, 2, 3]
calc1(*nums)

# 关键词参数,允许传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('lili', 20)
person('bob', 28, city='beijing')

# 上面复杂的调用简化
extra = {'city': 'beijing', 'job':'Manager'}
person('jack', 30, **extra)

# 命名关键字参数,可以限制关键字参数的名字
# 只接收city和job作为关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)
person('jack', 24, **extra)

# 递归函数
def fact(n):
    if n == 1:
        return 1
    else :
        return n * fact(n -1)
print(fact(5))
# print(fact(1000))

# 尾递归
# def fact(n):
#     return fact_filter(n, 1)
# def fact_filter(num, product):
#     if num == 1:
#         return product
#     else :
#         return fact_filter(num - 1, num * product)
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
print(fact(5))
print(fact(1000))