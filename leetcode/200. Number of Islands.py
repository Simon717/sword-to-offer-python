# -*- coding: utf-8 -*-
"""
   File Name：     200. Number of Islands
   Description :
   Author :       simon
   date：          19-3-31
"""

"""
DFS 

这道题其实和之前的剑指offer最后补充的回溯问题很相似 机器人的运动范围 
每次找到一个运动范围之后 将这个范围全部清成0
"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])


        self.cnt = 0

        def DFS(i, j):
            if 0 <= i < rows and 0 <= j < cols and grid[i][j] == '1':
                grid[i][j] = '0'
                DFS(i + 1, j)
                DFS(i - 1, j)
                DFS(i, j + 1)
                DFS(i, j - 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    self.cnt += 1
                    DFS(i, j)
        return self.cnt

"""
简洁写法
"""
class Solution_(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                grid[i][j] = '0'
                map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1)) # 使用map函数直接调用四个方向
                return 1
            return 0
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[0])))

if __name__ == '__main__':
    print(Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))