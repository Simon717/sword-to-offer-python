# -*- coding: utf-8 -*-
"""
   File Name：     647. Palindromic Substrings
   Description :
   Author :       simon
   date：          19-3-12
"""

"""
考虑每一个可能的对称轴 共有2N-1个可能的点（包含两个index的中点）
"""
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        cnt = 0
        s = list(s)
        N = len(s)
        for i in range(2 * N - 1):
            p1 = i // 2
            p2 = p1 + i % 2
            while (p1 >= 0 and p2 < len(s)):
                if s[p1] == s[p2]:
                    cnt += 1
                    p1 -= 1
                    p2 += 1
                else:
                    break
        return cnt