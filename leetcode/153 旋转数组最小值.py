# -*- coding: utf-8 -*-
"""
   File Name：     153 旋转数组最小值
   Description :
   Author :       simon
   date：          19-4-2
"""


"""
容易理解的方法
"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + ((r - l) >> 1)
            if nums[mid] < nums[mid - 1]: # 数组中唯一一个逆序 序列 找到之后直接返回
                return nums[mid]

            elif nums[mid] < nums[l]: # mid 位于右段 target位于左段
                r = mid - 1
            elif nums[mid] > nums[r]: # mid 位于左段 target位于右段
                l = mid + 1
            else: # 处理只有一个元素的情况 [1]
                return nums[l]

if __name__ == '__main__':
    print(Solution().findMin([2,3,4,0,1]))