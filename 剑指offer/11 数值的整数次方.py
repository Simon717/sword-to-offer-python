# -*- coding: utf-8 -*-
"""
   File Name：     11 数值的整数次方
   Description :
   Author :       YYJ
   date：          2019-02-15
"""

# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        if exponent == -1:
            return 1./base

        res = self.Power(base, exponent >> 1)
        res *= res
        if (exponent & 0x1) == 1:
        # if exponent % 2:
            res *= base
        return res


if __name__ == '__main__':
    solu = Solution()
    print(solu.Power(0,-2))