# -*- coding: utf-8 -*-
"""
   File Name：     数组中重复的数字
   Description :
   Author :       simon
   date：          19-3-16
"""
"""
利用上 长度为n的数组里的所有数字都在0到n-1的范围内 这个条件
尝试对数组进行重排列
发现要交换的两个数字相同的时候 说明找到了结果
"""
# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        for i in range(len(numbers)):
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                index = numbers[i]
                numbers[i], numbers[index] = numbers[index], numbers[i]
        return False

# -*- coding:utf-8 -*-
class Solution_hash:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        dic = {}
        for num in numbers:
            if num not in dic:
                dic[num] = 0
            dic[num] += 1
            if dic[num] == 2:
                duplication[0] = num
                return True
        return False