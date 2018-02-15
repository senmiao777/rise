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
