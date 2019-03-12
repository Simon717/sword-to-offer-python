# -*- coding: utf-8 -*-
"""
   File Name：     283. Move Zeroes
   Description :
   Author :       simon
   date：          19-3-12
"""
"""
直接考虑每个非零数字最终需要移动的次数
使用一个List存放每一个元素需要移动的距离
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        move = [0] * N
        cnt = 0
        for i in range(N):
            move[i] = cnt
            if not nums[i]:
                cnt += 1
        for i in range(N):
            nums[i - move[i]] = nums[i]
        for i in range(N - cnt, N):
            nums[i] = 0

class Solution1(object):
    def sao(self, nums):
        nums.sort(key=bool, reverse=True)
        nums.sort(key=lambda x: 1 if not x else 0)

class Solution0(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        last0 = 0 # 可以分成第一个数字为0 和第一个数字不为0两种情况讨论
                    #如果第一个数字不为 last0将跟着不为零的数字一直往前走 知道找到一个0
        for i in range(0, len(nums)):
            if (nums[i] != 0):
                nums[i], nums[last0] = nums[last0], nums[i]
                last0 += 1 # 每发生一次交换 0 都会岁之后移
