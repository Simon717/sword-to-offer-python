# -*- coding: utf-8 -*-
"""
   File Name：     数字
   Description :
   Author :       simon
   date：          19-4-13
"""


class Solution:
    def queshi(self, nums):
        nums += [float('inf')]
        for n in nums[:-1]:
            nums[n] = - abs(nums[n])
        for i, n in enumerate(nums):
            if n > 0:
                return i

        # return nums.index(0)

    def que(self, nums):
        res = [-1] * (len(nums)+1)
        for n in nums:
            res[n] = 1
        for i , n in enumerate(res):
            if n == -1:
                return i


if __name__ == '__main__':
    nums = input().strip().split(',')
    nums = list(map(int, nums))
    # print(Solution().queshi([1,0,3]))
    print(Solution().queshi(nums))
