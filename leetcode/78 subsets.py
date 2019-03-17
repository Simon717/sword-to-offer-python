# -*- coding: utf-8 -*-
"""
   File Name：     78 subsets
   Description :
   Author :       simon
   date：          19-3-15
"""


# Combination 不考虑元素的顺序
# Author: Huahua, running time: 60 ms
class Solution:
    def subsets(self, nums):
        ans = []

        # C(m, n) 在m个数中找出n个数出来 有多少种组合
        def dfs(n, s, cur):
            if n == len(cur):
                ans.append(cur.copy())
                return

            for i in range(s, len(nums)):
                cur.append(nums[i])
                dfs(n, i + 1, cur)
                cur.pop()

        # i 表示解的长度 [0, ..., n]
        for i in range(len(nums) + 1):
            dfs(i, 0, [])
        return ans

    """
    需要理解 深度优先搜索
    """
    def subsets1(self, nums):
        res = []

        def dfs(nums, s, path):
            res.append(path[:])
            for i in range(s, len(nums)):
                dfs(nums, i + 1, path + [nums[i]]) # 因为不能有冲恢复元素 所以不回头 i + 1

        dfs(nums, 0, [])
        return res


test = [0, 1, 2]
solu = Solution()
print(solu.subsets1(test))
