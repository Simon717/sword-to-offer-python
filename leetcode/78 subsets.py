# -*- coding: utf-8 -*-
"""
   File Name：     78 subsets
   Description :
   Author :       simon
   date：          19-3-15
"""


# Combination 不考虑元素的顺序
# Author: Huahua, running time: 60 ms
"""

"""
class Solution:
    def subsets(self, nums):
        res = []

        def dfs(s, path):
            res.append(path[:])
            for i in range(s, len(nums)):
                dfs(i + 1, path + [nums[i]]) # 因为不能有冲恢复元素 所以不回头 i + 1

        dfs(0, [])
        return res

"""
复杂度 2^n
思路很清晰 
每一个位置上的数字都可以选择取还是不取
"""
class Solution_(object):

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def search(path, idx):
            if idx == len(nums):
                res.append(path)
            else:
                search(path + [nums[idx]], idx + 1)
                search(path, idx + 1)

        search([], 0)
        return res

test = [0, 1, 2]
solu = Solution_()
print(solu.subsets(test))
