# -*- coding: utf-8 -*-

height = 1.75
weight = 80.5

bmi = weight / (height * height)

if bmi < 18.5:
    res = '过轻'
elif 18.5 <= bmi < 25:
    res = '正常'
elif 25 <= bmi <28:
    res = '过重'
else:
    res = '肥胖'
print(res)