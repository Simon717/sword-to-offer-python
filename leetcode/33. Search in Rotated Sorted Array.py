# -*- coding: utf-8 -*-
"""
   File Name：     33. Search in Rotated Sorted Array
   Description :
   Author :       simon
   date：          19-4-1
"""

"""
二分

"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        def biFind(left, right):
            while left <= right:
                mid = left + ((right - left) >> 1)
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        # 先判断目标在左半段 还是 右半段
        flag = 0 # 左段
        if target < nums[0]:
            flag = 1 # 右段

        # find split index
        split = 0
        if nums[0] < nums[-1]:
            res = biFind(0, len(nums)-1)
        else:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + ((right - left) >> 1)
                # print(mid)
                if nums[mid] < nums[mid - 1]:
                    split = mid
                    break
                elif nums[mid] > nums[0]:
                    left = mid + 1
                else:
                    right = mid - 1

            # print(split)

            if not flag:
                res = biFind(0, split-1)
            else:
                res = biFind(split, len(nums) - 1)
        return res

"""
看下面的注释
基于常规二分查找算法
重点在于 我们确定lr边界的时候需要考虑mid所在不同分段存在不同情况
"""
class Solution_(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + ((r - l) >> 1)
            if nums[mid] == target:
                return mid
            if nums[mid] <= nums[r]: # mid 位于 右半段
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else: # mid 位于 左半段
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            """
            看起来 上面的代码和下面的差不多
            但是 当我在尝试写下面的代码的时候发现这样不可行 
            target > nums[mid] 有两种情况  一种是二者位于同一区段 一种是二者位于两个区段 这两种情况l r 边界的变化是相反的
            所以需要 先确定mid所在的区段 之后分别判断target跟mid的关系 就可以确定lr边界的变化
            """
            # if target > nums[mid]:
            #     l = mid + 1
            # else:
            #     r = mid - 1

        return -1

class Solution_cpoy(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            if nums[mid] < nums[-1]: # mid 位于右段
                if nums[mid] <= target <= nums[-1]: # 为什么选择这个判断条件？ 是因为这一段容易判断
                                                    # 二分时 我们需要根据target所在mid的左半部分还是右半部分进行lr边界的变换
                                                    # 我们可以发现右半段的判断更加简单 左半部分包含两种情况 比较复杂
                    left = mid + 1
                else:
                    right = mid - 1
            else: # mid 位于左段
                if nums[0] <= target <= nums[mid]: # 同理 实测 等号随便取
                    right = mid - 1
                else:
                    left = mid + 1
        return -1

# class Solution__(object):
#     def search(self, nums, target):
#         left, right = 0, len(nums) - 1
#         while left <= right:
#             mid = left + ((right - left) >> 1)
#             if nums[mid] == target:
#                 return mid
#             if nums[mid] <= nums[right]:

"""
为啥可以找到 min index

"""
class Solution___:
    def search(self, nums, target):
        # 先去找到旋转数组的最小元素的下标
        left, right = 0, len(nums) - 1
        while left < right: # 思想是一定要等到区间缩小到1 不区判断mid是否可以直接命中
            mid = (left + right) // 2
            if nums[mid] > nums[right]: # mid 位于左段 target必然在右段
                left = mid + 1
            else: # mid位于右段 target位于左段
                right = mid # 一定不能是mid - 1 因为target本身就在右段上面 我们得保证不漏掉target

        index = left
        print(index, mid, left, right)

        # The usual binary search and accounting for rotation. 旋转数组的二分查找 需要知道旋转的index
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2 # 对于未旋转的坐标系下的坐标
            realmid = (mid + index) % len(nums) # 对于旋转的坐标系下的坐标 也是正真实的坐标
            if nums[realmid] == target:
                return realmid
            if nums[realmid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1







if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    # nums = [3,5,1]
    target = 0
    print(Solution___().search(nums, target))



