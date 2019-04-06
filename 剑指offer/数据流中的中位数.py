# -*- coding: utf-8 -*-
"""
   File Name：     数据流中的中位数
   Description :
   Author :       simon
   date：          19-3-21
"""

"""
插入排序
"""
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.data = []

    def Insert(self, num):
        # write code here
        index = len(self.data) - 1
        self.data.append(num)
        while index>=0 and num < self.data[index]: # 将加入的数字插入到合理的位置
            self.data[index+1] = self.data[index]
            index -= 1
        self.data[index+1] = num

    def Insert_(self, num): # 先考虑用使用库函数
        self.data.append(num)
        self.data.sort()

    def GetMedian(self, m):
        # write code here
        N = len(self.data)
        if not N: return 0
        a, b = N // 2, N % 2
        if b:
            return self.data[a]
        return (self.data[a] + self.data[a - 1]) / 2. # 保证是一个浮点数