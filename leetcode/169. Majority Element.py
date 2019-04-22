# -*- coding: utf-8 -*-
"""
   File Name：     169. Majority Element
   Description :
   Author :       simon
   date：          19-4-13
"""

"""
分而治之
如果我能知道左半部分的众数  和右半部分的众数  就可以找到全局的众数 
因为我现在只需要再比较这两个数谁出现的更多就行

时间复杂度 O(nlogn)
复杂度不是最优  只是来理解一下分而治之的思想
"""
class Solution:
    def majorityElement(self, nums, lo=0, hi=None):
        def majority_element_rec(lo, hi):
            # base case; the only element in an array of size 1 is the majority
            # element.
            if lo == hi:
                return nums[lo]

            # recurse on left and right halves of this slice.
            mid = (hi - lo) // 2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid + 1, hi)

            # if the two halves agree on the majority element, return it.
            if left == right:
                return left

            # otherwise, count each element and return the "winner".
            left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums) - 1)
