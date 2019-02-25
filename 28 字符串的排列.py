# -*- coding: utf-8 -*-
"""
   File Name：     28 字符串的排列
   Description :
   Author :       YYJ
   date：          2019-02-21
"""

# -*- coding:utf-8 -*-
"""
不通过
"""
class Solution:
    def Permutation(self, ss):
        # write code heres
        ss = [x for x in ss]
        self.res = []
        self.Permu(ss, [])
        return self.res

    def Permu(self, ss, decided):
        if not ss:
            return

        if len(ss) > 1:
            for i, s in enumerate(ss):
                rest = ss[:]
                del rest[i]
                # decided = []
                decided.append(s)
                self.Permu(rest, decided)
        else:
            decided += ss
            self.res.append(decided)
            decided.pop()

class Solution1:
    def Permutation(self, ss):
        if not len(ss):
            return []
        if len(ss) == 1: # 递归到底
            return list(ss)

        charlist = list(ss) # 必须转成list 不然没法使用sort
        charlist.sort() # 目的是让相同元素聚集到一起

        res = []
        for i,s in enumerate(charlist):
            if i and s == charlist[i-1]: # 遇到相同元素需要跳过
                continue
            restPermus = self.Permutation(''.join(charlist[:i]) + ''.join(charlist[i+1:]))
            for restPermu in restPermus:
                res.append(s+restPermu)
        return res


"""
先从一堆字符中找到一个字符作为最终字符中的第一个字符（扣出一个字符） 
计算剩余字符的排列 得到本轮的排列
然后将剩余的字符进行相同的操作 ==> 递归
"""
class Solution0:
    def Permutation(self, ss):
        # write code here
        if not len(ss):
            return []
        if len(ss) == 1:
            return list(ss)

        charList = list(ss)
        charList.sort()
        pStr = [] # 当前子串可能的排列
        for i in range(len(charList)):
            if i > 0 and charList[i] == charList[i-1]: # 目的是让相同的字符串连在一起
                continue
            temp = self.Permutation(''.join(charList[:i])+''.join(charList[i+1:])) # 扣掉中间第i个字符之后 可能的排列
            for j in temp:
                pStr.append(charList[i]+j) # +用于字符串的连接
        return pStr # 当前子串可能的排列

if __name__ == '__main__':
    test = 'aba'
    S = Solution1()
    print(S.Permutation(test))