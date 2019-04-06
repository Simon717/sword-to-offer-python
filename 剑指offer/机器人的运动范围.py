# -*- coding: utf-8 -*-
"""
   File Name：     机器人的运动范围
   Description :
   Author :       simon
   date：          19-3-19
"""


# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        if rows < 1 or cols < 1 or threshold < 0:
            return 0
        visited = [0] * rows * cols
        return self.helper(threshold, rows, cols, 0, 0, visited)

    # 定义辅助函数的规范： 不变的参数放在前面 变化的参数放在后面
    def helper(self, threshold, rows, cols, i, j, visited):
        if 0 <= i < rows and 0 <= j < cols and self.bitsum(i) + self.bitsum(j) <= threshold and not visited[i * cols + j]:
            visited[i * cols + j] = True # 对于没见过的数字进行累加计数即可..
            return 1 + self.helper(threshold, rows, cols, i + 1, j, visited) + \
                       self.helper(threshold, rows, cols, i - 1, j, visited) + \
                       self.helper(threshold, rows, cols, i, j + 1, visited) + \
                       self.helper(threshold, rows, cols, i, j - 1, visited)
        return 0 # 递归底 无路可走之时 return 0

    def bitsum(self, num):
        res = 0
        while num:
            res += num % 10
            num = num // 10
        return res


"""
使用hash表 记录各个点是否访问过 比数组使用起来简单
尽量在函数内定义变量 + 使用全局变量 减少参数在函数之间的传递
"""
class Solution_:
    def movingCount(self, threshold, rows, cols):
        # write code here
        if rows < 1 or cols < 1 or threshold <= 0:
            return 0

        self.hash = {}
        self.cnt = 0
        def DFS(i, j):
            if check(i, j):
                self.cnt += 1
                self.hash[(i, j)] = 1
                DFS(i - 1, j)
                DFS(i + 1, j)
                DFS(i, j + 1)
                DFS(i, j - 1)

        def check(i, j):
            def getSum(num):
                res = 0
                while num:
                    res += num % 10
                    num = num // 10
                return res

            return 0 <= i < rows and 0 <= j < cols and (i, j) not in self.hash and getSum(i) + getSum(j) <= threshold

        DFS(0, 0)
        return self.cnt



solu = Solution_()
print(solu.movingCount(5, 10, 10))