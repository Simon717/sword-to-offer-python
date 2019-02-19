# -*- coding: utf-8 -*-
"""
   File Name：     18 树的子结构
   Description :
   Author :       YYJ
   date：          2019-02-16
"""
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        # 前序遍历二叉树 找到树B根节点相同的节点
        result = False
        if pRoot1 and pRoot2:
            if pRoot1.val == pRoot2.val:
                result = self.sameNodes(pRoot1, pRoot2)
            if not result: # 没找到 继续前序遍历
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)
            return result

    def sameNodes(self, p1, p2):
        if p2 == None: # 此时可能出现 p1 == None # 如果树B到底 说明两棵树已经完全相同
            return True
        if p1 == None:
            return False
        if p1.val != p2.val:
            return False
        return self.sameNodes(p1.left, p2.left) and self.sameNodes(p1.right, p2.right)

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

    pRoot8 = TreeNode(8)
    pRoot9 = TreeNode(9)
    pRoot10 = TreeNode(2)
    pRoot8.left = pRoot9
    pRoot8.right = pRoot10

    S = Solution()
    print(S.HasSubtree(pRoot1, pRoot8))