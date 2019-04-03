# -*- coding: utf-8 -*-
"""
   File Name：     55. Jump Game
   Description :
   Author :       simon
   date：          19-4-2
"""

"""
纯模拟
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        dp = [False] * (len(nums) + 1)
        dp[1] = True

        for i in range(1, len(nums)): # 理解为坐标向右平移了一位
            if not dp[i]: return False
            for j in range(i+1, min(len(nums)+1, i+nums[i-1]+1)): # 此处重复计算太多 导致超时
                dp[j] = True
            # dp[i:min(len(nums)-1, i+nums[i-1])] = True
        print(dp)
        return dp[-1]

"""
只需要记录我们能够到达的最远index即可
一旦当前index大于最远index 直接return False
"""
class Solution_(object):
    def canJump(self, nums):
        end_index = 0
        for index in range(len(nums)):
            if index > end_index: return False # 一旦当前index超出了我们能够到达的最远index 直接return False
            end_index = max(end_index, index + nums[index])
        return True


if __name__ == '__main__':
    test = [3,2,1,0,4]
    print(Solution_().canJump(test))


