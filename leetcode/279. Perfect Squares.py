# -*- coding: utf-8 -*-
"""
   File Name：     279. Perfect Squares
   Description :
   Author :       simon
   date：          19-3-31
"""

"""
拼命去想当前这个target sum 跟之前的target sum有什么关系 
能不能考虑最后一个方块具体是啥 这样就可以跟之前的解有关系
dp[i] = min(dp[i], dp[i - j**2] + 1)
"""
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [0] * (n + 1) # target sum [0, n] 所以是n+1个数
        for i in range(n+1):
            dp[i] = i
            for j in range(1, int(i**0.5)+1):
                dp[i] = min(dp[i], 1 + dp[i - j ** 2])
        return dp[-1]



if __name__ == '__main__':
    print(Solution().numSquares(12))

