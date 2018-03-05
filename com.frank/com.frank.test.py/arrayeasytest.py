#!/usr/bin/env python
# -*- coding: utf-8 -*-

print('Hello World')


def twoSum(numbers, target):
    map = {}
    ##result = []
    for i in range(len(numbers)):
        b = target - numbers[i]
        if (str(b) in map):
            # result.append(map[str(b)])
            # result.append(i)
            # return result
            return [map[str(b)], i]
        else:
            map[str(numbers[i])] = i


def remove_duplicate(numbers):
    n = 0;
    for i in range(1, len(numbers)):
        # 从第0个开始比
        if (numbers[n] != numbers[i]):
            n = n + 1
            # 从第一个开始记
            numbers[n] = numbers[i]
    return n + 1


num = [1, 4, 11, 15, 17]
target = 26
print("twoSum=", twoSum(num, target))

num = [1, 1, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7]
print("remove_duplicate=", remove_duplicate(num))
print("remove_duplicate number =", num)
