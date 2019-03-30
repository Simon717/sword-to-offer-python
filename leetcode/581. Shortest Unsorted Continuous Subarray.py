# -*- coding: utf-8 -*-
"""
   File Name：     581. Shortest Unsorted Continuous Subarray
   Description :
   Author :       simon
   date：          19-3-25
"""

""" 总结起来就是 先缩到最小 然后逐渐放大区间 """
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p1, p2 = 0, len(nums)-1
        while p1+1< len(nums) and nums[p1] <= nums[p1+1]:
            p1 += 1

        if p1 + 1 == len(nums):
            return 0

        while p2-1>=0 and nums[p2] >= nums[p2-1]:
            p2 -= 1

        minnum = min(nums[p1:p2+1])
        maxnum = max(nums[p1:p2+1])

        while p1>=0 and nums[p1] > minnum:
            p1 -= 1

        while p2<len(nums) and nums[p2] < maxnum:
            p2 += 1
        return p2 - p1 - 1

"""
    直接sort，然后找出sort前与sort后不同的数组长度
"""
class Solution_(object):
    def findUnsortedSubarray(self, nums):

        sortnums = sorted(nums)
        stt, end = 0, len(nums) - 1

        while stt<len(nums) and nums[stt] == sortnums[stt]:
            stt += 1

        while end>=0 and (nums[end] == sortnums[end]):
            end -= 1

        return end - stt + 1 if end > stt else 0

"""
要满足三个性质：

nums[0, i - 1] and nums[j + 1, n - 1] are both sorted.
nums[i] != nums_sorted[i] and nums[j] != nums_sorted[j].
nums[i - 1] <= min and max <= nums[j + 1], where min and max are the minimum and maximum values of subarray nums[i, j].
所以我们需要做的就是 find the two longest sorted subarrays starting at index 0 and ending at index n - 1

从左到右找到第一个不满足nums[l] <= nums[l+1]的index l
然后从右到左找到第一个不满足nums[r] >= nums[r-1]的 index r
    此时 [l, r]是可能的最小的区间 因为左右两侧的有序性是必须满足的
然后开始保证第三条性质，只要min(nums[l:r+1]) < nums[l]，l就自减1；只要max(nums[l:r+1]) > nums[r], r就自增1；
    此时在根据条件放大当前的区间
这两个index中间这一坨就是需要我们sort的最短subarray

总结起来就是 先缩到最小 然后逐渐放大区间
"""
import sys
class Solution__(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l < r and nums[l] <= nums[l + 1]:
            l += 1
        if l >= r:
            return 0
        while r > 0 and nums[r] >= nums[r - 1]:
            r -= 1
        max_num, min_num = -sys.maxsize, sys.maxsize

        for k in range(l, r + 1):
            max_num = max(max_num, nums[k])
            min_num = min(min_num, nums[k])

        while l >= 0 and min_num < nums[l]:
            l -= 1
        while r < len(nums) and nums[r] < max_num:
            r += 1

        return r - l - 1

# class Solution_(object):
#     def findUnsortedSubarray(self, nums):



if __name__ == '__main__':
    # test = [2, 6, 4, 8, 10, 9, 15]
    test =  [1,3,2,2,2]
    solu = Solution()
    print(solu.findUnsortedSubarray(test))