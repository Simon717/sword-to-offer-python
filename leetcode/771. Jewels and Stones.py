# -*- coding: utf-8 -*-
"""
   File Name：     771. Jewels and Stones
   Description :
   Author :       simon
   date：          19-4-8
"""

import collections

"""
set 也是hash表
查找时间的O(1)
"""
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        J = set(J) #
        cntS = collections.Counter(S)
        res = 0
        for k in list(cntS.keys()): # O(n)
            if k in J: # O(1)
                res += cntS[k]
        return res
