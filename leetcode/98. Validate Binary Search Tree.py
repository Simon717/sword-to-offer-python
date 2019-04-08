# -*- coding: utf-8 -*-
"""
   File Name：     98. Validate Binary Search Tree
   Description :
   Author :       simon
   date：          19-4-7
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
利用 plast 存放上一个节点
"""


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.plast = None

        def helper(root):
            if not root:
                return True

            left = helper(root.left)
            if self.plast:
                if self.plast.val >= root.val:
                    return False
            self.plast = root

            right = helper(root.right)
            return left and right

        return helper(root)


"""
自上而下 check每一个节点的取值区间
"""
import sys


class Solution_(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def valid(root, smallest, largest):
            if not root:
                return True
            if smallest >= root.val or largest <= root.val:
                return False
            return valid(root.left, smallest, root.val) and valid(root.right, root.val, largest)

        if not root:
            return True
        return valid(root, -sys.maxsize, sys.maxsize)
