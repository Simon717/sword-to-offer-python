# -*- coding: utf-8 -*-
"""
   File Name：     79. Word Search
   Description :
   Author :       simon
   date：          19-4-2
"""

"""
使用hash表 记录有没有访问过该节点
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        rows, cols = len(board), len(board[0])
        self.hash = {}
        self.flag = False

        def DFS(i, j, index):
            # print(path)
            if index == len(word):
                self.flag = True
                return

            if 0 <= i < rows and 0 <= j < cols and (i, j) not in self.hash and board[i][j] == word[index]:
                self.hash[(i, j)] = 1
                DFS(i - 1, j, index + 1)
                DFS(i + 1, j, index + 1)
                DFS(i, j - 1, index + 1)
                DFS(i, j + 1, index + 1)
                del self.hash[(i, j)]

        for i in range(rows):
            for j in range(cols):
                DFS(i, j, 0)
        return self.flag

"""
优化 
- 去掉hash
- 去掉全局变量 
- 提前终止程序
"""
class Solution__(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        rows, cols = len(board), len(board[0])

        def DFS(i, j, index):
            if not 0 <= i <= rows - 1 or not 0 <= j <= cols - 1 or board[i][j] != word[index]: # 使用 or 终止程序肯定比 and 快
                return False
            if index == len(word) - 1: return True

            board[i][j] = '#'
            res =  DFS(i - 1, j, index + 1) or DFS(i + 1, j, index + 1) or DFS(i, j - 1, index + 1) or DFS(i, j + 1, index + 1)
            board[i][j] = word[index]
            return res

        for i in range(rows):
            for j in range(cols):
                if DFS(i, j, 0): return True
        return False


        # return any(DFS(i,j,0) for i in range(rows) for j in range(cols))


"""
其实没有必要使用hash
走过的路径直接表上特殊符号就可以
"""
class Solution_:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        if not word:
            return True

        row = len(board)
        col = len(board[0]) if row else 0

        def DFS(i, j, idx):
            if not 0 <= i <= row - 1 or not 0 <= j <= col - 1 or board[i][j] != word[idx]:
                return False
            if idx == len(word) - 1:
                return True
            board[i][j] = '*'
            res = DFS(i + 1, j, idx + 1) or DFS(i, j + 1, idx + 1) or DFS(i - 1, j, idx + 1) or DFS(i, j - 1, idx + 1)
            board[i][j] = word[idx]
            return res

        return any(DFS(i, j, 0) for i in range(row) for j in range(col))

if __name__ == '__main__':
    board =[
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]


    print(Solution__().exist(board, 'ABCCED'))

