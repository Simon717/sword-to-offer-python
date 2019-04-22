# -*- coding: utf-8 -*-
"""
   File Name：     头条 旅行计划
   Description :
   Author :       simon
   date：          19-4-14
"""
# 在这里修改测试样例
test = """4
0 2 6 5 
2 0 4 4
6 4 0 2
5 4 2 0
"""

# DEBUG = 1 # DEBUG = 1 用于本地调试 DEBUG = 0 用于线上提交
# if DEBUG:
#     with open('test.txt', 'w') as f:
#         f.writelines(test)
#     with open('test.txt', 'r') as f:
#         lines = f.readlines() # 利用txt文件的readlines 模拟sys.stdin.readlines() 不需要每一次手动输入测试样例 不然心态容易炸裂
# else:
#     import sys
#     lines = sys.stdin.readlines()


import sys
lines = sys.stdin.readlines()
lines = lines[1:]
matrix = []
for line in lines:
    l = line
    matrix.append(list(map(int, l)))

n = len(matrix)
for i in range(n):
        matrix[i][i] = float('inf')

# print(matrix)
n = len(matrix)
stt = 0
visited = [stt]
res = 0
for i in range(n):
    # for j in matrix:
    #     print(j)
    if i == n-1:
        res += matrix[0][stt]
        break
    # if i == 0:
    #     stt = min(matrix[0])
    #     index = matrix[0].index(stt)
    tp_min = min(matrix[stt])
    end = matrix[stt].index(tp_min)
    matrix[stt][end] = matrix[end][stt] = float('inf')
    stt = end
    res += tp_min

    # print(tp_min)
print(res)

