# -*- coding: utf-8 -*-
"""
   File Name：     221. Maximal Square
   Description :
   Author :       simon
   date：          19-4-2
"""

"""
直观的解法 
使用二维的空间
"""
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0] * (cols + 1) for _ in range(rows+1)] # 直接存放正方形的边长
        # dp = [0] * (cols + 1)  # 第一行的结果

        for i in range(1, rows+1):
            for j in range(1, cols+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) # 注意dp matrix的坐标的变化 dp的坐标比matrix大一 因为长度比matrix大

        maxlen = max((max(x) for x in dp)) # python 找到二维list的最大值必须这么写 ..
        return maxlen ** 2

"""
优化空间使用
"""
class Solution_(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        # dp = [[0] * (cols + 1) for _ in range(rows+1)] # 直接存放正方形的边长
        dp = [0] * (cols + 1)  # 第一行的结果
        prev = dp # 定义为前一行的结果

        for i in range(1, rows+1):
            for j in range(1, cols+1):
                if matrix[i-1][j-1] == '1':
                    # dp[i][j] = 1 + min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) # 注意dp matrix的坐标的变化 dp的坐标比matrix大一 因为长度比matrix大
                    dp[j] = 1 + min(prev[j], prev[j-1], dp[j-1])
            # 当把当前行处理完毕 刷新prev
            prev = dp

        maxlen = max((max(x) for x in dp)) # python 找到二维list的最大值必须这么写 ..
        return maxlen ** 2



if __name__ == '__main__':
    test = [["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]]
    print(Solution().maximalSquare(test))

