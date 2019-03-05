# -*- coding: utf-8 -*-

# list, 是可变对象，对list进行操作，list内部的内容是会变化的
classmates = ['xiaoli', 'xiaoxiu', 'xiaohua']
#classmates.sort() # 排序后，classmates值的顺序发生变化

print(classmates)
print(len(classmates))
print(classmates[-1])
classmates.append('追加的一员')
print(classmates)
classmates.insert(1, '插入的一员')
print(classmates)
classmates.pop(2) # 参数为空，默认删除最后一个
print(classmates)

# touple，与list相似，但是一旦初始化后就不能改变
teachers = ('T01', 'T02', 'T03')
print(teachers)
print(teachers[1])
t = (1,) # 只有一个元素的touple定义时必须加逗号，来消除歧义
print(t)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[1][1])