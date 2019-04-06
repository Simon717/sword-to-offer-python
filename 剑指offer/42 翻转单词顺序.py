# -*- coding: utf-8 -*-
"""
   File Name：     42 翻转单词顺序
   Description :
   Author :       simon
   date：          19-3-5
"""

# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        strlist = s.split(' ')
        strlist.reverse()
        return ' '.join(strlist)

if __name__ == '__main__':
    test = 'I am Bee.'
    solu = Solution()
    print(solu.ReverseSentence(test))