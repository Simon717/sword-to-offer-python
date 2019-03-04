# -*- coding: utf-8 -*-
"""
   File Name：     41 和为S的连续正数序列
   Description :
   Author :       simon
   date：          19-3-4
"""
# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum <= 0:
            return
        small, big = 1, 2
        curSum = 3
        res = []

        while small <= (tsum-1)/2:
            if curSum == tsum:
                res.append([x for x in range(small, big+1)])
                big += 1
                curSum += big
            while curSum < tsum:
                big += 1
                curSum += big
            while curSum > tsum:
                small += 1
                curSum -= small - 1

        return res

if __name__ == '__main__':
    test = 9
    solu = Solution()
    print(solu.FindContinuousSequence(test))