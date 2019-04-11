# -*- coding: utf-8 -*-
"""
   File Name：     网易 堆棋子
   Description :
   Author :       simon
   date：          19-4-9
"""
import sys
"""
重点在于证明 最终聚合的点位于xy的组合中
只有暴力搜索可能的聚合点 
然后计算可能的
"""
_ = input()
x = input().strip().split(' ')
y = input().strip().split(' ')
xs = list(map(int, x))
ys = list(map(int, y))
N = len(x)

res = [float('inf')] * N
for x in xs:
    for y in ys:
        dists = [abs(x - xs[i]) + abs(y - ys[i]) for i in range(N)]
        dists.sort()
        for i in range(1, N): # 计算累加和
            dists[i] += dists[i - 1]
        for i in range(1, N):
            res[i] = min(res[i], dists[i])
res = ['0'] + [str(x) for x in res[1:N]]
print(' '.join(res))
