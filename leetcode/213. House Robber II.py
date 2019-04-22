# -*- coding: utf-8 -*-
"""
   File Name：     213. House Robber II
   Description :
   Author :       simon
   date：          19-4-12
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def helper(nums):
            prev, cur = 0, 0  # dp[i-2] dp[i-1]
            for num in nums:
                prev, cur = cur, max(cur, prev + num)
            return cur
        return max(helper(nums[:-1]), helper(nums[1:]))

class Solution_(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev, cur = 0, 0  # dp[i-2] dp[i-1]
        for num in nums:
            prev, cur = cur, max(cur, prev + num)
        return cur