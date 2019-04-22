# -*- coding: utf-8 -*-
"""
   File Name：     198. House Robber
   Description :
   Author :       simon
   date：          19-3-24
"""

"""
dp[i]代表只偷到第i家的maximum amount of money
状态转移方程:
dp[i] = max(dp[i-1], dp[i-2] + nums[i]) 
空间可以优化到O(1)
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        DP = [0] * len(nums)
        DP[0] = nums[0]
        DP[1] = max(nums[:2])
        for i in range(2, len(nums)):
            DP[i] = max(DP[i - 1], nums[i] + DP[i - 2])
        return DP[-1]


"""
其实就是上面解法的空间优化版本
"""


class Solution_(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev, cur = 0, 0  # dp[i-2] dp[i-1]
        for num in nums:
            # tp = prev
            # prev = cur
            # cur = max(cur, tp+num)
            prev, cur = cur, max(cur, prev + num)
        return cur


"""
思路 1 ******- 时间复杂度: O(N)******- 空间复杂度: O(N)******

dp[i][0]代表偷到第i家，并且不偷第i家的最大收益
dp[i][1]代表偷到第i家，并且偷第i家的最大收益
"""


class Solution__:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        # dp = [[0] * 2 for i in range(len(nums))]
        # dp[0][1] = nums[0]
        #
        #
        # for i in range(1, len(nums)):
        #     dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
        #     dp[i][1] = dp[i - 1][0] + nums[i]

        pick = [0] * len(nums)
        pick[0] = nums[0]
        nopick = [0] * len(nums)
        for i in range(1, len(nums)):
            pick[i] = nopick[i - 1] + nums[i]
            nopick[i] = max(pick[i - 1], nopick[i - 1])

        return max(pick[-1], nopick[-1])


"""
递归 + memo 
此时 dp(i) 定义为 从第一家偷到第i家


"""


class Solution_rec(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = {-1:0}

        def dp(n):
            if n not in memo:
                if n == 0:
                    res = nums[0]
                elif n == 1:
                    res = max(nums[:2])
                else:
                    res = max(dp(n - 1), nums[n] + dp(n - 2))
                memo[n] = res
            return memo[n]

        return dp(len(nums) - 1)


if __name__ == '__main__':
    test = [2, 7, 9, 3, 1]
    # test = [1,2,3,1]
    solu = Solution()
    print(solu.rob(test))
    print(Solution_rec().rob(test))
