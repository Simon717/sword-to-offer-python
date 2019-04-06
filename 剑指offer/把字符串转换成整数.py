# -*- coding: utf-8 -*-
"""
   File Name：     把字符串转换成整数
   Description :
   Author :       simon
   date：          19-3-19
"""


# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if not s:
            return 0

        s = list(s)
        for i in s:
            if i not in ['+', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                return 0

        def makenum(s):
            res = 0
            i = 1
            while s:
                tp = s.pop()
                res += i * int(tp) # 使用哈希表实现比较靠谱
                i *= 10
            return res

        if s[0] in ['-', '+']:
            res = 1 if s[0] == '+' else -1
            res *= makenum(s[1:])
        else:
            res = makenum(s)
        return res

"""
改进
"""
class Solution_:
    def StrToInt(self, s):
        # write code here
        if not s:
            return  0

        nums = []
        numbers = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        for i, n in enumerate(s):
            if n in numbers.keys():
                nums.append(n)
            elif i == 0 and n in ['+', '-']:
                continue
            else:
                return 0
        res = 0
        for i in nums:
            res = res * 10 + numbers[i]
        if s[0] == '-':
            return -1 * res
        return res