# -*- coding: utf-8 -*-
"""
   File Name：     287. Find the Duplicate Number
   Description :
   Author :       simon
   date：          19-3-25
"""


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash = [0] * (len(nums) + 1)

        for num in nums:
            hash[num] += 1
        print(hash)
        for i in range(len(hash)):
            if hash[i] >= 2:
                return i

    """
    基于原理 n+1个 范围在[1,n]的数字中必然有重复的数字 
    基于二分查找思路不断缩小查找区间 范围在[1,n]的数字大于n 必然有重复 
    --> 范围在[1, (1+n)/2]的数字大于(1+n)/2的话必然存在重复 总感觉这个推理不严谨啊 
    """
    def findDuplicate_bi(self, nums):
        low, high = 1, len(nums) - 1 # l, r代表数的取值的范围 [1,n]
        while low <= high:
            mid = (low+high) >> 1
            cnt = sum(x <= mid for x in nums)
            if cnt > mid:
                high = mid - 1
            else:
                low = mid + 1
        return low

class Solution___(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 1, len(nums) - 1
        while low <= high:
            mid = (low + high) >> 1
            cnt = sum(x <= mid for x in nums)
            if cnt > mid:
                high = mid - 1
            else:
                low = mid + 1
        return low


if __name__ == '__main__':
    test = [3,1,4,4,2]
    solu = Solution()
    print(solu.findDuplicate_bi(test))