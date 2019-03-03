# -*- coding: utf-8 -*-
"""
   File Name：     40 平衡二叉树
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

class Solution:
    def __init__(self):
        self.flag = True

    def IsBalanced_Solution(self, pRoot):
        self.getDepth(pRoot)
        return self.flag

    def getDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0

        left = self.getDepth(pRoot.left)
        right = self.getDepth(pRoot.right)
        if abs(left - right) > 1: # TODO 如何快速跳出递归
            self.flag = False
        return max(left, right) + 1

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

    solu = Solution()
    print(solu.IsBalanced_Solution(pRoot1))