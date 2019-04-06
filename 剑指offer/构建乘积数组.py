# -*- coding: utf-8 -*-
"""
   File Name：     构建乘积数组
   Description :
   Author :       simon
   date：          19-3-17
"""
"""
尝试举例子 总结规律
"""
# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        p = 1
        B = [1] * len(A)
        for i in range(len(A)):
            B[i] *= p
            p *= A[i]
        p = 1
        for i in range(len(A)-1, -1, -1):
            B[i] *= p
            p *= A[i]
        return B