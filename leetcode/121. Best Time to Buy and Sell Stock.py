# -*- coding: utf-8 -*-
"""
   File Name：     121. Best Time to Buy and Sell Stock
   Description :
   Author :       simon
   date：          19-3-24
"""

"""
股票利润最大化
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        res = maxEndHere = 0 # 截止到当前时间的最大利润
        inP = prices[0] # 买入时候的价钱
        for i in range(1, len(prices)):
            if prices[i] - inP > 0: # 今天卖出 能得到的最大利润
                maxEndHere = prices[i] - inP
            else: # 会亏钱的话 选择放弃交易 考虑今天买入
                inP = prices[i]

            res = max(res, maxEndHere)
        return res

"""
仍然可以看成是连续子序列的优化问题 买入到卖出之间形成一条连线 
maxEndHere 考虑要不要在今天卖出股票 如果卖出能赚的钱是之前的钱加上今天和昨天的差价 

对于从第一天后的每一天i来说：
如果我们在第i天卖出，  则能赚的钱是在第i-1卖能赚到的钱 +（第i天的股价 - 第i-1的股价）
如果我们在第i天不卖出，则当前赚的钱为 0
"""
class Solution_(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        res, max_cur = 0, 0
        for i in range(1, len(prices)):
            max_cur = max(0, max_cur + prices[i] - prices[i - 1])
            res = max(res, max_cur)
        return res

if __name__ == '__main__':
    test = [7,1,5,3,6,4]
    solu = Solution()
    print(solu.maxProfit(test))