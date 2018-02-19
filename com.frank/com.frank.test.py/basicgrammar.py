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
# 各国有各国的编码标准（比如美国ASCII，中国GB2312，日本Shift_JIS，韩国Euc-kr），难免会出现冲突的问题。
# 解决方案是Unicode。 Unicode把所有语言都统一到一套编码里，这样就不会再有乱码问题了。
# Unicode 编码，最常用的是用两个字节表示一个字符（如果要用到非常偏僻的字符，就需要4个字节）
# 如果你存的全是英文字符，用Unicode编码比ASCII(一个字节存一个字符)编码需要多一倍的存储空间，在存储和传输上就十分不划算。
# 解决方案是utf8。UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节
# 常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。如果你要传输的文本包含大量英文字符，用UTF-8编码就能节省空间。

# 在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。
# 用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件
# 浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器
encode = '学习'.encode('utf8')
print("encode=", encode)

decode = encode.decode('utf8')
print("decode=", decode)

print("encode=", 'A'.encode('ascii'))
print("encode=", 'A'.encode('utf8'))
print("encode=", 'A'.encode('Euc-kr'))
print("encode=", 'A'.encode('Shift_JIS'))

mylist = ['张三', 'Bob', 'Sofia']
print("list长度=", len(mylist))
print("list[0]=%s,最后一个元素list[-1]=%s，倒数第二个元素list[-2]=%s" % (mylist[0], mylist[-1], mylist[-2]))
