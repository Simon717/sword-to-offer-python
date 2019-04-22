# -*- coding: utf-8 -*-
"""
   File Name：     70. Climbing Stairs
   Description :
   Author :       simon
   date：          19-3-15
"""


"""
Top down - TLE 递归求解
"""
def climbStairs1(self, n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return self.climbStairs(n - 1) + self.climbStairs(n - 2)

"""
top down  + memo
仍然采用递归求解
但是将解存下 就可以避免重复计算
"""
class Solution(object):
    def climbStairs(self, n):
        if n == 1: return 1
        dic = [-1 for i in range(n)] # 把解存下来 避免重复计算
        dic[0], dic[1] = 1, 2
        return self.dp(n - 1, dic)

    def dp(self, n, res):
        if res[n] == -1:
            res[n] = self.dp(n - 1, res) + self.dp(n - 2, res)
        return res[n]

"""
采用hash表 好处在于不需要一开始定义数组
"""
class Solution0(object):
    # Top down + memorization (dictionary)
    def __init__(self):
        self.dic = {1: 1, 2: 2}


    def climbStairs(self, n):
        if n not in self.dic:
            self.dic[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.dic[n]

"""
生成式解法 列表推导
Bottom up, O(n) space
"""

def climbStairs2(self, n):
    if n == 1:
        return 1
    res = [0 for i in range(n)]
    res[0], res[1] = 1, 2
    for i in range(2, n):
        res[i] = res[i - 1] + res[i - 2]
    return res[-1]


# Bottom up, constant space
def climbStairs3(self, n):
    if n == 1:
        return 1
    a, b = 1, 2
    for i in range(2, n):
        a, b = b, a + b
    return b

