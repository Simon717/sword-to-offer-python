# -*- coding: utf-8 -*-
"""
   File Name：     表示数值的字符串
   Description :
   Author :       simon
   date：          19-3-22
"""
# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        s = list(s)
        i = 0
        if s[i] in ['+', '-']:
            i += 1

        while i < len(s) and ord('0') <= ord(s[i]) <= ord('9'):
            i += 1

        if i < len(s) and s[i] == '.':
            i += 1
            while i < len(s) and ord('0') <= ord(s[i]) <= ord('9'):
                i += 1

        if i < len(s) and s[i] in ['e', 'E']:
            i += 1
            if i == len(s): return False  # 如果现在就结束
            if s[i] in ['+', '-']:
                i += 1
            while i < len(s) and ord('0') <= ord(s[i]) <= ord('9'):
                i += 1

        return i == len(s)


test = '123.45e+6'
solu = Solution()
print(solu.isNumeric(test))
