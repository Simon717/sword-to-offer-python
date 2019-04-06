# -*- coding: utf-8 -*-
"""
   File Name：     33 把数组排成最小的数
   Description :
   Author :       simon
   date：          19-2-24
"""
from functools import cmp_to_key
# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return
        # numstr = list(map(lambda x: str(x), numbers)) # 定义变换F 输入x
        numstr = list(map(str, numbers)) # 定义变换F 以及输入x
        numstr.sort(key=cmp_to_key(lambda x,y: int(x+y) - int(y+x))) # 使用Python内置函数实现排序
        # for i in range(len(numstr)): # 因为这是利用两两比较进行排序的算法 所以冒泡排序很适合
        #     for j in range(len(numstr)-i-1):
        #         if self.cmp(numstr[j], numstr[j+1]):
        #             numstr[j], numstr[j+1] = numstr[j+1], numstr[j]
        return ''.join(numstr)

    def cmp(self, x, y):
        return int(x+y) - int(y+x)


if __name__ == '__main__':
    test = [3, 32, 321]
    solu = Solution()
    print(solu.PrintMinNumber(test))