# -*- coding: utf-8 -*-
"""
   File Name：     京东回文
   Description :
   Author :       simon
   date：          19-4-12
"""

class Solution:
    # 找到end with end的最大回文串
    def huiwen(self, s):
        res = 1
        for i in range(len(s)):
            if s[i:] == s[i:][::-1]:
                # res = max(res, len(s)-i)
                res = len(s) - i
                break
        return res + 2*(len(s)-res)

if __name__ == '__main__':
    s = input().strip()
    print(Solution().huiwen(s))
