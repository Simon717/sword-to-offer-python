# -*- coding: utf-8 -*-
"""
   File Name：     交错01串
   Description :
   Author :       simon
   date：          19-4-8
"""

"""
将输入和实际问题处理部分分离
将问提处理部分写成函数
"""

def helper(s):
    if not s:
        return 0
    maxEnd = s[0]
    res = 0
    for i in s[1:]:
        maxEnd = maxEnd + i if i != maxEnd[-1] else i
        res = max(res, len(maxEnd))
    return res

if __name__ == '__main__':
    s = input()
    print(helper(s))