# -*- coding: utf-8 -*-
"""
   File Name：     30 最小的K个数
   Description :
   Author :       simon
   date：          19-2-22
"""

# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not self.CheckValidInputs(tinput, k):
            return []

        self.findK(tinput, k-1)
        res = tinput[:k]
        res.sort()
        return res

    def CheckValidInputs(self, tinput, k):
        if not tinput or k > len(tinput):
            return 0
        return 1

    def findK(self, nums, K): # 复杂度O(n)
        start, end = 0, len(nums)-1
        index  = self.Partition(nums, start, end)
        while index != K:
            if index < K:
                start = index +  1
            else:
                end = index - 1
            index = self.Partition(nums, start, end)
        return nums[index]

        pass

    def Partition(self, nums, start, end):
        pivot = nums[start]
        left, right = start+1, end
        while True:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1

            if left > right:
                break
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        nums[start], nums[right] = nums[right], nums[start]
        return right

if __name__ == '__main__':
    test = [5,2,3,4,1]
    solu = Solution()
    print(solu.GetLeastNumbers_Solution(test, 5))