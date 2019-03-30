# -*- coding: utf-8 -*-
"""
   File Name：     39. Combination Sum
   Description :
   Author :       simon
   date：          19-3-26
"""

"""
这种求和的问题 应该在每一步使用减法而不是最后使用加法 
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def DFS(path):
            tp =sum(path)
            if tp == target:
                res.append(path)
                return
            if tp > target:
                return

            for n in candidates:
                if path and n < path[-1]:
                    continue
                DFS(path + [n])

        DFS([])
        return res

    """
    加速效果明显
    """
    def combinationSum_(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        candidates.sort()

        def DFS(path, remain):
            if remain == 0:
                res.append(path)
                return
            if remain < 0:
                return

            for n in candidates:
                if path and n < path[-1]: # 要求结果按照从小到大排列 从而达到去重目的
                    continue
                DFS(path + [n], remain - n)

        DFS([], target)
        return res

    """
    优化 不需要每一次都需要整个数组遍历
    """
    def combinationSum__(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        candidates.sort()

        def DFS(path, remain, stt):
            if remain == 0:
                res.append(path)
                return
            if remain < 0:
                return

            for i in range(stt, len(candidates)):
                DFS(path + [candidates[i]], remain - candidates[i], i) # 仍然是强迫这个path由小到大

        DFS([], target, 0)
        return res


class Solution_(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def helper(remain, combi, idx):
            if remain < 0:
                return
            if remain == 0:
                res.append(combi)
                return
            if idx >= len(candidates):
                return
            helper(remain, combi, idx + 1)
            helper(remain - candidates[idx], combi + [candidates[idx]], idx)

        res = []
        helper(target, [], 0)
        return res

    """
    hash表的键值是数字 有什么问题
    """
    def combinationSum_hash(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def DFS(path):
            if sumHash(path) == target and path not in res:
                res.append(path)
                return
            if sumHash(path) > target:
                return

            for n in candidates:
                path[n] = path.get(n, 0) + 1
                DFS(path)
                path[n] -= 1
                if path[n] == 0: del path[n]

        def sumHash(dic):
            res = 0
            for k, v in dic:
                if v > 0:
                    res += k*v
            return res

        DFS({})
        return res

if __name__ == '__main__':
    test = [2,3,6,7]
    solu = Solution()
    print(solu.combinationSum__(test, 7))