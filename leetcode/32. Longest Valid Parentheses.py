# -*- coding: utf-8 -*-
"""
   File Name：     32. Longest Valid Parentheses
   Description :
   Author :       simon
   date：          19-4-10
"""

"""
f(i,j) = f(i+1, j-1) or f(i+2, j) or f(i, j-2) 
"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                if s[i] == '(' and s[j] == ')' and (j - i == 1 or dp[i + 1][j - 1] == True):
                    # print(i+1, j-1)
                    dp[i][j] = True
                # elif s[i] == '(' and s[j] == ')' and dp[i+1][j-1]: dp[i][j] = True
                elif s[i:i + 2] == '()' and dp[i + 2][j]:
                    dp[i][j] = True
                elif s[j - 1:j + 1] == '()' and j > 2 and dp[i][j - 2]:
                    dp[i][j] = True
                if dp[i][j]:
                    res = max(res, j - i)
                    # print(s[i:j])
        # print(dp)
        return res + 1

    def longestValidParentheses_(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = 0
        for i in range(n, -1, -1):
            for j in range(i + 1, n):
                if s[i] == '(' and s[j] == ')' and (j - i == 1 or dp[i + 1][j - 1] == True):
                    # print(i+1, j-1)
                    dp[i][j] = True
                # elif s[i] == '(' and s[j] == ')' and dp[i+1][j-1]: dp[i][j] = True
                # elif s[i:i+2] == '()' and dp[i+2][j]: dp[i][j] = True
                elif dp[i][i + 1] and dp[i + 2][j]:
                    dp[i][j] = True
                # elif s[j-1:j+1] == '()' and j>2 and dp[i][j-2]: dp[i][j] = True
                elif dp[j - 1][j] == '()' and j > 2 and dp[i][j - 2]:
                    dp[i][j] = True
                if dp[i][j]:
                    res = max(res, j - i + 1)
                    # print(s[i:j])
        # print(dp)
        return res


"""
只寻找子序列的最优解
考虑O(n)的算法 最优解的末尾index必然在[0,1,...,n]
考虑maxendhere

if a[i] == ')' 合法末尾必然是')'
    if `a[i-1] == '(' f[i] = f[i-2] + 2
    if 'a[i-1] == ')' and a[i - f[i-1] - 1] == '(' f[i] = f[i-1] + 2 + f[i - f[i-1] - 2]
"""


class Solution_(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2

                elif s[i - 1] == ')' and i - dp[i - 1] - 1 >=0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i-1] + 2 + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] - 2 > 0 else 0)
        print(dp)
        return max(dp)

class Solution__(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        dp = [0 for i in range(len(s))]
        for i in range(1, len(s)):
            if s[i] == ')':
                left = i - 1 - dp[i-1]
                if left >= 0 and s[left] == '(':
                    dp[i] = dp[i-1] + 2
                    if left > 0: # 这个是判断 left 前面是否能与后面继续连起来
                        dp[i] += dp[left-1]
        return max(dp)

    """
    还是maxEndHere的思想 考虑了最优解所有可能的结尾index
    
    """
    def longestValidParentheses_(self, s):
        if len(s) == 0:
            return 0
        stack = [-1] # 标记起始位置
        res = 0
        for i, x in enumerate(s):
            if x == '(':
                stack.append(i)
            if x == ')':
                stack.pop() # 弹出左括号和无法配对的右括号
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res



if __name__ == '__main__':
    test = "(()))())("
    print(Solution__().longestValidParentheses_(test))
