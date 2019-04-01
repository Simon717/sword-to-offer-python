# -*- coding: utf-8 -*-
"""
   File Name：     560. Subarray Sum Equals K
   Description :
   Author :       simon
   date：          19-3-31
"""


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        queue = []
        cnt = 0
        tp_sum = 0

        for n in nums:
            queue.append(n)
            tp_sum += n
            if tp_sum > k: # 当前和超过了sum 考虑丢掉之前的元素 但是当前sum小的时候 也有可能要丢掉之前的元素 因为元素可能是负的..
                while queue and  tp_sum > k:
                    tp = queue.pop(0)
                    tp_sum -= tp
            if tp_sum == k:
                cnt += 1

        return cnt

"""
正确解法
为了计算sum(i,j) = preSum(j) - preSum(i)    其中：preSum(j) = sum(0, j)
令 sum(i,j) = preSum(j) - preSum(i) = target
当遍历到j的位置 查找 有没有preSum(i) == preSum(j) - target
"""
class Solution_:
    def subarraySum(self, nums, target):
        dic = {0:1} # {preSum: cnt}
        res = preSum = 0
        for n in nums:
            preSum += n
            res += dic.get(preSum - target, 0)l
            dic[preSum] = dic.get(preSum, 0) + 1 # 不存在键值 新建键值 给出默认值
        return res
if __name__ == '__main__':
    print(Solution().subarraySum([1], 0))