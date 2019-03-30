# -*- coding: utf-8 -*-
"""
   File Name：     155. Min Stack
   Description :
   Author :       simon
   date：          19-3-25
"""

"""
基本思想就是使用两个栈
一个栈是常规的数据
另一个存放当前栈内最小值 这个栈不必和第一个栈相同长度 
"""
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if not self.minStack or (self.minStack and x <= self.minStack[-1]): # 必须是小于等于 等于意味着之前有个当前栈最小值==现在压入的值 此时二者都要保存
            self.minStack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        x = self.stack.pop()
        if x == self.minStack[-1]: # 这里的一个陷阱 010这种情况 弹出0之后minstack有可能变空
            self.minStack.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]

# Your MinStack object will be instantiated and called as such:
minStack =  MinStack()
minStack.push(0)
minStack.push(1)
minStack.push(0)
print(minStack.getMin())
minStack.pop()
print(minStack.top())
print(minStack.getMin())