# -*- coding: utf-8 -*-
"""
   File Name：     49. Group Anagrams
   Description :
   Author :       simon
   date：          19-3-23
"""

"""
一开始不想使用sort
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        def makedic(s):
            res = {}
            for i in s:
                if i not in res:
                    res[i] = 0
                res[i] += 1
            return res

        dics = []
        res = []
        for i, str in enumerate(strs):
            dic = makedic(str)
            if dic not in dics:
                dics.append(dic)
                res.append([i])
            else:
                res[dics.index(dic)].append(i)

        resstr = []
        for x in res:
            tp = []
            for i in x:
                tp.append(strs[i])
            resstr.append(tp)
        return resstr

    def solu(self, strs):
        res = {}
        for s in strs:
            res[sorted(s)] = []

"""
标准解法
sortedStr --> [strs] 
需要这么一个hash表
用python 建立一个默认value是list的hash表
"""


import collections
class Solution_(object):
    def groupAnagrams(self, strs):
        hash = collections.defaultdict(list)  # 新建一个默认value是list的hash表
        for s in strs:
            hash[tuple(sorted(s))].append(s)
        return hash.values()

    def groupAnagrams(self, strs):
        hash = {}
        for str in sorted(strs):
            key = tuple(sorted(str))
            hash[key] = hash.get(key, []) + [str] # 利用get处理新建list的问题
        return hash.values()

test = ["eat", "tea", "tan", "ate", "nat", "bat"]
solu = Solution()
print(solu.groupAnagrams(test))