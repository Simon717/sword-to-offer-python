# -*- coding: utf-8 -*-
"""
   File Name：     416. Partition Equal Subset Sum
   Description :
   Author :       simon
   date：          19-3-26
"""

"""
transition function is dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]  # 此处nums[1]表示使用数组中第一个数也就是nums[0]  实际对应到代码上应该是nums[i-1]
其中i代表使用数组中的前i个数(0, len(nums)) j代表目标和 (0~tar) 全部是前闭后闭区间
    第一行表示使用数组中0个数 第二行表示使用数组中一个数
注意到当前行的解只和上一行有关系 所以只需要一行的空间就可以

特别注意：
内层循环的顺序是从右往左刷新 因为我们刷新j位置的时候 用到了j位置左边的解 
保证左边的解的更新慢与右边 这样就可以保证到我们拿到上一轮次的解
"""
"""
使用二维空间
"""
class Solution(object):
    def canPartition(self, nums):
        if not nums or len(nums) == 0:
            return True # 注意 这里是TRue

        if sum(nums) % 2 != 0:
            return False

        tar = sum(nums) // 2

        dp = [[False]*(tar+1) for _ in range(len(nums)+1)]

        for i in range(1, len(nums)+1):
            dp[i][0] = True

        dp[0][0] = True

        for i in range(1, len(nums)+1):
            for j in range(nums[i-1], tar+1):
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
        return dp[-1][-1]

"""
空间优化到一维 
时间也缩短接近一半
代码也更加简洁...
"""

class Solution_(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) == 0:
            return True # 注意 这里是TRue

        if sum(nums) % 2 != 0:
            return False

        tar = sum(nums) // 2

        dp = [False]* (tar + 1) # 因为目标和是从0开始直到tar 数目是tar+1
        dp[0] = True

        for num in nums: # 为啥不用+1 因为第一轮的解在初始化dp数组的时候已经确定了 所以只需要往后更新len(nums)即可 这里是从第二轮开始循环
            for j in range(tar, num-1, -1):  # 从tar 到 num 倒序刷新dp数组是为了保证拿到的是上一轮的解
                dp[j] = dp[j] or dp[j - num] # 为啥是这样呢？ 因为我们刷新j位置的时候 用到了j位置左边的解 我们必须保证左边的解的更新慢与右边 这样就可以保证到我们拿到上一轮次的解
        return dp[-1]

if __name__ == '__main__':
    solu = Solution()
    print(solu.canPartition([1,5,5,11]))