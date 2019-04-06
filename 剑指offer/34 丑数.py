# -*- coding: utf-8 -*-
"""
   File Name：     34 丑数
   Description :
   Author :       simon
   date：          19-2-25
"""


class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0:
            return 0
        ugly = [1] * index
        T2, T3, T5 = 0, 0, 0
        i = 1
        while i < index:
            while ugly[T2] * 2 <= ugly[i-1]:
                T2 += 1
            while ugly[T3] * 3 <= ugly[i-1]:
                T3 += 1
            while ugly[T5] * 5 <= ugly[i-1]:
                T5 += 1
            ugly[i] = min(ugly[T2] * 2, ugly[T3] * 3 , ugly[T5] * 5)
            i += 1
        return ugly[-1]

if __name__ == '__main__':
    test = 1
    solu = Solution()
    print(solu.GetUglyNumber_Solution(test))