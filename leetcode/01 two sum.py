# -*- coding: utf-8 -*-
"""
   File Name：     01 two sum
   Description :
   Author :       simon
   date：          19-3-11
"""
"""
每一个数字的下方 存放这个数字可能的解 当下次的遍历遇到这个解之后 return
用hash表存下想要遇到的解 一旦遇到返回另一半的index和当前的index
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(nums):
            if num not in dic:
                dic[target-num] = i
            else:
                return [dic[num], i]
        return [-1, -1]

    def twoSum_sim(self, nums, target):
        dic = {}
        for i, num in enumerate(nums):
            if num in dic:
                return dic[num], i
            dic[target-num] = i


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dic = {}

        for i, n in enumerate(nums):
            if target - n in dic:
                return [i, dic[target-n]]
            dic[n] = i
        return [-1, -1]


