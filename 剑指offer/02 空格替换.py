# -*- coding: utf-8 -*-
"""
   File Name：     02 空格替换
   Description :
   Author :       YYJ
   date：          2019-02-12
"""

# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        return s.replace(' ', '%20')

if __name__ == '__main__':
    solu = Solution()
    print(solu.replaceSpace('We Are Happy'))