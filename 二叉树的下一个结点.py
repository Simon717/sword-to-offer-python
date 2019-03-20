# -*- coding: utf-8 -*-
"""
   File Name：     二叉树的下一个结点
   Description :
   Author :       simon
   date：          19-3-18
"""
# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

"""
中序遍历 左根右

第一道自己的原创解 感觉很有成就感~
主要是活学活用了之前的状态码思想 
"""
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return

        # 获得根节点
        pRoot = pNode
        while pRoot.next:
            pRoot = pRoot.next
        self.res = None

        def inOrder(root, state):
            if not root:
                return state # 为啥不能是 return -1

            state = inOrder(root.left, state)

            if state == 1: #检查状态码2
                self.res = root  # 必须定义为 self类的属性才有用
                state = 2
            if root == pNode: # 找到目标节点之后 将状态码置成1 下一次的判断到状态码为1的节点就是需要return的节点
                state = 1
            if state == 2:  # 加速递归的结束 后面的节点不用继续递归
                return state

            state = inOrder(root.right, state)
            return state

        inOrder(pRoot, -1)
        return self.res