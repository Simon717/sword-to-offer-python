# -*- coding: utf-8 -*-
"""
   File Name：     62. Unique Paths
   Description :
   Author :       simon
   date：          19-3-26
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        self.cnt = 0  # 如果是list 可以不用加self duiyu

        def DFS(i, j, idx):
            if check(i, j):
                if idx == m + n - 1:
                    self.cnt += 1

                DFS(i + 1, j, idx + 1)
                DFS(i, j + 1, idx + 1)

        def check(i, j):
            return i < m and j < n

        DFS(0, 0, 1)
        return self.cnt

    # 空间复杂度 O(m*n)
    def uniquePaths_DP(self, m, n):

        DP = [[1]*n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                DP[i][j] = DP[i-1][j] + DP[i][j-1] # 这里发现每一次更新只需要上一行的结果 和 这一行的结果 i-1行 i行
        return DP[-1][-1]

    # 空间复杂度 O（n）
    def uniquePaths_DP1(self, m, n):
        pre = [1] * n # 上一行的结果
        cur = [1] * n # 这一行的结果
        for i in range(1,m):
            for j in range(1,n):
                cur[j] = pre[j] + cur[j-1]
            pre = cur

        return cur[-1]

    def uniquePaths_DP2(self, m, n):
        cur = [1] * n  # 这一行的结果
        for i in range(1, m):
            for j in range(1, n):
                cur[j] = cur[j] + cur[j - 1]
        return cur[-1]

    def uniquePaths_math(self, m, n):
        def factorial(num):
            res = 1
            for i in range(1,num+1):
                res *= i
            return res

        return factorial(m+n-2) // factorial(m-1) // factorial(n-1)



if __name__ == '__main__':
    solu = Solution()
    print(solu.dp2(2, 2))
