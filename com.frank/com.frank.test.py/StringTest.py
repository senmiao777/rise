import re

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


print('读取txt result=', read_txt('G:\pycharm\pytest.txt'));
