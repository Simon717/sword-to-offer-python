# -*- coding: utf-8 -*-
"""
   File Name：     312. Burst Balloons
   Description :
   Author :       simon
   date：          19-4-13
"""

"""
思路：
一开始最容易想到的是考虑所有可能的排列数 复杂度过高

之后想到这里面存在重叠的子问题
12 3 和 21 3 处理到3的时候两个情况变成了一种情况 没有必要分开处理
这里就提示我们可以使用dp 或者memo

先区考虑最后一个气球可能的位置 最后一个气球的贡献是最容易计算的 
遍历最后一个气球可能的位置 就可以将问题分成不相干的两个部分 []i[] i表示最后一个气球 
i是最后一个气球 所以在之前的所有步当中 左半部分气球永远不能和右半部分向邻
实现了分治
"""


class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        memo = {}

        def dp(low, high):
            if (low, high) not in memo:
                if low > high:
                    res = 0
                # elif low == high:
                #     res = nums[low-1]*nums[low]*nums[low+1]
                else:
                    res = 0
                    for k in range(low, high + 1):
                        res = max(res, nums[low - 1] * nums[k] * nums[high + 1] + dp(low, k - 1) + dp(k + 1, high))
                memo[(low, high)] = res
            return memo[(low, high)]

        return dp(1, len(nums) - 2)


"""
简单优化 
将hash表换成list 仍然比较慢
"""


class Solution__(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        n = len(nums)
        memo = [[0] * n for i in range(n)]

        def dp(low, high):
            if not memo[low][high]:
                if low > high:
                    res = 0
                # elif low == high:
                #     res = nums[low-1]*nums[low]*nums[low+1]
                else:
                    res = 0
                    for k in range(low, high + 1):
                        res = max(res, nums[low - 1] * nums[k] * nums[high + 1] + dp(low, k - 1) + dp(k + 1, high))
                memo[low][high] = res
            return memo[low][high]

        return dp(1, len(nums) - 2)


"""
学习一下别人的解
"""


class Solution_TB(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        def calculate(i, j):
            if dp[i][j] or j == i + 1:  # in memory or gap < 2
                return dp[i][j]
            coins = 0
            for k in range(i + 1, j):  # find the last balloon
                coins = max(coins, nums[i] * nums[k] * nums[j] + calculate(i, k) + calculate(k, j))
            dp[i][j] = coins
            return coins

        return calculate(0, n - 1)


"""
这是一道典型的 间隔DP问题
dp[i][j]定义为从i到j的区间内能够得到的最大解 k表示最后处理的气球的位置
dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j]) # i < k < j 
可以看出 刷新i的解的时候 用到的k比i大  
必须把中间两区间的解计算出来之后再去计算两区间合并的解 
所以必须将小间隔的解计算出来之后  再区计算大间隔的解
"""


class Solution_BT(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]  # build the complete array
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for gap in range(2, n):  # 必须从小问题开始解决 gap = j - i 其中i j都不在数字区
            for i in range(n - gap):  # 考虑可能的起点
                j = i + gap  # 检查一下 i = n - gap 的时候 j = i + gap = n 满足题意
                for k in range(i + 1, j):  # k in [i+1, j-1]
                    dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])
        return dp[0][n - 1]


class Solution_BT_(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for i in range(n)]

        for gap in range(2, n):  # i j 之间的距离 i， j表示外围边界
            for i in range(n - gap):
                j = i + gap


if __name__ == '__main__':
    print(Solution().maxCoins([3, 1, 5, 8]))
