# -*- coding: utf-8 -*-
"""
   File Name：     139. Word Break
   Description :
   Author :       simon
   date：          19-3-31
"""
"""
递归 大问题化成小问题 
字典中可能存在多个匹配的prefix

对于单词字典进行字数的统计 建立hash表 
key：字符数 values：[str]
"""

# 超时 会有大量重复计算
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        self.flag = False
        dic = {}
        for i in wordDict:
            dic[len(i)] = dic.get(len(i), [])
            dic[len(i)] += [i]

        les = list(dic.keys())

        def helper(s):
            if not s:
                self.flag = True

            for end in les:
                for i in dic[end]:
                    if s[:end] == i:
                        helper(s[end:])

        helper(s)
        return self.flag

"""
DP 解
直觉上看 最小零钱问题很像...
ok[i] tells whether s[:i] can be built.
"""
class Solution_(object):
    def wordBreak(self, s, wordDict):

        ok = [False] * (len(s) + 1)
        ok[0] = True
        for i in range(1, len(s) + 1): # end index
            for j in range(i):         # stt index
                if ok[j] and s[j:i] in wordDict:
                    ok[i] = True
        return ok[-1]

    def wordBreak_(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        ok = [True]
        for i in range(1, len(s)+1): # end index的范围
            ok += [any(ok[j] and s[j:i] in wordDict for j in range(i))]

        return ok[-1]



if __name__ == '__main__':
    s = 'aaabaa'
    wordDict = ["aa", "aaab"]
    print(Solution_().wordBreak(s, wordDict))