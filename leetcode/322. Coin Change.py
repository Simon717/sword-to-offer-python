# -*- coding: utf-8 -*-
"""
   File Name：     322. Coin Change
   Description :
   Author :       simon
   date：          19-3-28
"""


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins = [x for x in coins if x <= amount]

        if not coins or not len(coins):
            if amount: return -1
            return 0

        dp = [amount + 1] * (amount + 1)  # 使用0个硬币 实现[0,...,amount] 这么多种target sum
        dp[0] = 0  # 使用0个硬币实现target sum 0

        for tar in range(min(coins), amount + 1):
            for coin in coins:
                dp[tar] = min(dp[tar], dp[tar - coin] + 1)

        return -1 if dp[-1] == amount + 1 else dp[-1]

"""
修改版
dp函数 输入：target 输出：需要的硬币数
"""


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount + 1] * (amount + 1)  #实现[0,...,amount] 这么多种target sum 需要的硬币数
        dp[0] = 0  # 实现target sum 0 需要0个硬币
        for tar in range(1, amount + 1):
            for coin in coins:
                if coin <= tar:
                    dp[tar] = min(dp[tar], dp[tar - coin] + 1)
        return -1 if dp[-1] == amount + 1 else dp[-1]
