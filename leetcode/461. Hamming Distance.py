# -*- coding: utf-8 -*-
"""
   File Name：     461. Hamming Distance
   Description :
   Author :       simon
   date：          19-4-8
"""


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        tp = x ^ y
        cnt = 0
        while tp:
            cnt += tp & 1
            tp = tp >> 1
        return cnt


"""
利用字符串性质
"""


class Solution_(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return str(bin(x ^ y)).count('1')
