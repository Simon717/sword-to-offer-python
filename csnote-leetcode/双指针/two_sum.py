# -*- coding: utf-8 -*-
class ma:
    pass

"""
two sum
经典双指针问题 
精髓： 初始化首尾指针是的搜索方向单向 
 舍弃很多不可能的解 减小解空间
"""
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        p1, p2 = 0, len(numbers)-1
        while p1 < p2:
            sum = numbers[p1] + numbers[p2]
            if sum == target:
                return p1+1, p2+1
            if sum < target:
                p1 += 1
            else:
                p2 -= 1
        return