#!/usr/bin/env python
import re
import os
from distutils.log import warn as printf
from random import randrange, choice
from string import ascii_lowercase as lc
from sys import maxsize
from time import ctime

str = "frank.just for test test2 test3"
replace = str.replace("test", "hello")
print(replace)

# str ="frank.just for test test2 test3"
replace = str.replace("test", "hello", 2)
print(replace)

split = str.split(' ')
print("split result =", split)

split = str.split(' ', 2)
print("split 2 result =", split)

# 按正则表达式替换
sub = re.sub('[r]', '1234', str)
print(sub)


def read_txt(path):
    with open(path, 'r', encoding='utf8') as f:
        lines = f.readlines()
    return lines


def println():
    with os.popen('who', 'r') as f:
        for eachline in f:
            printf(re.split(r'\s\s+|\t'), eachline.strip())


#
# def generate(tlds):
#     for i in range(randrange(5, 11)):
#         dtint = randrange(maxsize)
#         dtstr = ctime(dtint)
#         llen = randrange(4, 8)
#         login = ''.join(choice(lc) for i in range(llen))
#         dlen = randrange(llen, 13)
#         dom = ''.join(choice(lc) for j in range(dlen))
#         print
#         '%s::%s@%s.%s::%d-%d-%d' % (dtstr, login, dom, choice(tlds), dtint, llen, dlen)


t = ('com', 'edu', 'net', 'org', 'gov')
print("生成数据=", generate(t))
print('读取txt result =', read_txt('G:\pycharm\pytest.txt'));

print(println())


def generate2():
    for i in range(randrange(5, 15)):
        print("number=",i)
print("suijishu =",generate2())
