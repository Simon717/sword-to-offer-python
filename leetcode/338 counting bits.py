# -*- coding: utf-8 -*-
"""
   File Name：     338 counting bits
   Description :
   Author :       simon
   date：          19-3-9
"""


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if not num:
            return [0]

        n = 0
        num += 1
        while not 2 ** n > num:
            n += 1
        n -= 1
        res = self.helper(2**n)
        left = [x + 1 for x in res[:num - 2 ** n]]
        return res + left

    def helper(self, num):
        if num == 2:
            return [0, 1]
        left = self.helper(num // 2)
        right = [x + 1 for x in left]
        return left + right

class Solution0(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]
        while len(res) <= num:
            res += [i+1 for i in res] # 批量添加 很骚
        return res[:num+1]

if __name__ == '__main__':
    test = 3
    solu = Solution()
    print(solu.countBits(test))