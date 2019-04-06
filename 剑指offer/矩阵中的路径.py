# -*- coding: utf-8 -*-
"""
   File Name：     矩阵中的路径
   Description :
   Author :       simon
   date：          19-3-19
"""
# -*- coding:utf-8 -*-
"""
matrix 是一维数据
"""
class Solution:
    def __init__(self):
        self.flag = False
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not matrix or rows<=0 or cols<=0 or not path:
            return False

        matrix, path = list(matrix), list(path)
        self.helper(matrix, [], [], path, cols)
        return self.flag



    def helper(self, matrix, path, path_idx, tar, cols):
        if path == tar:
            self.flag = True

        for i in range(len(matrix)):
            # print(i)
            idx = path_idx[-1] if path_idx else 0
            if self.check(i, idx, cols) and (matrix[i] not in path):
                self.helper(matrix, path + [matrix[i]], path_idx + [i], tar, cols)
    # 检查两个点是否相邻
    def check(self, i, j, cols):
        if not j:
            return True
        a,b = i//cols, i%cols
        c,d = j//cols, j%cols
        return (abs(a-c) + abs(b-d)) <= 1

"""
标准解法 相当漂亮
"""
class Solution_:
    def hasPath(self, matrix, rows, cols, path):
        if matrix == None or rows < 1 or cols < 1 or path == None:
            return False

        visited = [0] * (rows * cols)

        pathLength = 0
        for row in range(rows): # 将起点的大循环拆开 可以避免找到path之后的递归执行 加速递归
            for col in range(cols):
                if self.hasPathCore(matrix, rows, cols, row, col, path, pathLength, visited):
                    return True
        return False

    def hasPathCore(self, matrix, rows, cols, row, col, path, pathLength, visited):
        if len(path) == pathLength:
            return True

        hasPath = False
        if row >= 0 and row < rows and col >= 0 and col < cols \
                and matrix[row * cols + col] == path[pathLength] and not visited[row * cols + col]:

            pathLength += 1
            visited[row * cols + col] = True

            hasPath = self.hasPathCore(matrix, rows, cols, row, col - 1, path, pathLength, visited) or \
                      self.hasPathCore(matrix, rows, cols, row - 1, col, path, pathLength, visited) or \
                      self.hasPathCore(matrix, rows, cols, row, col + 1, path, pathLength, visited) or \
                      self.hasPathCore(matrix, rows, cols, row + 1, col, path, pathLength, visited)

            if not hasPath: # 把当前可能的四个方向全部走完（1. 找到路径返回True  2. 没有找到路径 返回False）
                pathLength -= 1
                visited[row * cols + col] = False

        return hasPath


"""
使用hash记录节点的访问情况
"""


class Solution_hash:
    def hasPath(self, matrix, rows, cols, path):
        if not matrix or cols < 1 or rows < 1 or not path:
            return False

        self.hash = {}

        def DFS(i, j, index):
            if check(i, j, index):
                self.hash[(i, j)] = 1  # 标记当前节点已经被访问
                if index == len(path) - 1: return True
                flag = DFS(i + 1, j, index + 1) or DFS(i, j + 1, index + 1) or \
                       DFS(i - 1, j, index + 1) or DFS(i, j - 1, index + 1)
                self.hash.pop((i, j))  # 当前节点的后续节点都没有找到合适的路径 释放点当前节点 允许再次访问
                return flag
            return False

        def check(i, j, index):  # 对于当前节点的合法性进行判断
            return 0 <= i < rows and 0 <= j < cols and (i, j) not in self.hash and matrix[i * cols + j] == path[index]

        for i in range(rows):
            for j in range(cols):
                if DFS(i, j, 0): return True
        return False


if __name__ == '__main__':

    s = Solution_hash()
    ifTrue = s.hasPath("ABCESFCSADEE", 3, 4, "ABCCED")
    ifTrue2 = s.hasPath("ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS", 5, 8, "SGGFIECVAASABCEHJIGQEM")
    print(ifTrue)
    print(ifTrue2)


    # test = 'abcd'
    # solu = Solution()
    # print(solu.hasPath("ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS", 5, 8, "SGGFIECVAASABCEHJIGQEM"))