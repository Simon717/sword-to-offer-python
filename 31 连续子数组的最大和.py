# -*- coding: utf-8 -*-
"""
   File Name：     31 连续子数组的最大和
   Description :
   Author :       simon
   date：          19-2-22
"""

# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return 0

        curSum = 0
        maxSum = array[0]
        for i, item in enumerate(array):
            if curSum < 0:
                curSum = item
            else:
                curSum += item

            if curSum > maxSum:
                maxSum = curSum
        return maxSum

    def FindGreatestSumOfSubArray0(self, array):
        if not array:
            return 0

        maxSumList = [array[0]]
        for i in range(1, len(array)):
            if maxSumList[i-1] < 0:
                maxSumList.append(array[i])
            else:
                maxSumList.append(maxSumList[i-1]+array[i])
        return max(maxSumList)


if __name__ == '__main__':
    test = [1, -3, 2, 4, -9]
    solu = Solution()
    print(solu.FindGreatestSumOfSubArray0(test))