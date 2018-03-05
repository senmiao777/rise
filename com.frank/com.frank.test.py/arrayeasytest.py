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
            return [map[str(b)],i]
        else:
            map[str(numbers[i])] = i


num = [1, 4, 11, 15, 17]
target = 26
print("twoSum=", twoSum(num, target))
