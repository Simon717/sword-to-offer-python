# -*- coding: utf-8 -*-
"""
   File Name：     309. Best Time to Buy and Sell Stock with Cooldown
   Description :
   Author :       simon
   date：          19-3-30
"""
import sys

"""
own = max(own, cool-p)
cool = max(cool, notown+p)
notown = own + p  # 特指卖掉股票的后一天

关于如何定义初始解：有些时候需要定义dp[-1] -1表示的是递推开始的前一个解 不代表python的最后一个的意思
dp[-1]的设置只需要让dp[0]复合实际情况即可
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cool =  not_own = 0
        own  = -float('inf')
        for p in prices:
            cool, own, not_own = max(cool, not_own), max(own, cool - p), own + p
            # print(cool, own, not_own)
        return max(cool, not_own)

"""
为什么会自然的想到这种解法？
因为在每一个位置都有三种可能 但是小偷问题类似 到某一家可以选择偷或者不偷这一家
"""
class Solution_(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = [0] * len(prices)
        sell = [0] * len(prices)
        cool = [0] * len(prices)
        buy[0] = -prices[0]
        for i in range(1, len(prices)):
            buy[i] = max(buy[i - 1], cool[i - 1] - prices[i])
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
            cool[i] = max(cool[i - 1], buy[i - 1], sell[i - 1])
        print(sell, cool)
        return max(sell[-1], cool[-1])

"""
own 代表持有股票 not own代表空仓 
own[i] = max(own[i-1], not_own[i-2] - p)
not_own[i] = max(not_own[i-1], own[i-1] + p)
"""
class Solution__(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        prev_not_own = not_own = 0
        own = -float('inf')
        for p in prices:
            prev_own = own
            own = max(own, prev_not_own - p)
            prev_not_own, not_own = not_own, max(not_own, prev_own + p)
        return max(not_own, own)

if __name__ == '__main__':
    test = [1, 2, 3, 0, 2]
    solu = Solution__()
    print(solu.maxProfit(test))

    solu = Solution()
    print(solu.maxProfit(test))