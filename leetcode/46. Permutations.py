# -*- coding: utf-8 -*-
"""
   File Name：     46. Permutations
   Description :
   Author :       simon
   date：          19-3-12
"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, [], res) # 好好感受这个输入参数 可以直接修改
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)): # 遍历当前没有确定的数字
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res) # 选出中间一个数字 这个数字加入路径 递归考虑剩余的数字