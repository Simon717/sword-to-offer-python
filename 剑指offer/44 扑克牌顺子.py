# -*- coding: utf-8 -*-
"""
   File Name：     44 扑克牌顺子
   Description :
   Author :       simon
   date：          19-3-5
"""

# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if len(numbers) != 5:
            return False

        # for i in range(len(numbers)): # 如果需要转换数字 使用哈希表进行转换
        #     if numbers[i] == 1:
        #         numbers[i] = 14
        #     if numbers[i] == 2:
        #         numbers[i] = 15

        numbers.sort()
        cnt = 0
        for num in numbers:
            if not num:
                cnt += 1

        if cnt == 1:
            return True
        else:
            same = self.isSame(numbers[cnt:]) # 考虑重复元素
            if same:
                return False
            if self.computeDist(numbers[cnt:]) <= cnt: #计算间隔之和
                return True
            else:
                return False


    def computeDist(self, nums):
        res = 0
        for i in range(len(nums)-1):
            res += nums[i+1] - nums[i] - 1
        return res

    def isSame(self, nums):
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False


if __name__ == '__main__':
    test = [1,3,2,6,4]
    solu = Solution()
    print(solu.IsContinuous(test))