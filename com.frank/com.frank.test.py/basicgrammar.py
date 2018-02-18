# -*- coding: utf-8 -*-
print('Hello World')
# name = input("please input your name: ")
# print("hello: ", name)

s = 'I\'m \"ok\"!'
print(s)

n = 1.25e3
print(n)
n = -1.25e3
print(n)

print('a\nb\nc')

print(3 > 2)
print(3 < 2)
print(True)

print('and or not:', True and False)

age = 18
if age >= 18:
    print('aduit')
else:
    print('teenager')

# python 中有两种除法， / 得到的是浮点类型的结果；// 得到的是整型的结果
print('10/3= ', 10 / 3)
print('9/3= ', 9 / 3)
print('10//3= ', 10 // 3)
print('9//3= ', 9 // 3)
# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符

print('print(ord(A))=%d,print(ord(B))=%d' % (ord('A'), ord('B')))
print('print(chr(66))=%s,print(chr(100))=%s' % (chr(66), chr(100)))

s = '\u4e2d\u6587'
print("十六进制编码 s = ", s)

# 字符串和byte转换
# Python对bytes类型的数据用带b前缀的单引号或双引号表示
encode = '学习'.encode('utf8')
print("encode=", encode)

decode = encode.decode('utf8')
print("decode=", decode)
