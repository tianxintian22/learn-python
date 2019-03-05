# -*- coding:utf-8 -*-

students = ['xiaoli', 'xiaowang', 'xiaohua']
for student in students:
    print(student)

sum = 0
for i in list(range(101)):
    sum += i
    if i > 10:
        break
print(sum)

for i in range(101):
    if i % 2 == 0:
        continue
    print(i)

