# -*- coding: utf-8 -*-
"""
   File Name：     顺子
   Description :
   Author :       simon
   date：          19-4-6
"""

# 在这里修改测试样例
test = """2
6
7 3 3 4 4 5 6
5
1 2 3 4 5 6 7 8 9 10 11 12 13
"""

DEBUG = 1 # DEBUG = 1 用于本地调试 DEBUG = 0 用于线上提交
if DEBUG:
    with open('test.txt', 'w') as f:
        f.writelines(test)
    with open('test.txt', 'r') as f:
        lines = f.readlines() # 利用txt文件的readlines 模拟sys.stdin.readlines() 不需要每一次手动输入测试样例 不然心态容易炸裂
else:
    import sys
    lines = sys.stdin.readlines().strip()


from collections import Counter

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
# print(nums)

def oneline(nums):
    cnt = Counter(nums)
    uni = list(cnt.keys())
    uni.sort()
    cur = [uni[0]]
    res = 0
    for i, num in enumerate(uni[1:]):
        if num - cur[-1] == 1:
            cur.append(num)
        else:
            cur = [num]

        if len(cur) >= 5:
            res += getNumEndHere(cur, cnt)
    return res

def getNumEndHere(nums, cnt): # 固定终点
    res = 0
    end = len(nums) - 1
    stt = end - 4
    while stt >= 0:  # 考虑不同起点
        tp_res = 1
        for i in nums[stt:]:
            tp_res *= cnt[i]
        res += tp_res
        stt -= 1
    return res

for n in nums:
    print(oneline(n))




