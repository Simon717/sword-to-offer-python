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