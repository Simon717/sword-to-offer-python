# -*- coding: utf-8 -*-
"""
   File Name：     41 和为s的两个数字
   Description :
   Author :       simon
   date：          19-3-4
"""

# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array:
            return []

        left, right = 0, len(array)-1
        while left < right:
            sum_ = array[left] + array[right]
            if sum_ == tsum:
                return [array[left], array[right]]
            while array[left] + array[right] > tsum:
                right -= 1
            while array[left] + array[right] < tsum:
                left += 1
        return []

if __name__ == '__main__':
    test = [1,2,4,7,11,15]
    solu = Solution()
    print(solu.FindNumbersWithSum(test, 5))