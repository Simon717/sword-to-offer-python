# -*- coding: utf-8 -*-
"""
   File Name：     448. Find All Numbers Disappeared in an Array
   Description :
   Author :       simon
   date：          19-3-24
"""

"""
关键信息： 1 ≤ a[i] ≤ n (n = size of array)
思路一：不断交换数字直到有些index上面的数字不等于index+1
"""
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res = []

        for i in range(len(nums)):
            while nums[i] != i + 1 and nums[nums[i]-1] != nums[i]:
                rightIndex = nums[i] - 1
                nums[i], nums[rightIndex] = nums[rightIndex], nums[i]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res.append(i + 1)
        return res

"""
直接使用hash表进行计数
使用list模拟定长的hash表
"""
def findDisappearedNumbers(self, nums):
    hash = [0] * (len(nums)+1) # 直接理解为确定keys的hash表 + 1因为是数字是从1开始的
    for n in nums:
        hash[n] += 1
    return [n for n in range(1, len(hash)) if hash[n] == 0]

"""
使用python的set去重
"""
class Solution_(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return list(set(range(1,len(nums)+1)) - set(nums))

if __name__ == '__main__':
    test = [4,3,2,7,8,2,3,1]
    solu = Solution()
    print(solu.findDisappearedNumbers(test))