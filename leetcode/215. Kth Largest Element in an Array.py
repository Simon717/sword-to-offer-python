# -*- coding: utf-8 -*-
"""
   File Name：     215. Kth Largest Element in an Array
   Description :
   Author :       simon
   date：          19-3-26
"""

"""
改成递归？ 
"""
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k  = len(nums) - k

        def partition(nums, stt, end):  # 可以把某一个数字移动到排完序的数组中的位置 并且实现二分类 左小右大
            p1, p2 = stt + 1, end
            pivot = nums[stt]
            while True:
                while p1 <= p2 and nums[p1] < pivot:
                    p1 += 1
                while p1 <= p2 and nums[p2] > pivot:
                    p2 -= 1
                if p1 > p2:
                    break
                else:
                    nums[p1], nums[p2] = nums[p2], nums[p1]
                    p1 += 1
                    p2 -= 1
            nums[stt], nums[p2] = nums[p2], nums[stt]
            return p2

        stt, end = 0, len(nums) - 1
        idx = partition(nums, stt, end)
        while idx != k:
            if idx < k:
                stt = idx + 1
            else:
                end = idx - 1
            idx = partition(nums, stt, end)
        return nums[idx]


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k  = len(nums) - k

        def partition(nums, stt, end):  # 可以把某一个数字移动到排完序的数组中的位置 并且实现二分类 左小右大
            p1, p2 = stt + 1, end
            pivot = nums[stt]
            while True:
                while p1 <= p2 and nums[p1] < pivot:
                    p1 += 1
                while p1 <= p2 and nums[p2] > pivot:
                    p2 -= 1
                if p1 > p2:
                    break
                else:
                    nums[p1], nums[p2] = nums[p2], nums[p1]
                    p1 += 1
                    p2 -= 1
            nums[stt], nums[p2] = nums[p2], nums[stt]
            return p2

        def helper(nums, stt, end):
            idx = partition(nums, stt, end)
            if idx < k:
                stt = idx + 1
            else:
                end = idx - 1



"""
思路 2 ******- 时间复杂度: O(Nlgk)******- 空间复杂度: O(k)******

前面的思路是全部放进去以后再pop k次

现在打算只维护一个容量为k的最大堆，最终堆顶的值就是结果 

时间最快
"""

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0

        from heapq import *

        heap = []
        for i in range(len(nums)):
            heappush(heap, nums[i])
            if len(heap) > k:
                heappop(heap)
        return heap[0]

# def partition(alist, first, last):
#     # rand = randint(first, last)  # 优化，随机取标定点，以解决近乎有序的列表
#     # alist[first], alist[rand] = alist[rand], alist[first]
#
#     pivot = alist[first]
#     left = first + 1
#     right = last
#     while True:  # 这里使用了双路快排，以解决有大量相同值的列表
#         while left <= right and alist[left] < pivot:
#             left += 1
#         while right >= left and alist[right] > pivot:
#             right -= 1
#
#         if left > right:
#             break
#         else:
#             alist[left], alist[right] = alist[right], alist[left]
#             left += 1
#             right -= 1
#     alist[first], alist[right] = alist[right], alist[first]  # right处于<=v部分的最后一个元素
#     return right
#

"""
速度巨慢 
内存巨大
但是很容易理解 
"""
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pivot = nums[0]
        smaller = [num for num in nums if num < pivot] # 用最简单的方式实现三分类
        equal = [num for num in nums if num == pivot]
        greater = [num for num in nums if num > pivot]

        if len(greater) >= k:
            return self.findKthLargest(greater, k)  # k may be there
        elif len(equal) >= (k - len(greater)):  # k may be in equal or smaller
            return equal[0]  # any number from equal
        else:
            return self.findKthLargest(smaller, k - len(greater) - len(equal))

if __name__ == '__main__':
    solu = Solution()
    print(solu.findKthLargest([3,1,2,4], 4))
