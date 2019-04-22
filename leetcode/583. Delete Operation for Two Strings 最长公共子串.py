# -*- coding: utf-8 -*-
"""
   File Name：     583. Delete Operation for Two Strings 最长公共子串
   Description :
   Author :       simon
   date：          19-4-13
"""

class Solution:
    def minDistance(self, word1, word2):
        def dp(i, j, sta):
            if i == len(word1) or j == len(word2):
                return 0
            else:
                if sta:
                    return  1 + dp(i + 1, j + 1, 1) if word1[i] == word2[j] else 0
                if word1[i] == word2[j]:
                    res = 1 + dp(i+1, j+1, 1)
                else:
                    res = max(dp(i+1, j, 0), dp(i, j+1, 0))
                return res
        return dp(0,0,0)