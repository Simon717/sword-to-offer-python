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
        self.dfs(nums, [], res) # python list 类型可以原地修改
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)): # 遍历当前没有确定的数字
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res) # 选出中间一个数字 这个数字加入路径 递归考虑剩余的数字


class Solution_(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]

        self.res = []

        def DFS(path, nums):
            if not nums:
                self.res.append(path)
                return
            for i in range(len(nums)):
                DFS(path+[nums[i]], nums[:i]+nums[i+1:])

        DFS([], nums)
        return self.res

"""
发现这题和之前的题目很像 也可以看成是之前走过的节点不要再走的问题
hash存放之前走过的路径
"""
class Solution_hash(object):
    def permute(self, nums):
        if not nums:
            return [[]]

        self.res = []
        self.hash = {}

        def DFS(path):
            if len(path) == len(nums): # 结果收集
                self.res.append(path)
                return

            for i in range(len(nums)):
                if i not in self.hash: # check 这个点没有被访问过
                    self.hash[i] = 1
                    DFS(path + [nums[i]])
                    self.hash.pop(i)
        DFS([])
        return self.res



test = [1,2,3]
solu = Solution_hash()
print(solu.permute(test))
