# -*- coding: utf-8 -*-
"""
   File Name：     53. Maximum Subarray
   Description :
   Author :       simon
   date：          19-3-15
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if max(nums) < 0:
            return max(nums)

        maxsum = S = 0
        for i in range(len(nums)):
            S += nums[i]
            maxsum = max(maxsum, S)
            if S < 0:
                S = 0

        return maxsum

"""
好好看看
动态规划
"""
class Solution_fast(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        curSum = 0
        for val in nums:
            curSum = val + curSum
            if curSum > res:
                res = curSum
            if curSum < 0:
                curSum = 0
        return res
"""
下面两种解法是通解 动态规划
子问题定义为 F(A, i) 表示为A[0:i]（前闭后闭）中包含A[i]的最优解
最终问题（A[0:N]中的最优解）的解是子问题解中的最大值

"""
class Solution_DP(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        DP = [nums[0]] * N # DP[i] 表示nums[:i+1]中包含nums[i]的最优解
        for i in range(1, N):
            DP[i] = max(DP[i - 1] + nums[i], nums[i])
        return max(DP)

"""
maxSubArray(A, i) = A[i] + maxSubArray(A, i - 1) if maxSubArray(A, i - 1) else 0; 
"""
class Solution_DP_(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = maxEndingHere = nums[0]
        for i in range(1, len(nums)):
            maxEndingHere = max(maxEndingHere + nums[i], nums[i]) # maxEnd 定义为包含当前元素的最优解
            res = max(res, maxEndingHere)
        return res

    """
    注意这种连续子序列的优化问题
    遍历
    第一步：找到包含当前节点的局部最优解 maxEndHere
    第二步：刷新全局最优解 res
    """
    def maxLenStr(self, s):
        if not s: return ''
        res = maxEndHere = s[0]
        for i in range(1, len(s)):
            maxEndHere = (maxEndHere if ord(maxEndHere[-1]) + 1 == ord(s[i]) else '') + s[i] # 这里的括号必不可少
            res = maxEndHere if len(maxEndHere) > len(res) else res
        return res


if __name__ == '__main__':
    test = [-2,1,-3,4,-1,2,1,-5,4]
    teststr = 'abcefghkk'
    solu = Solution_DP_()
    # print(solu.maxSubArray(test))
    print(solu.maxLenStr(teststr))