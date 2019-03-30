# -*- coding: utf-8 -*-
"""
   File Name：     494. Target Sum
   Description :
   Author :       simon
   date：          19-3-26
"""

"""
基于 416 

集合可以分成两个子集 一部分是正 一部分是负
问题可以转化成 找到一个sum=target的子集
之前是two sum 而且是有序数组 现在不确定子集数目 并且数组未排序

f(i,j) = f(i-1,j) + f(i-1, j-num) 
         no pick     pick num
其中 i in [0, len(nums)] 表示使用数组的一个数一直到使用N个数
j 表示当前的目标数字 [0, target] 表示目标和从0开始一直到真正的target
- num 表示当前考察到的数组中的数 要还是不要这个数 对应了两种选择
"""
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums or not len(nums):
            return 1 if not S else 0

        if sum(nums) < S or ((sum(nums)+S) % 2 ):
            return 0

        target = (sum(nums)+S) // 2

        dp = [0] * (target + 1) # 对应这 i=0 这一行的结果 也就是使用空集 实现 target sum 空集可以使得target = 0  其他target不能实现所以全是0
        dp[0] = 1

        for num in nums: # 使用数组中的第一个数 --> 使用到数组中的所有数
            for tar in range(target, num-1, -1): # index range [target, num]
                dp[tar] += dp[tar - num]
        # print(dp)
        return dp[-1]

if __name__ == '__main__':
    solu = Solution()
    print(solu.findTargetSumWays([1,1,1,1,1], 3))