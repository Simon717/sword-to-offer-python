# -*- coding: utf-8 -*-
"""
   File Name：     64. Minimum Path Sum
   Description :
   Author :       simon
   date：          19-3-26
"""

"""
简单的DP问题
f(m,n) = nums[m][n] + min(f(m-1,n), f(m, n-1))
"""
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0]) if rows else 0 # 这么写最为保险

        for i in range(1, rows):
            grid[i][0] += grid[i-1][0]
        for i in range(1, cols):
            grid[0][i] += grid[0][i-1]

        for i in range(1, rows):
            for j in range(1, cols):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        print(grid)
        return grid[-1][-1]

if __name__ == '__main__':
    test = [
              [1,3,1],
              [1,5,1],
              [4,2,1]
            ]
    solu = Solution()
    print(solu.minPathSum(test))