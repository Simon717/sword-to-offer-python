# -*- coding: utf-8 -*-
"""
   File Name：     152. Maximum Product Subarray
   Description :
   Author :       simon
   date：          19-4-7
"""

"""
简单的存下所有的连续乘积结果
"""
import sys


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        init = -sys.maxsize
        dp = [[init] * len(nums) for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][i] = nums[i]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                dp[i][j] = dp[i][j - 1] * nums[j]
        return max(max(x) for x in dp)


"""
maxendhere 
全局最大 res
正数最大 pos
负数最大 neg
"""


class Solution_(object):
    def maxProduct(self, nums):
        res, pos, neg = -sys.maxsize, -1, 1
        for n in nums:
            if n > 0:
                pos = pos * n if pos > 0 else n
                neg = neg * n if neg < 0 else neg
            elif n < 0:
                pos = neg * n if neg < 0 else -1
                neg = pos * n if pos > 0 else n
            else:
                pos, neg = -1, 1
            res = max(res, pos)
        return res

    """
    DP 问题先写DP方程
    维护当前正数最大 维护当前负数最大
    dp(i) = max(dp(i-1)*n, n) 尝试将n加入到乘积序列中 也可以另起炉灶
    """

    def maxProduct_(self, nums):
        res = pos = neg = nums[0] # 考虑初始解 只需要考虑当输出只有一个数的时候
        for n in nums[1:]:
            prev_pos = pos
            pos = max(n, n * pos, n * neg)
            neg = min(n, n * prev_pos, n * neg)
            res = max(res, pos)
        return res


class Solution__(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxdp = [nums[0]] * len(nums)
        mindp = [nums[0]] * len(nums)

        for i in range(1, len(nums)):
            maxdp[i] = max(mindp[i - 1] * nums[i], maxdp[i - 1] * nums[i], nums[i])
            mindp[i] = min(maxdp[i - 1] * nums[i], mindp[i - 1] * nums[i], nums[i])
        print(maxdp)

        return max(maxdp)


if __name__ == '__main__':
    solu = Solution_()
    print(solu.maxProduct_([2, 3, -2, 4, -3]))

    solu = Solution__()
    print(solu.maxProduct([2, 3, -2, 4, -3]))
