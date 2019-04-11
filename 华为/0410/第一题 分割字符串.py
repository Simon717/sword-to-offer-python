# -*- coding: utf-8 -*-
"""
   File Name：     第一题
   Description :
   Author :       simon
   date：          19-4-11
"""

# 在这里修改测试样例
test = """1 abc 12345678910
"""

DEBUG = 1 # DEBUG = 1 用于本地调试 DEBUG = 0 用于线上提交
if DEBUG:
    with open('test.txt', 'w') as f:
        f.writelines(test)
    with open('test.txt', 'r') as f:
        lines = f.readlines() # 利用txt文件的readlines 模拟sys.stdin.readlines() 不需要每一次手动输入测试样例 不然心态容易炸裂
else:
    import sys
    lines = sys.stdin.readlines()

line = lines[0]
line = line.strip().split(' ')[1:]

res = []
for s in line:
    while len(s) >= 8:
        res.append(s[:8])
        s = s[8:]
    if s:
        res.append(s + '0'*(8 - (len(s)%8)))

res.sort()
print(' '.join(res))
