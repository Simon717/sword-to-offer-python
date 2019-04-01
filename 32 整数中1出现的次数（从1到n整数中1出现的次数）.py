# -*- coding: utf-8 -*-
"""
   File Name：     32 整数中1出现的次数（从1到n整数中1出现的次数）
   Description :
   Author :       simon
   date：          19-2-23
"""

# -*- coding:utf-8 -*-
class Solution:
    # def NumberOf1Between1AndN_Solution(self, n):
    #     # write code here
    #     ones, num = 0, 1  # i 表示 1 10 100
    #     while n >= num:
    #         a, b = n // num, n % num  # 按照数位进行分割
    #         ones += a // 10 * num + (a % 10 == 1) * (b + 1) + ((a // 10) >= 2) * num
    #         num *= 10
    #     return ones

    """
    直观解法:  
    还是有bug
    思路是对与数据不断的分段

    每一次都干掉当前的数位 555 第一轮处理 [0 ~ 499] 剩下 [500 ~ 555] 等价于 [0～55] 接下来就是怎么处理[0 ~ 499] 继续分段 [0 ~ 99] [100 ~ 199] [200 ~ 499] 总结规律即可
    111 [0 ~ 99] 剩下 [100 ~ 111] 能不能等价于 [1 ~ 11] 不能 高位1 对于低位有影响 在干掉高位1之前考虑其对低位的影响  [100 ~ 111] 高位1出现了 11+1次
    在干掉1之前需要加上这12
    """
    def NumberOf1Between1AndN_Solution_(self, n):
        self.res = 0
        def helper(s):
            if not s:
                return

            k = len(s)
            num = int(s[0])  # 得到当前位的数字

            if num == 0: return

            if k == 1: # 处理到个位
                self.res += (1 if int(s) >= 1 else 0)
                return

            if num >= 2:
                self.res += (num-1) * (k - 1) * 10 ** (k-2) + 10 ** (k-1) # [100 ~ 199]: 10 ** (k-1)        [200 ~ 299]:(num-1) * (k - 1) * 10 ** (k-2)
            else:
                self.res += int(s[1:]) + 1 # 需要考虑高位1可能对低位的影响
            self.res += (k - 1) * 10 ** (k-2) # 公共段： [0 99]:(k - 1) * 10 ** (k-2)
            return helper(s[1:]) # 此时可以抛弃当前位 只需要管低位
        helper(str(n))
        return self.res


# -*- coding:utf-8 -*-
class Solution__:
    def NumberOf1Between1AndN_Solution(self, n):
        ones, m = 0, 1
        while m <= n:
            ones += (n // m + 8) // 10 * m + (n // m % 10 == 1) * (n % m + 1)
            m *= 10
        return ones

    def NumberOf1Between1AndN2(self, n):
        ones, m = 0, 1
        while m <= n:
            if ((n // m) % 10) != 0 and ((n // m) % 10) != 1:
                ones += (n // 10 // m + 1) * m
            elif ((n // m) % 10) == 1:
                ones += (n // m // 10) * m + n % m + 1
            m *= 10
        return ones



if __name__ == '__main__':
    test = 10
    solu = Solution()
    print(solu.NumberOf1Between1AndN_Solution_(test))
    print(Solution().NumberOf1Between1AndN_Solution(test))

    s = Solution__()
    print(s.NumberOf1Between1AndN_Solution(test))
    # print(s.NumberOf1Between1AndN2(test))
