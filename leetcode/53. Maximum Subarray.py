# -*- coding: utf-8 -*-
"""
   File Name：     53. Maximum Subarray
   Description :
   Author :       simon
   date：          19-3-15
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if max(nums) < 0:
            return max(nums)

        maxsum = S = 0
        for i in range(len(nums)):
            S += nums[i]
            maxsum = max(maxsum, S)
            if S < 0:
                S = 0

        return maxsum

"""
好好看看
动态规划
"""
class Solution_fast(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        curSum = 0
        for index, val in enumerate(nums[:]):
            curSum = val + curSum
            if curSum > max_sum:
                max_sum = curSum
            if curSum < 0:
                curSum = 0
        return max_sum

class Solution0:
    # @param A, a list of integers
    # @return an integer
    # 6:57
    def maxSubArray(self, A):
        if not A:
            return 0

        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum