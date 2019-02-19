# -*- coding: utf-8 -*-
"""
   File Name：     01 二维数组查找
   Description :
   Author :       YYJ
   date：          2019-02-12
"""


class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if array == []:
            return False

        M, N = len(array), len(array[0])

        # 从右上角开始
        i, j =  0, N-1
        while i<M and j>=0:
            if array[i][j] == target:
                return True
            if array[i][j] > target:
                    j -= 1
            else:
                    i += 1
        return False


if __name__ == '__main__':
    testArr = [[1,2], [3,4]]
    solu = Solution()
    print(solu.Find(3, testArr))