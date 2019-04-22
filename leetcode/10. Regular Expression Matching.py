# -*- coding: utf-8 -*-
"""
   File Name：     10. Regular Expression Matching
   Description :
   Author :       simon
   date：          19-4-12
"""

"""
递归 + memo 
爽的一批

自顶向下
为什么是自顶向下 因为当前的解依赖于未来的解 
dp（i,j）意味着 s[i:] 和 p[j:] 之间的匹配情况
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = {}

        def dp(i, j):
            if i == len(s) and j == len(p):  # 00
                res = True
            elif i != len(s) and j == len(p):  # 10
                res = False
            else:  # 01 11
                if (i, j) in memo:
                    res = memo[(i, j)]
                else:
                    if j < len(p) - 1 and p[j + 1] == '*':
                        if i < len(s) and p[j] in ['.', s[i]]:
                            res = dp(i, j + 2) or dp(i + 1, j)
                        else:
                            res = dp(i, j + 2)
                    elif i < len(s) and p[j] in ['.', s[i]]:
                        res = dp(i + 1, j + 1)
                    else:
                        res = False

            memo[(i, j)] = res
            return res

        return dp(0, 0)

class Solution_(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if i == len(s) and j == len(p):  # 00
                    res = True
                elif i != len(s) and j == len(p):  # 10
                    res = False
                else:  # 01 11
                    if j < len(p) - 1 and p[j + 1] == '*':
                        if i < len(s) and p[j] in ['.', s[i]]:
                            res = dp(i, j + 2) or dp(i + 1, j)
                        else:
                            res = dp(i, j + 2)
                    elif i < len(s) and p[j] in ['.', s[i]]:
                        res = dp(i + 1, j + 1)
                    else:
                        res = False

                memo[(i, j)] = res
            return memo[(i, j)]

        return dp(0, 0)

if __name__ == '__main__':
    print(Solution().isMatch("aab", "c*a*b"))
