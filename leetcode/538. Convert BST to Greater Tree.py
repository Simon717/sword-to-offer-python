# -*- coding: utf-8 -*-
"""
   File Name：     538. Convert BST to Greater Tree
   Description :
   Author :       simon
   date：          19-3-15
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.total = 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        self.convertBST(root.right)

        self.total += root.val
        root.val = self.total
        self.convertBST(root.left)

        return root


class Solution1(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.helper(root, 0)
        return root

    def helper(self, root, sum):
        if not root:
            return sum
        sum = self.helper(root.right, sum)
        tp = sum
        sum += root.val
        root.val += tp
        sum = self.helper(root.left, sum)
        return sum