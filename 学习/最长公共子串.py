# -*- coding: utf-8 -*-
"""
   File Name：     最长子串
   Description :
   Author :       simon
   date：          19-4-13
"""

test = 'bab,caba'

s, p = test.strip().split(',')

"""
加上状态码之后反而是错误答案
因为它只去找第一个相同的路径
"""


class Solution:
    def mxcommon(self, s, p):
        def dp(i, j, sta):
            if i == len(s) or j == len(p):
                return 0
            else:
                if sta:
                    return 1 + dp(i + 1, j + 1, 1) if s[i] == p[j] else 0
                if s[i] == p[j]:
                    res = max(1 + dp(i + 1, j + 1, 1), dp(i + 1, j + 1, 0))  # 当前位置+1 and 后面强制连续 or
                else:
                    res = max(dp(i + 1, j, 0), dp(i, j + 1, 0))
                return res

        return dp(0, 0, 0)


class Solution_:
    def mxcommon(self, s, p):
        self.res = 0

        def dp(i, j):
            if i == len(s) or j == len(p):
                return 0
            else:
                if s[i] == p[j]:
                    out = 1 + dp(i + 1, j + 1)
                    self.res = max(self.res, out)
                    return out
                else:
                    return 0

        dp(0, 0)
        return self.res


"""
memo[(i,j)] 存放的是 s[i:] p[j:] 两个字符串的公共子序列
"""


class Solution_fix:
    def LongCommonSubSequence(self, s, p):
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if i == len(s) or j == len(p):
                    res = 0
                else:
                    if s[i] == p[j]:  # 当前两个位置字符相同 先加1 继续考察后面的字符
                        res = 1 + dp(i + 1, j + 1)
                    else:
                        res = max(dp(i + 1, j), dp(i, j + 1))
                memo[(i, j)] = res
            return memo[(i, j)]

        return dp(0, 0)


"""
cache[i][j]表示A[:i] 和 B[:j]的最长公共子序列的长度

如何保证substr的连续性呢？？
"""


class Solution_DP:
    def longestCommonSubsequence(self, s, p):
        if not s or not p:
            return 0

        memo = [[0] * (len(s) + 1) for j in range(len(p) + 1)]

        for i in range(1, len(p) + 1):  # memo的坐标比字符串的大1
            for j in range(1, len(s) + 1):
                if s[j - 1] == p[i - 1]:  # memo的坐标比字符串的大1
                    memo[i][j] = memo[i - 1][j - 1] + 1
                else:
                    memo[i][j] = max(memo[i][j - 1], memo[i - 1][j])

        return memo[-1][-1]

"""
仍然使用了EndHere的思想 因为最长连续子串的终点可以分类讨论
"""
def find_lcsubstr(s1, s2):
    memo = [[0]*(len(s2) + 1) for j in range(len(s1) + 1)]  # 生成0矩阵，为方便后续计算，比字符串长度多了一列
    res = 0  # 最长匹配的长度
    p = 0  # 最长匹配对应在s1中的最后一位
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                memo[i + 1][j + 1] = memo[i][j] + 1
                res = max(res, memo[i+1][j+1])
                if memo[i + 1][j + 1] > res:
                    res = memo[i + 1][j + 1]
                    p = i + 1
    return s1[p - res:p], res  # 返回最长子串及其长度
"""
memo[i][j] 表示s1[:i] s2[:j]的两个子串的公共子串长度 限制条件是当前公共子串是以ij结尾的
使用了EndHere的思想 因为最长连续子串的终点可以分类讨论 假设最长的子串的终点是i i一定在[0,len(s1)]范围内
还记得之前说的连续子序列优化问题 基本上都可以使用endHere的思想吗？
"""
def find_lcsubstr_(s1, s2):
    memo = [[0]*(len(s2) + 1) for j in range(len(s1) + 1)]
    res = 0  # 最长匹配的长度
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                memo[i + 1][j + 1] = memo[i][j] + 1 # 此时ij定义为前一个解的index 其范围就是[0, len(s1)] 写起来简单一点
                res = max(res, memo[i+1][j+1])
    return res


if __name__ == '__main__':
    # s, p = input().strip().split(',')
    s1 = '12abcd12111133333111'
    s2 = '43abcd11111133333123'
    # print(Solution().mxcommon(s1, s2))
    # print(Solution_().mxcommon(s1, s2))
    print(find_lcsubstr(s1, s2))
    print(Solution_fix().LCSubstr(s1, s2))
    print(Solution_DP().longestCommonSubsequence(s1, s2))
    # print(Solution().mxcommon(s, p))
