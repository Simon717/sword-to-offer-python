# -*- coding: utf-8 -*-
"""
   File Name：     34. Find First and Last Position of Element in Sorted Array
   Description :
   Author :       simon
   date：          19-4-1
"""

"""
O(n)
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        res = [-1, -1]
        nums.append('#')
        meet = False
        hold = False
        for i, n in enumerate(nums):
            if n == target and  not meet:
                res[0] = i
                meet = True
                hold = True
            elif hold and nums[i]!=nums[i-1]:
                res[1] = i-1
                return res
        return res

"""
O(log n) 必须二分

"""
class Solution_(object):
    def searchRange(self, nums, target):

        if not nums:
            return [-1, -1]

        left, right = 0, len(nums) - 1
        res = []
        # find left index
        while left <= right:
            mid = left + (right - left) >> 1
            if nums[mid] == target and (mid == 0 or nums[mid-1] != target): # 边界处理要细腻
                res.append(mid)
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        if not res:
            return [-1, -1]

        # find right index
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) >> 1
            if nums[mid] == target and (mid == len(nums)-1 or nums[mid+1] != target): # 边界处理要细腻
                res.append(mid)
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return res

if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(Solution().searchRange(nums, target))
