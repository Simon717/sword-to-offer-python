# -*- coding: utf-8 -*-
"""
   File Name：     96. Unique Binary Search Trees
   Description :
   Author :       simon
   date：          19-3-26
"""

"""
n = 0 1 2 3都正确 
4 开始 小于 正确解
"""
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        self.cnt = 0

        def DFS(n):
            if n == 0:
                self.cnt += 1
                return
            if n < 0:
                return
            # if left and not right:
            #     DFS(n - 1, 1, 0)
            # if right and not left:
            #     DFS(n - 1, 0, 1)
            # if left and right:
            #     DFS(n - 2, 1, 1)
            DFS(n-1)
            DFS(n-1)
            DFS(n-2)

        DFS(n-1)
        return self.cnt


"""
h(n) = h(0)*h(n-1) + h(1)*h(n-2) + ... + h(n-1)h(0)
"""
class Solution(object):
    def numTrees(self, n):
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(0, i):
                dp[i] += dp[j]*dp[i-1-j]

        return dp[-1]

if __name__ == '__main__':
    solu = Solution()
    print(solu.numTrees(3))
