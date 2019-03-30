# -*- coding: utf-8 -*-
"""
   File Name：     5. Longest Palindromic Substring
   Description :
   Author :       simon
   date：          19-3-23
"""
"""
DP解
"""
class Solution_DP(object):
    def longestPalindrome(self, s):
        n = len(s)
        maxStr = ''
        DP = [[0]*n for _ in range(n)] # 这么创建二维list 存放 的是实值不是引用
        for i in range(n): # 终点
            for j in range(0, i+1): # 起点
                if  (j+1 > i-1 or DP[j+1][i-1]) and s[j] == s[i]: # j+1 > i-1  包含了两种基本情况 i,i i,i+1
                    DP[j][i] = 1
                if DP[j][i] and i - j + 1 > len(maxStr):
                    maxStr = s[j:i+1]
        return maxStr

"""
中心拓展法
考虑镜像特性 不断尝试对称轴
需要考虑两种情况： 

"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxLen = 0
        maxStr = []

        for i in range(len(s)):
            j = 0
            while i + j < len(s) and i - j >= 0 and s[i + j] == s[i - j]:
                j += 1

            tp_str = s[i - j + 1:i + j]
            tp_len = len(tp_str)
            if tp_len > maxLen:
                maxLen = tp_len
                maxStr = tp_str

            p, q = i, i + 1
            while p >= 0 and q < len(s) and s[p] == s[q]:
                p -= 1
                q += 1

            tp_str = s[p + 1:q]
            tp_len = len(tp_str)
            if tp_len > maxLen:
                maxLen = tp_len
                maxStr = tp_str
        return ''.join(maxStr)

"""
优化版本 
将拓展边界写成函数
"""

class Solution_(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.maxLen = 0
        self.maxStr = ''

        def expandAroundCenter(left, right):
            l, r = left, right
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > self.maxLen:
                self.maxStr = s[l + 1:r]
                self.maxLen = r - l - 1

        for i in range(0, len(s)):
            expandAroundCenter(i, i)
            expandAroundCenter(i, i + 1)
        return self.maxStr

test = 'cbba'
solu = Solution_DP()
print(solu.longestPalindrome(test))

