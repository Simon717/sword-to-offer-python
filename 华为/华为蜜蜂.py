# -*- coding: utf-8 -*-
"""
   File Name：     华为蜜蜂
   Description :
   Author :       simon
   date：          19-4-3
"""
from math import sqrt

# line = input().strip().split()
# n = list(map(int, line))
# n = [int(i) for i in line]
# nums = [[n[0],n[1]], [n[2],n[3]], [n[4],n[5]], [n[6],n[7]], [n[8],n[9]]]

"""
我的代码
"""
nums = [[1,1], [2,2], [3,3], [4,4], [5,5]]

permu = []
index = list(range(5))
def DFS(path):
    if len(path) == 5:
        permu.append(path)
        return

    for i in index:
        if i not in path:
            DFS(path + [i])
DFS([])
print(permu)

def compute_dist(path):
    res = 0
    for i in range(len(path) - 1):
        res += sqrt((nums[path[i]][0] - nums[path[i+1]][0])**2 + (nums[path[i]][1] - nums[path[i+1]][0])**2)
    res += sqrt(nums[path[0]][0]**2 + nums[path[0]][1]**2)
    res += sqrt(nums[path[-1]][0]**2 + nums[path[-1]][1]**2)
    return res

import sys
minDist = sys.maxsize

for i in permu:
    dis = compute_dist(i)
    minDist = min(minDist, dis)
print(minDist)



"""
别人的
"""
nums = [[0,0],[1,1], [2,2], [3,3], [4,4], [5,5]]
order = [[1]]
for i in range(2,6):
    lens = len(order)
    j = 0
    while j < lens:
        for k in range(i-1):
            tmp = order[j][:]  #
            order.append(tmp)
            order[-1].insert(k, i)
        order[j].append(i)
        j += 1
# 接下来是制作距离矩阵
dist = [[0] * 6 for i in range(6)]
for i in range(6):
    for j in range(6):
        if dist[i][j] == 0:
            dist[i][j] = sqrt((nums[i][0]-nums[j][0])**2 + (nums[i][1]-nums[j][1])**2)
        else:
            dist[i][j] = dist[j][i]
# 贪心算法取最小
minVal = 0
for path in order:
    sums = dist[0][path[0]]
    for i in range(4):
        sums += dist[path[i]][path[i+1]]
    sums += dist[path[4]][0]
    if minVal > sums or minVal == 0:
        minVal = sums
print(minVal)