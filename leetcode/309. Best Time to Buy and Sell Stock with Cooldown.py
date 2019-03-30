# -*- coding: utf-8 -*-
"""
   File Name：     309. Best Time to Buy and Sell Stock with Cooldown
   Description :
   Author :       simon
   date：          19-3-30
"""
import sys

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        notown = 0
        own = cool = -sys.maxsize
        for p in prices:
            notown, own, cool = max(notown, cool), max(own, notown - p), own + p
            print(notown, own, cool)
        return max(notown, cool)

if __name__ == '__main__':
    test = [ 1,2,3,0,2]
    solu = Solution()
    print(solu.maxProfit(test))