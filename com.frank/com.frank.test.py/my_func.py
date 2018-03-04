# coding=utf-8

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('数据类型错误，无法取绝对值')
    if x >= 0:
        return x
    else:
        return -x


## 多个返回值
## 其实也是一个返回值，返回的是个tuple,不可变的list
def my_fx(x, y, step):
    x2 = x + step
    y2 = y + step
    return x2, y2, x2 + x


## 默认参数 定义一个函数求 X² ，f = X*X ,求X的三次方f= X*X*X ,。。。一直求到X的一百次方，你定义99个函数去？
## 默认取平方
## 定义有默认值得参数时，必传项必须写前边，明确传参。都是非必填项，变化大的放前边，也是为了方便调用者理解，明确传参
## ！！！默认参数必须指向不变对象！
def power(x, n=2):
    t = 1
    while (n > 0):
        n = n - 1
        t = t * x
    return t


## 如果有多个默认参数，需要对后边的默认参数传值，则需要制定参数名
## 例如 enter_info('张三', city='shanghai')
def enter_info(name, age=18, city='beijing'):
    print("name=", name)
    print("age=", age)
    print("city=", city)
