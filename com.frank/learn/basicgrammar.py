# -*- coding: utf-8 -*-
from my_func import my_abs, my_fx, power, enter_info

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

mylist = ['张三', 'Bob', 'Frank', 'Sofia']
print("list长度=", len(mylist))
print("list[0]=%s,最后一个元素list[-1]=%s，倒数第二个元素list[-2]=%s" % (mylist[0], mylist[-1], mylist[-2]))
mylist.append('App')
print("after append list=", mylist)
# list里的数据类型可以不一致
mylist.insert(1, ['one', True])
print("after insert list=", mylist)
# 删除
mylist.pop(3)
print('atfer pop list=', mylist)

# tuple 可以理解为一个不可变的list，不可变，指的是引用不可变。
mytuple = (1, '2', mylist)
print('mytuple=', mytuple)
mylist.append('tuple\'s member list change')
print('mytuple=', mytuple)

if '0':
    print("True")
else:
    print("False")

# age = input('请输入年龄: ')
# # 直接使用age会报错，因为input接收到的是字符串
# age = int(age)
age = 18
if age >= 18:
    print('aduit')
elif age >= 6:
    print('teenager')
else:
    print('kid')

for i in mylist:
    print(i)

# range函数生成一个序列，下标从0到n-1
r = range(5)
print("range =", r)
for i in r:
    print(i)

s = 0
for i in range(101):
    s = s + i
print("1+2+3+...+99+100 =", s)

i = 0
s = 0
while i <= 100:
    s = s + i
    i = i + 1
print("result= ", s)

for i in range(10):
    if i % 3 == 0:
        continue
    if i % 5 == 0:
        break
    print("number= ", i)

# dict dictionary 就是java里的map
obj = {'frank': True, 'sofia': 'woman', age: 78}
# 't' in obj 判断是否存在
print("obj['frank']=%s ,obj['sofia']=%s ,obj[age]=%s,exist=%s" % (obj['frank'], obj['sofia'], obj[age], 't' in obj))

# 创建后赋值
obj['add'] = 'addElement'
obj['add2'] = 'addElement2'
# get 第二个参数，给默认值，map中不存在不会保存，返回默认值
print("obj['add']= %s,obj['add3']=%s" % (obj.get('add'), obj.get('add3', -199)))
# obj.pop('add2')
print("obj=", obj)

s1 = set([1, 2, 3, 4, 4, 4, 4])
s2 = set([3, 4, 5, 6, 7])
s3 = set([3, 4, 5, 6, 7, 8, 9])
s4 = s1 & s2
s5 = s1 | s2
print("s1 & s2 =", s4)
print("s1 | s2 =", s5)
print("s2 -s1 =", s2 - s1)
print("s1 - s2 =", s1 - s2)
print("s1 | s2 | s3 =", (s1 | s2 | s3))
print("s1 & s2 & s3 =", (s1 & s2 & s3))

contains__ = s1.__contains__(11)
print("contains=", contains__)

a = 100
print("abs()=", abs(a))
string = "190"
int1 = int(string)
print("数据类型转换 String 2 int", int1)
string = "190.98"
f = float(string)
print("数据类型转换 String 2 float", f)

print("int 2 String =", str(int1))

print("1- String 2 boolean =", bool(string))
print("2- String 2 boolean =", bool(''))
print("int 2 boolean =", bool(int1))

# print("my_abs=", my_abs("gt"))
print("my_abs=", my_abs(1))

print("my_fx", my_fx(1, 2, 3))
print("power=", power(2, 4))

print("enter_info:", enter_info('张三', city='shanghai'))

str = "地区：江西赣州，性别：男，职业：教书匠，学历：本科，年龄：24，对对方的大致要求：最好女的。"
split = str.split("，")
print("111 strip=", split)
print("111 strip length =", len(split))

split = str.split("#")
print("222 strip=", split)
print("222 strip length =", len(split))

str2 = "地区：江西赣州"
find = str2.find("2")
print("index find=", find)

# 注意 index 方法，如果找不到，会报错；find 方法，找不到元素，返回 -1
index = str2.index("：")
print("index index=", index)
print("substring=", str2)
str3 = "地区江西赣州"
find = str3.find("地区")
print("index find=", find)

s = "地区江西赣州"
print("substring=", s[2:len(s)])


def get_diff():
    bigSister = open("D:/t1.txt", mode="r", encoding="utf-8")
    s = set()
    try:
        ## 去掉行尾的 \n
        all_the_text = bigSister.read().splitlines()
        print("all_the_text", all_the_text)
        readlines = bigSister.readlines(20)
        print("readlines()=", readlines)
        s = set(all_the_text)
        print("set()=", s)
    finally:
        bigSister.close()

    my = open("D:/t2.txt", mode="r", encoding="utf-8")
    s1 = set()
    try:
        ## 去掉行尾的 \n
        all_the_text = my.read().splitlines()
        print("all_the_text", all_the_text)
        readlines = my.readlines(20)
        print("readlines()=", readlines)
        s1 = set(all_the_text)
        print("set()=", s1)
    finally:
        bigSister.close()
    return s - s1


##print(get_diff())
# a= 10
# b= 100
# and_b = a and b
# print("a and b =", and_b)
# print("a and b =", type(and_b))
a = 10
b = 100
b_a = b / a
print("b_a =", b_a)
print("b_a  type=", type(b_a))

print("100 / 10 =", 100 / 10)

from enum import Enum, unique


# unique用于校验枚举值的唯一性
@unique
class Roman(Enum):
    M = ('M', 1000, 'M对应值为1000')
    D = ('D', 500, 'D对应值为500')
    C = ('C', 100, 'C对应值为100。C can be placed before D (500) and M (1000) to make 400 and 900')
    L = ('L', 50, 'L对应值为50')
    X = ('X', 10, 'X对应值为10。X can be placed before L (50) and C (100) to make 40 and 90')
    V = ('V', 5, 'V对应值为5')
    I = ('I', 1, 'I对应值为1。I can be placed before V (5) and X (10) to make 4 and 9')
    IV = ('IV', 4, 'IV对应值为4')
    IX = ('IX', 9, 'IX对应值为9')
    XL = ('XL', 40, 'XL对应值为40')
    XC = ('XC', 90, 'XC对应值为90')
    CD = ('CD', 400, 'CD对应值为400')
    CM = ('CM', 900, 'CM对应值为900')

    def __init__(self, key, number, desc):
        self.key = key
        self.number = number
        self.desc = desc

    @property
    def _value(self):
        return self.number

    @property
    def _key(self):
        return self.key

    @property
    def _desc(self):
        return self.desc


print("11111111111111111111111Roman=", Roman)
print("11111111111111111111111Roman.CM.key=", Roman.CM._key)
print("11111111111111111111111Roman.CM.number=", Roman.CM._value)
print("11111111111111111111111Roman.CM._desc=", Roman.CM._desc)


class Planet(Enum):
    MERCURY = (3.303e+23, 2.4397e6)
    VENUS = (4.869e+24, 6.0518e6)
    EARTH = (5.976e+24, 6.37814e6)
    MARS = (6.421e+23, 3.3972e6)
    JUPITER = (1.9e+27, 7.1492e7)
    SATURN = (5.688e+26, 6.0268e7)
    URANUS = (8.686e+25, 2.5559e7)
    NEPTUNE = (1.024e+26, 2.4746e7)

    def __init__(self, mass, radius):
        self.mass = mass  # in kilograms
        self.radius = radius  # in meters

    @property
    def surface_gravity(self):
        # universal gravitational constant  (m3 kg-1 s-2)
        G = 6.67300E-11
        return G * self.mass / (self.radius * self.radius)


print("Planet.CM.desc=", Planet.EARTH.value)
print("Planet.CM.desc=", Planet.EARTH.surface_gravity)
