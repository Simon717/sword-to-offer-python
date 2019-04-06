# -*- coding: utf-8 -*-
"""
   File Name：     39 二叉树的深度
   Description :
   Author :       simon
   date：          19-3-3
"""

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class mySolution:
    def __init__(self):
        self.maxLen = -1
        self.path = []

    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        self.TreeDepth_(pRoot)
        return self.maxLen

    def TreeDepth_(self, pRoot):
        # write code here
        if not pRoot:
            return

        self.path.append(pRoot)
        self.TreeDepth(pRoot.left)
        self.TreeDepth(pRoot.right)

        if not pRoot.left and not  pRoot.right: # 叶子节点 check路径长度
            if len(self.path) > self.maxLen:
                self.maxLen = len(self.path)
        self.path.pop()

class Solution:
    # 递归解法, 简单直接, 时间复杂度O(n), 空间复杂度O(logn)
    """
    递归的时候无需判断左右子树是否存在，因为如果该节点为叶节点，它的左右子树不存在，那么在下一级递归的时候，直接return 0。意思就是深度是0
    """
    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        else:
            return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1

# TODO 没看
class Solution1:
    # 非递归算法，利用一个栈以及一个标志位栈
    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0

        depth = 0
        stack, tag = [], []
        pNode = pRoot
        while pNode or stack:
            while pNode:
                stack.append(pNode)
                tag.append(0)
                pNode = pNode.left
            if tag[-1] == 1:
                depth = max(depth, len(stack))
                stack.pop()
                tag.pop()
                pNode = None
            else:
                pNode = stack[-1]
                pNode = pNode.right
                tag.pop()
                tag.append(1)
        return depth

if __name__ == '__main__':
    pRoot1 = TreeNode(8)
    pRoot2 = TreeNode(8)
    pRoot3 = TreeNode(7)
    pRoot4 = TreeNode(9)
    pRoot5 = TreeNode(2)
    pRoot6 = TreeNode(4)
    pRoot7 = TreeNode(7)
    pRoot1.left = pRoot2
    pRoot1.right = pRoot3
    pRoot2.left = pRoot4
    pRoot2.right = pRoot5
    pRoot5.left = pRoot6
    pRoot5.right = pRoot7

    solu = mySolution()
    solu.TreeDepth(pRoot1)
    print(solu.maxLen)

    solu0 = Solution()
    print(solu0.TreeDepth(pRoot1))
