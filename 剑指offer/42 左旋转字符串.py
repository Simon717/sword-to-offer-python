# -*- coding: utf-8 -*-
"""
   File Name：     42 左旋转字符串
   Description :
   Author :       simon
   date：          19-3-5
"""

# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if not s:
            return ''

        n = n % len(s)
        return s[n:] + s[:n]

if __name__ == '__main__':
    test = 'abc123def'
    solu = Solution()
    print(solu.LeftRotateString(test, 2))