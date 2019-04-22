# -*- coding: utf-8 -*-
"""
   File Name：     最小编辑狙击
   Description :
   Author :       simon
   date：          19-4-12
"""
"""
这两天一直没有弄清楚 递归 DP 自顶向下 自底向上 之间的关系、
之前的认知是 DP是自底向上 递归是自顶向下
现在发现DP 递归 都可以是自顶向下 或者自底向上 没有限制
"""
class solution:
    def minDistance(self, word1, word2):
        if not word1 and not  word2: # 0 0
            return 0
        if not word1 or not word2: # 01 10
            return 1

        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        return 1 + min(self.minDistance(word1[1:], word2), self.minDistance(word2[0] + word1, word2), self.minDistance(word2[0] + word1[1:], word2))




"""
递归 + memo
"""
class Solution(object):
    def __init__(self):
        self.memo = {}

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1 and not  word2: # 0 0
            return 0
        if not word1 or not word2: # 01 10
            return len(word1) or len(word2)

        if word1[0] == word2[0]: # 相等的情况下直接考虑后面
            return self.minDistance(word1[1:], word2[1:])
        # 不相等的情况下考虑对当前元素  删除 插入 替换 操作数+1
        if (word1, word2) not in self.memo:
            res =  1 + min(self.minDistance(word1[1:], word2), self.minDistance(word1, word2[1:]),
                    self.minDistance(word1[1:], word2[1:]))  # 删除 插入 替换
            self.memo[(word1, word2)] = res
        return self.memo[(word1, word2)]



if __name__ == '__main__':
    print(solution().minDistance('abc', 'bce'))
