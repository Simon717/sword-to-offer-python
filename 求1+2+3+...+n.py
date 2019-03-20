# -*- coding: utf-8 -*-
"""
   File Name：     求1+2+3+...+n
   Description :
   Author :       simon
   date：          19-3-20
"""


# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        if n == 1:
            return 1

        return n + self.Sum_Solution(n-1)

test = 10
solu = Solution()
print(solu.Sum_Solution(10))