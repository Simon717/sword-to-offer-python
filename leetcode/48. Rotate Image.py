# -*- coding: utf-8 -*-
"""
   File Name：     48. Rotate Image
   Description :
   Author :       simon
   date：          19-3-25
"""

"""

"""
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 上下翻转
        for i in range(n//2):
            matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i]
        # 主对角线翻转
        for i in range(n):
            for j in range(i+1,n):  # 这里只取一半的元素..
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# if __name__ == '__main__':

