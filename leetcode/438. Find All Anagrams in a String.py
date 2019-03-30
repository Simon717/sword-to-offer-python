# -*- coding: utf-8 -*-
"""
   File Name：     438. Find All Anagrams in a String
   Description :
   Author :       simon
   date：          19-3-25
"""
"""
方法简单粗暴 但是超时
完全不需要一次性计算很多个counter
滑窗counter
"""
from collections import Counter

class Solution(object):
    # def findAnagrams(self, s, p):
    #     """
    #     :type s: str
    #     :type p: str
    #     :rtype: List[int]
    #     """
    #     if not s:
    #         return []
    #
    #     dic_p = Counter(p)
    #
    #     dics_s = []
    #     for i in range(len(s)-len(p)+1):
    #         dics_s.append(Counter(s[i:i+len(p)]))
    #
    #     return [i for i in range(len(dics_s)) if dics_s[i] == dic_p]

    """
    只开辟了两个Counter 没有重复计算
    """
    def findAnagrams(self, s, p):
        if not s:
            return []

        res = []
        cntP = Counter(p)
        cntS = Counter(s[:len(p)-1])
        for i in range(len(p)-1, len(s)):
            cntS[s[i]] += 1
            if cntS == cntP:
               res.append(i-len(p)+1)

            cntS[s[i-len(p)+1]] -= 1
            if not cntS[s[i-len(p) + 1]]: del cntS[s[i-len(p)+1]]
        return res

    #
    # """ 使用滑窗counter """
    # def findAnagrams(self, s, p):
    #     """
    #     :type s: str
    #     :type p: str
    #     :rtype: List[int]
    #     """
    #     res = []
    #     pCounter = Counter(p)
    #     sCounter = Counter(s[:len(p)-1])
    #
    #     for i in range(len(p)-1,len(s)):
    #         sCounter[s[i]] += 1   # include a new char in the window
    #         if sCounter == pCounter:    # This step is O(1), since there are at most 26 English letters
    #             res.append(i-len(p)+1)   # append the starting index
    #
    #         sCounter[s[i-len(p)+1]] -= 1   # decrease the count of oldest char in the window
    #         if sCounter[s[i-len(p)+1]] == 0:
    #             del sCounter[s[i-len(p)+1]]   # remove the count if it is 0
    #     return res

class Solution_(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        dic_p = {}
        for i in p:
            dic_p[i] = dic_p.get(i, 0) + 1 # 一行代码建hash

        res = []
        for i in range(len(s)-len(p)+1):
            if s[i] not in dic_p:
                i += 1
                continue
            tp = {}
            for j in range(i, i+len(p)):
                tp[s[j]] = tp.get(s[j], 0) + 1
            if tp == dic_p:
                res.append(i)
        return res


if __name__ == '__main__':
    test = "cbaebabacd"
    solu = Solution()
    print(solu.findAnagrams(test, 'abc'))
