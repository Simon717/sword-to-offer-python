# -*- coding: utf-8 -*-
"""
   File Name：     104 Maximum Depth of Binary Tree
   Description :
   Author :       simon
   date：          19-3-9
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.helper(root)

    def helper(self, root):
        if not root:
            return 0

        res = 1  # 当前节点飞空  计数1
        child = max(self.helper(root.left), self.helper(root.right)) # 计算左右子树的深度 取其中较大的值

        return res + child
