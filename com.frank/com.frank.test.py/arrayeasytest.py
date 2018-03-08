# !/usr/bin/env python
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
    n = 0
    for i in range(1, len(numbers)):
        # 从第0个开始比
        if (numbers[n] != numbers[i]):
            n = n + 1
            # 从第一个开始记
            numbers[n] = numbers[i]
    return n + 1


def remove_element(nums, target):
    index = 0
    n = len(nums)
    for i in range(n):
        if (nums[i] != target):
            nums[index] = nums[i]
            index = index + 1
    return index


def move_zero(numbers):
    index = 0
    l = len(numbers)
    for i in range(l):
        if (numbers[i] != 0):
            numbers[index] = numbers[i]
            index = index + 1
    for i in range(index, l):
        numbers[i] = 0


#
#  Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#
# Example 1
#
# Input: [3,0,1]
# Output: 2
#
# Example 2
#
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8

def find_missing_num(numbers):
    s = set(numbers)
    # 总数是 len(numbers) 加1 ，没有加一，缺失的是最大值的时候，程序会有问题
    for i in range(len(numbers) + 1):
        if not i in s:
            return i


def contains_duplicate(numbers):
    map = {}
    for i in range(len(numbers)):
        if numbers[i] in map:
            return True
        else:
            map[numbers[i]] = i
    return False


num = [1, 4, 11, 15, 17]
target = 26
print("twoSum=", twoSum(num, target))

num = [1, 1, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7]
print("remove_duplicate=", remove_duplicate(num))
print("remove_duplicate number =", num)

num = [1, 1, 1, 2, 3, 1, 3, 4, 4, 5, 6, 7]
print("remove_element=", remove_element(num, 3))
print("move_zero number =", num)

num = [1, 8, 2, 3, 4, 5, 6, 7, 10, 9, 0]
print("find_missing_num=", find_missing_num(num))

num = [0, 8, 2, 0, 4, 5, 6, 7, 10, 9, 0]
move_zero(num)
print("move_zero=", num)

num = [0, 8, 2, 4, 6,5, 6, 7, 10, 9]
print("contains_duplicate=", contains_duplicate(num))
