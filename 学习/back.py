# -*- coding: utf-8 -*-
"""
   File Name：     back
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
        return 0


if __name__ == '__main__':
    nums = input().strip().split(',')
    nums = list(map(int, nums))
    # print(Solution().queshi([0,2]))
    print(Solution().queshi(nums))