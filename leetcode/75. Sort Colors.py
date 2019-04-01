# -*- coding: utf-8 -*-
"""
   File Name：     75. Sort Colors
   Description :
   Author :       simon
   date：          19-3-31
"""


"""
很明显的三路快速排序

简单的想法 是遇到0插入到数组首位 遇到2插入到数组尾 遇到1不用动
但是这么做需要移动很多次

改进：维护三路分区 012分别插入到各个分区的最后位置就可以
less 指向0区域的后一个元素 [left:less) 
i 指向1区域的后一个元素    [less, i)
greater 指向2区域的左边一个元素 （greater,right] 2
"""
class Solution(object):
    def sortColors(self, nums):
        less, i, greater = 0, 0, len(nums) - 1

        while i <= greater:
            if nums[i] == 0:
                nums[i], nums[less] = nums[less], nums[i]
                i += 1
                less += 1
            elif nums[i] == 1:
                i += 1
            else: # 2
                nums[i], nums[greater] = nums[greater], nums[i]
                # i += 1 # 从右边搬运来一个数 还没有对这个数进行判断 所以不能移动过去
                greater -= 1

        print(nums)



"""
count 排序
"""
class Solution_(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # 【0 1 2】
        dic = {0:0,
               1:0,
               2:0}
        for n in nums:
            dic[n] += 1

        for i in range(dic[0]):
            nums[i] = 0
        for i in range(dic[0], dic[0] + dic[1]):
            nums[i] = 1
        for i in range(dic[0]+dic[1], len(nums)):
            nums[i] = 2
        # nums = [0]*dic[0] + [1]*dic[1] + [2]*dic[2]

        print(nums)

"""
直接计数
"""
class Solution__(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        red, white = 0, 0
        for i in nums:
            if i == 0:
                red += 1
            elif i == 1:
                white += 1
        for i in range(red):
            nums[i] = 0
        for i in range(red, red+white):
            nums[i] = 1
        for i in range(red+white, len(nums)):
            nums[i] = 2

"""
只是用 两个指针 
只维护左右两个区域 
"""
class Solution___(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, left, right = 0, 0, len(nums) - 1 # left right 都是开区间
        while i < len(nums):
            if nums[i] == 2 and i < right:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            elif nums[i] == 0 and i > left:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
            else:
                i += 1

        print(nums)

if __name__ == '__main__':
    print(Solution___().sortColors([2,0,2,1,1,0,0,0]))


