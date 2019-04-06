# -*- coding: utf-8 -*-
"""
   File Name：     21 栈的压入、弹出序列
   Description :
   Author :       YYJ
   date：          2019-02-17
"""

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.aux = []

    def IsPopOrder(self, pushV, popV):
        # write code here
        for i in pushV: # 模拟进栈
            self.aux.append(i)
            if i == popV[0]: #尝试弹出当前元素
                self.aux.pop()
                del popV[0]
        # 进栈完成 只剩下出栈
        # popV.reverse()
        # res = True if popV == self.aux else False
        return popV[::-1] == self.aux

if __name__ == '__main__':
    solu = Solution()
    pushV = [1, 2, 3, 4, 5]
    popV = [4, 5, 3, 2, 1]
    popVF = [4, 5, 2, 1, 3]
    print(solu.IsPopOrder(pushV, popVF))
