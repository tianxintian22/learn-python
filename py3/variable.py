#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# bool (True/False)，注意大小写，运算符：and ,or, not
print (True and False)

# 空值 none

a = '1243'
print (a)
a = 1234
print (a)
a = a + 1
print (a)

# 常量名习惯上用大写表示
# Python的整数没有大小限制
# Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）

print (10/3)
print (10//3) # 地板除，两个整数的除法结果仍然是整数
print (10%3)
print (10/2)

# 计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。
# ASCII编码是1个字节，Unicode编码是2个字节，UTF-8编码是根据不同数字大小编码成1-6个字节
print (ord('A'))
print (ord('中'))
print (chr(66))

# 'abc' 是字符串类型str，b'abc'是bytes类型，前者一个字符对应若干个字节，后者每个字符只占一个字节
# str 通过encode()可以编码为 bytes
# bytes 通过decode()可以解码为 str
print ('A'.encode('ascii'))
print ('中文'.encode('utf-8'))
print (b'A'.decode('ascii'))
print (b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# len() 计算str的字符数，bytes的字节数
print (len('abc'))
print (len(b'abc'))
print (len(b'\xe4\xb8\xad\xe6\x96\x87'))
print (len('中文'.encode('utf-8')))
print (len('中文'))

# %运算符就是用来格式化字符串的
print ('age:%s, gender:%s' % (23, '女'))