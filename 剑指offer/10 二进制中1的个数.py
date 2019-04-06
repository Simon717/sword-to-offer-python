# -*- coding: utf-8 -*-
"""
   File Name：     10 二进制中1的个数
   Description :
   Author :       YYJ
   date：          2019-02-15
"""
# -*- coding:utf-8 -*-
class Solution:
    # def NumberOf1(self, n):
    #     # write code here
    #     count = 0
    #     if n < 0: # 获得负数的补码转化为一个正数
    #         n = n & 0xffffffff
    #     while n: # 只要n不为0 就必然存在1
    #         count += 1
    #         n = (n - 1) & n
    #     return count
    #
    def NumberOf1(self, n):
        # n = n & 0xffffffff if n < 0 else n
        cnt = 0
        # while n:
        for i in range(3):
            n = n & (n-1)
            print(bin(n))
            cnt += 1
        return cnt



if __name__ == '__main__':
    solu = Solution()
    print(solu.NumberOf1(-1))