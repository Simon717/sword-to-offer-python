# -*- coding: utf-8 -*-
"""
   File Name：     45 孩子们的游戏(圆圈中最后剩下的数)
   Description :
   Author :       simon
   date：          19-3-5
"""
# -*- coding:utf-8 -*-
"""
明确函数的定义
f[i] = (f[i-1] + m) % i 中i代表当前队伍当中剩余的人数 
f函数返回值为index 范围是0～n-1
"""

class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n < 1: # 最后一个孩子是n-1 所以至少得有1个人
            return -1

        res = 0
        for i in range(1, n+1): # i代表的是人数 所以i从1到 n
            res  = (res + m) % i # f[i] = (f[i-1] + m) % i
        return res