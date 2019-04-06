# -*- coding: utf-8 -*-
"""
   File Name：     40 数组中只出现一次的数字
   Description :
   Author :       simon
   date：          19-3-3
"""

# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if array == None or len(array) <= 0:
            return []
        resultExclusiveOr = 0 # 定义为ab异或的结果 因为不相同 必然不是1
        for num in array:
            resultExclusiveOr ^= num

        indexOf1 = self.FindFirstBitIs1(resultExclusiveOr)
        num1, num2 = 0, 0
        for num in array:
            if self.IsBit1(num, indexOf1): # 对于数据进行分组 将两个出现一次的数字转换成一个出现次数为1的问题
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]

    # 最右边为1的那一位
    def FindFirstBitIs1(self, num):
        indexBit = 0
        while num & 1 == 0 and indexBit <= 32:
            indexBit += 1
            num = num >> 1
        return indexBit

    # 某一位是不是1
    def IsBit1(self, num, indexBit):
        num = num >> indexBit
        return num & 1


# -*- coding:utf-8 -*-
class mySolution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if not array:
            return []

        temp = 0
        for num in array:
            temp ^= num

        right = self.rightEstIndex1(temp)
        num1, num2 = 0, 0
        for num in array:
            if self.isBit1(num, right):
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]

    def rightEstIndex1(self, num):
        indexBit = 0
        while not num & 1:
            indexBit += 1
            num = num >> 1
        return indexBit

    def isBit1(self, num, indexBit):
        num = num >> indexBit
        return num & 1

if __name__ == '__main__':

    aList = [2, 4, 3, 6, 3, 2, 5, 5]
    s = mySolution()
    print(s.FindNumsAppearOnce(aList))