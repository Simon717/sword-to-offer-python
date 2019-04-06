# -*- coding: utf-8 -*-
"""
   File Name：     顺子3
   Description :
   Author :       simon
   date：          19-4-6
"""
import collections
import sys
lines = sys.stdin.readlines().strip()

# lines = lines[1:]
lines = lines[::2][1:]
N = len(lines)
# print(lines)

dic = {'A': 1,
       'J': 11,
       'Q': 12,
       'K': 13}

nums = []
for line in lines:
    tp = line.strip().split(' ')
    num = []
    for i in tp:
        if i in dic:
            num.append(dic[i])
        else:
            num.append(int(i))
    nums.append(num)

lines = nums
# count = [0]*13
# m[i][j] 从i开始 到j结束能否组成顺子(长度=j-i+1)
# 那么i的范围是1-9
# j的范围是1-13
'''
递归方程
m[i][j] = 1 if m[i][j-1]=1 and j in nums
else m[i][j] = 0

'''

for i in range(N):
    nums = lines[i]
    m = [[0] * (14) for j in range(10)]

    # 统计各元素出现次数

    count = collections.Counter(nums)

    for num in nums:
        m[num][num] = 1

    for r in range(1, 13):
        for i in range(1, 10):
            j = i + r
            if j >= 13:
                break
            m[i][j] = 1 if (m[i][j - 1] == 1 and j in nums) else 0

    ans = 0
    for r in range(4, 13):
        for i in range(1, 10):
            j = i + r
            if j >= 13:
                break
            if m[i][j] == 1:
                tmp = 1
                for k in range(i, j + 1):
                    tmp *= count[k]
                ans += tmp

    print(ans)