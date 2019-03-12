# -*- coding: utf-8 -*-
"""
   File Name：     238. Product of Array Except Self
   Description :
   Author :       simon
   date：          19-3-12
"""

"""
2 3 4 5 6
---------
3 2 2 2 2
4 4 3 3 3
5 5 5 4 4
6 6 6 6 5
"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        res = [1] * N

        p = 1
        for i in range(N):
            res[i] *= p
            p *= nums[i]

        p = 1
        for i in range(N - 1, -1, -1):
            res[i] *= p
            p *= nums[i]

        return res

test = [1,2,3]
solu = Solution()
print(solu.productExceptSelf(test))