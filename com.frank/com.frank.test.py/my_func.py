
# coding=utf-8

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('数据类型错误，无法取绝对值')
    if x >= 0:
        return x
    else:
        return -x
