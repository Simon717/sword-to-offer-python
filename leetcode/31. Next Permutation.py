# -*- coding: utf-8 -*-
"""
   File Name：     31. Next Permutation
   Description :
   Author :       simon
   date：          19-4-7
"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index = 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                index = i
                break
        if index:
            for j in range(len(nums) - 1, -1, -1):
                if nums[j] > nums[index]: break
            nums[j], nums[index-1] = nums[index-1], nums[j]
        nums[index:] =nums[index:][::-1]
        print(nums)

class Solution_(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        idx = 0
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]: # find first number which is smaller than it's after number
                idx = i
                break
        if idx != 0: # if the number exist,which means that the nums not like{5,4,3,2,1}
            for i in range(len(nums)-1, idx-1, -1):
                if nums[i] > nums[idx-1]:
                    nums[i], nums[idx-1] = nums[idx-1], nums[i]
                    break

        nums[idx:] = nums[idx:][::-1]

if __name__ == '__main__':
    test = [5,4,3,2,1]
    Solution().nextPermutation(test)
