# -*- coding: utf-8 -*-
"""
   File Name：     01 二维数组查找
   Description :
   Author :       YYJ
   date：          2019-02-12
"""
# test
"""
二刷记录
"""


# -*- coding:utf-8 -*-
class Solution2:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        rows = len(array)
        cols = len(array[0]) if array else 0

        i, j = rows - 1, 0
        while i >= 0 and j < cols:
            if array[i][j] == target:
                return True
            elif array[i][j] < target:
                j += 1
            else:
                i -= 1
        return False


class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if array == []:
            return False

        M, N = len(array), len(array[0])

        # 从右上角开始
        i, j = 0, N - 1
        while i < M and j >= 0:
            if array[i][j] == target:
                return True
            if array[i][j] > target:
                j -= 1
            else:
                i += 1
        return False


if __name__ == '__main__':
    testArr = [[1, 2], [3, 4]]
    solu = Solution()
    print(solu.Find(3, testArr))
