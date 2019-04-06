# -*- coding: utf-8 -*-
"""
   File Name：     20 包含min函数的栈
   Description :
   Author :       YYJ
   date：          2019-02-17
"""

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.minStack = [] #设置的同步栈 元素数目和stack一样 对应着当前栈内最小值

    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.minStack or node < self.min():
            self.minStack.append(node)
        else:
            self.minStack.append(self.min())

    def pop(self):
        # write code here
        if not self.stack:
            return
        self.stack.pop(-1)
        self.minStack.pop(-1)

    def top(self):
        # write code here
        return self.stack[-1]

    def min(self):
        # write code here
        return self.minStack[-1]

if __name__ == '__main__':
    S = Solution()
    # S.push(3)
    # S.push(4)
    # S.push(2)
    # S.push(1)
    print(S.min())
    S.pop()
    print(S.min())
    S.pop()
    print(S.min())

