# -*- coding: utf-8 -*-
import os
# 切片  正数第一个元素索引是0，倒数第一个元素的索引是-1
L = ['lili', 'lucy', 'lilei', 'meimei']
print(L[0:3])
print(L[-1:])
print(L[-2:-1])

L = list(range(0, 99))
print(L[:10])
print(L[-10:])
print(L[10:20])
print(L[0:10:2])
print(L[::5])

t = tuple(range(10))
print(t[0:3])

s = 'abcdefg'
print(s[0:3])

# 迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for value in d.values():
    print(value)
for k, v in d.items():
    print(k, v)

for ch in 'ABC':
    print(ch)

for x,y in [(1, 2), (3, 5), (4, 7)]:
    print(x, y)

# 获取列表的最大值和最小值
def findMinAndMax(L):
    if L == []:
        return (None, None)
    min = max = L[0]
    for v in L[1:]:
        if v < min:
            min = v
        if v > max:
            max = v
    return (min, max)

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

# 列表生成式
L = [x * x for x in range(1, 11) if x % 2 == 0]
print(L)

print([d for d in os.listdir('.')])

L = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L if isinstance(s, str)])

# 生成器 generator,一边循环一遍计算的机制
g = (x * x for x in range(10))
print(g)
print(next(g))
for n in g:
    print(n)

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    print('step 3')
    yield 3
o = odd()
next(o)
next(o)
next(o)
# next(o)


def triangles(n):
    L = []
    i = 1
    while i <= n:
        L1 = []
        j = 1
        while j <= i:
            print(j, i)
            if j == 1 | j == i:
                L1.append(1)
            else :
                # pass
                L1.append(L[j]+L[j-1])
            j = j + 1
        L = L1
        yield L
        i = i + 1
    return 'done'
t = triangles(4)
next(t)
next(t)
# for l in t:
#     # pass
#     print(l)

