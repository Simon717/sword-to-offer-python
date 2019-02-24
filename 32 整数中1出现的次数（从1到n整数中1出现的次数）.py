# -*- coding: utf-8 -*-
"""
   File Name：     32 整数中1出现的次数（从1到n整数中1出现的次数）
   Description :
   Author :       simon
   date：          19-2-23
"""

# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        ones, num = 0, 1  # i 表示 1 10 100
        while n >= num:
            a, b = n // num, n % num  # 按照数位进行分割
            ones += a // 10 * num + (a % 10 == 1) * (b + 1) + ((a // 10) >= 2) * num
            num *= 10
        return ones


if __name__ == '__main__':
    test = 1
    solu = Solution()
    print(solu.NumberOf1Between1AndN_Solution(test))
