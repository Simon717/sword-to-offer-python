# -*- coding: utf-8 -*-
"""
   File Name：     02 空格替换
   Description :
   Author :       YYJ
   date：          2019-02-12
"""


class Solution2:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s = list(s)
        for i, c in enumerate(s):
            if c == ' ':
                s[i] = '%20'
        return ''.join(s)


# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        return s.replace(' ', '%20')


if __name__ == '__main__':
    solu = Solution()
    print(solu.replaceSpace('We Are Happy'))
    solu2 = Solution2()
    print(solu2.replaceSpace('We Are Happy'))
