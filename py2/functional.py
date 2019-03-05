#coding=utf-8
import math
import time
def add(x, y, f):
    return f(x) + f(y)
print add(4, 4, math.sqrt)

L = ['adam', 'LISA', 'barT']
def f(x):
    t1 = x[0].upper()
    t2 = x[1:].lower()
    return t1 + t2
print map(f, L)


def prod(x, y):
    return x * y
print reduce(prod, [2, 4, 5, 7])

def is_sqrt(x):
    r = math.sqrt(x)
    return int(r) == r
print filter(is_sqrt, range(1, 101))

print sorted([3,1,2,5,4])

def reversed_cmp(x, y):
    x = x.lower()
    y = y.lower()
    if x > y:
        return 1
    elif x < y:
        return -1
    else :
        return 0
print sorted(['bob', 'about', 'Zoo', 'Credit']) 
print sorted(['bob', 'about', 'Zoo', 'Credit'], reversed_cmp)

# 闭包
def calc_prod(lst):
    def calc():
        return reduce(prod, lst)
    return calc
f = calc_prod([1, 2, 3, 4])
print f()

def count():
    fs = []
    for i in range(1, 4):
        def f(num):
            def t():
                return num * num
            return t
        fs.append(f(i))
    return fs

f1, f2, f3 = count()
print f1()

# 匿名函数
is_not_empty = lambda s: s and len(s.strip()) > 0
filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])

# 装饰器
def new_fn(f):
    def fn(x):
        print 'call ' + f.__name__ + '()...'
        return f(x)
    return fn
@new_fn
def f1(x):
    return x * 2
# f1 = new_fn(f1)
print f1(1)

# 不带参数的decorator
def log(f):
    def fn(*args, **kw):
        print 'call ' + f.__name__ + '()...'
        return f(*args, **kw)
    return fn
@log
def f2(x):
    return x
print f2(2)
@log
def add(x, y):
    return x + y
print add(1, 2)

def performance(f):
    def fn(*args, **kw):
        print 'call ' + f.__name__ + '() at ', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return f(*args, **kw)
    return fn
@performance
def f3(x):
    return x * x
print f3(3)

# 带参数的decorator
def log1(prefix):
    def log_decorator(f):
        def wrapper(*args, **kw):
            print '[%s] %s()...' % (prefix, f.__name__)
            return f(*args, **kw)
        return wrapper
    return log_decorator

@log1('DEBUG')
def f4(x):
    return 2 * x
print f4(5)