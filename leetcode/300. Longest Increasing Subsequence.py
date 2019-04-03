# -*- coding: utf-8 -*-
"""
   File Name：     300. Longest Increasing Subsequence
   Description :
   Author :       simon
   date：          19-4-1
"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        dp = [1] * len(nums) # end with here 的最长递增序列

        for i in range(1, len(nums)):
            dp[i] = 1 + max([dp[j] if nums[i]>nums[j] else 0 for j in range(i)])
        return max(dp)

"""
待消化
"""
import bisect
class Solution_(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0

        lis = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > lis[-1]:
                lis.append(nums[i]) # 拓展序列
            else:
                # 要用bisect_left，因为如果插入到右边就相当于多append了一个，而不再是replace了
                lis[bisect.bisect_left(lis, nums[i])] = nums[i] #　直接replace掉之前的数字

        return len(lis)


class Solution__(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def binarySearch(nums, l, r, target):
            while l <= r:
                mid = l + ((r - l) >> 1)
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        if not nums or len(nums) == 0:
            return 0

        tails = [0 for i in range(len(nums) + 1)]
        tails[0] = nums[0]
        # always points empty slot 空位
        length = 1
        for i in range(1, len(nums)):
            if (nums[i] < tails[0]):
                # new smallest value
                tails[0] = nums[i]
            elif (nums[i] > tails[length - 1]):
                # A[i] wants to extend
                # largest subsequence
                tails[length] = nums[i]
                length += 1
            else:
                # A[i] wants to be current
                # end candidate of an existing
                # subsequence. It will replace
                # ceil value in tailTable
                tails[binarySearch(tails, 0, length - 1, nums[i])] = nums[i]

        return length
if __name__ == '__main__':
    print(Solution().lengthOfLIS([1,3,6,7,9,4,10,5,6]))