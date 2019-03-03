# -*- coding: utf-8 -*-
"""
   File Name：     subsets
   Description :
   Author :       simon
   date：          19-3-2
"""
class Solution:
# @param {integer[]} nums
# @return {integer[][]}
    def subsets(self, nums):
        if nums is None:
            return []
        result = []
        nums.sort()
        self.dfs(nums, 0, [], result)
        return result

    def dfs(self, nums, pos, list_temp, ret):
        # append new object with []
        ret.append([] + list_temp)
        printList(list_temp)
        # print(pos)
        for i in range(pos, len(nums)): # 每次把排序后的数据中的最后一个元素处理完之后返回上级
            list_temp.append(nums[i])
            self.dfs(nums, i + 1, list_temp, ret)
            list_temp.pop()

# 对于各个元素进行二进制编码
class Solution0:
    def subsets(self, S):
        if not S:
            return []

        ret = []
        S.sort()
        n = len(S)
        # 000 -> []
        # 001 -> [1]
        # 010 -> [2]
        # ...
        # 111 -> [1, 2, 3]
        for i in range(2 ** n):
            tmp = []
            for j in range(n):
                if i & (1 << j):
                    tmp.append(S[j])
            ret.append(tmp)
        return ret

def printList(nums):
    strlist = [str(x) for x in nums]
    print('---'.join(strlist))

test = [1,2,3,4]
solu = Solution()
print(solu.subsets(test))