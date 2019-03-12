# -*- coding: utf-8 -*-
"""
   File Name：     226. Invert Binary Tree
   Description :
   Author :       simon
   date：          19-3-11
"""


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        if not root.left and not root.right:
            return root

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root

    def invertTree0(self, root):
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root