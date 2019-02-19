# -*- coding: utf-8 -*-
"""
   File Name：     19 顺时针打印矩阵
   Description :
   Author :       YYJ
   date：          2019-02-17
"""

# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if not matrix:
            return

        nRows,nCols = len(matrix), len(matrix[0])

        stt = 0
        res = []
        while(nRows>2*stt and nCols>2*stt):
            res.append(self.printCircle(matrix, stt))
            stt += 1
        out = []
        for i in res:
            out += i
        return out

    def printCircle(self, matrix, stt):
        nRows,nCols = len(matrix)-1, len(matrix[0])-1
        endR, endC = nRows-stt, nCols-stt
        res = []

        for i in range(stt, endC+1): # 横是一定要画的
            res.append(matrix[stt][i])
        if endR-stt: # 判断竖要不要画
            for i in range(stt+1,endR+1):
                res.append(matrix[i][endC])
        if endR - stt and endC - stt: #
            for i in range(endC-1, stt, -1):
                res.append(matrix[endR][i])
            for i in range(endR, stt, -1):
                res.append(matrix[i][stt])

        # res += matrix[stt][stt:endC] # numpy 的索引方式
        # res += matrix[stt:endR][endC]
        # res += matrix[endR][endC:stt:-1]
        # res += matrix[endR:stt:-1][stt]

        # for r in range(stt, endR+1):
        #     for c in range(stt, endC+1):
        #         res.append(matrix[r][c])
        return res

'''
思路超神：
可以模拟魔方逆时针旋转的方法，一直做取出第一行的操作
例如
1 2 3
4 5 6
7 8 9
输出并删除第一行后，再进行一次逆时针旋转，就变成：
6 9
5 8
4 7
继续重复上述操作即可
24ms
5632k
'''
class Solution0:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        result = []
        while (matrix):
            result += matrix.pop(0)
            if not matrix:
                break
            matrix = self.turn(matrix)
        return result

    def turn(self, matrix):
        newmat = []
        row = len(matrix)
        col = len(matrix[0])
        for i in range(col):
            newmat1 = []
            for j in range(row):
                newmat1.append(matrix[j][i])
            newmat.append(newmat1)
        newmat.reverse()
        return newmat

if __name__ == '__main__':
    matrix = [[1,  2,  3,  4],
              [5,  6,  7,  8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    matrix2 = [[1],[2],[3],[4],[5]]
    matrix3 = [[1,2],[3,4],[5,6],[7,8],[9,10]]
    matrix = [[1]]
    S = Solution()
    print(S.printMatrix(matrix3))
    # S.printMatrix(matrix2)
    # S.printMatrix(matrix3)