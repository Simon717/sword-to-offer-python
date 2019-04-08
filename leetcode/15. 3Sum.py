# -*- coding: utf-8 -*-
"""
   File Name：     15. 3Sum
   Description :
   Author :       simon
   date：          19-4-8
"""


class Solution(object):  # 此法也超时
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def twoSum(nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
            """
            lookup = {}
            for num in nums:
                if target - num in lookup:
                    if (-target ,target - num, num) not in res:
                        res.append((-target ,target - num, num))
                lookup[num] = target - num

        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            twoSum(nums[i+1:], 0-nums[i])
        return [list(i) for i in res]


"""
利用有序性去重...
如何保证所有的数字都不是重复的？
确保你的解由左到右 有序

思路是考虑解的第一个元素的所有可能情况
将第一个元素做成target
在第一个元素的后面开始找2sum 为什么不考虑前面的元素？ 因为去重 需要保证当前[a,b,c] a是最小的 所以不能往回找 只需要在后面的元素查找
"""
class Solution_(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n, res = len(nums), []
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:   # 因为i=0这个元素会直接往下执行
                continue
            l, r = i+1, n-1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if tmp == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif tmp > 0:
                    r -= 1
                else:
                    l += 1
        return res

"""
双指针 sweep 2sum
"""
class Solution__:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue # 这是一种重复情况 [a,b,c] a 相同
            left, right = i+1, len(nums)-1 # 标准的双指针sweep查找2sum
            while left < right:
                curSum = nums[i] + nums[left] + nums[right]
                if  curSum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[right] == nums[right+1]: right -= 1 # 防止重复解 [-2, 0, 0, 2, 2]
                    while left < right and nums[left] == nums[left-1]: left += 1 # 得确保下一个位置下的2sum不能和当前解重复 一定要移动到不一样的地方

                # while nums[i] + nums[left] + nums[right] > 0: # 优化 每一步只改变一下 就不用重复计算
                #     right -= 1
                # while nums[i] + nums[left] + nums[right] < 0:
                #     left += 1
                elif curSum > 0:
                    right -= 1
                else:
                    left += 1
        return res

    """
    找到所有不重复的解
    """
    def Sum2Sweep(self, nums, target):
        nums.sort()
        left, right = 0, len(nums) - 1
        res = []
        while left < right:
            cur = nums[left] + nums[right]
            if cur == target:
                res.append([nums[left], nums[right]]) # 收集了解之后一定要注意后面的处理
                left += 1
                right -= 1
                while left < right and nums[right] == nums[right + 1]: right -= 1  # 防止重复解 [-2, 0, 0, 2, 2]
                while left < right and nums[left] == nums[left - 1]: left += 1  # 得确保下一个位置下的2sum不能和当前解重复 一定要移动到不一样的地方
            elif cur > target:
                right -= 1
            else:
                left += 1
        return res

if __name__ == '__main__':
    test = [1,1,2,2,3,3]
    print(Solution__().Sum2Sweep(test, 4))



