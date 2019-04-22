# -*- coding: utf-8 -*-
"""
   File Name：     07 用两个栈实现队列
   Description :
   Author :       YYJ
   date：          2019-02-12
"""
# -*- coding:utf-8 -*-
"""
栈1 栈2 有着先后顺序
栈1 进入栈
栈2 弹出栈
弹出元素的时候 栈2有值的情况下直接弹出 因为栈2中的元素永远比栈1的元素先进入队列
当栈2没有元素就把栈1中的元素全部翻转放到栈2中
"""


class Solution2:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # write code here
        self.stack1.append(node)

    def pop(self):
        # return xx
        if not self.stack1 and not self.stack2:
            return
        elif self.stack2:
            return self.stack2.pop()
        else:
            self.stack2 = self.stack1[::-1]
            self.stack1 = []
            return self.stack2.pop()


class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # write code here
        self.stack1.append(node)

    def pop(self):
        # return xx
        if not self.stack1 and not self.stack2:
            return
        if self.stack2:
            return self.stack2.pop()
        else:
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()


if __name__ == '__main__':
    queue = Solution()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.pop()
    queue.push(4)
    print(queue.stack1, queue.stack2)

    P = Solution()
    P.push(10)
    P.push(11)
    P.push(12)
    print(P.pop())
    P.push(13)
    print(P.pop())
    print(P.pop())
    print(P.pop())
    print(P.pop())
