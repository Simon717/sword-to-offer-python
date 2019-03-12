# -*- coding: utf-8 -*-
"""
   File Name：     617 mergeTrees
   Description :
   Author :       simon
   date：          19-3-9
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 递归代码
# 控制好 终止条件
# 写好本级的代码 就OK 比如只考虑最上一级的代码
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 or not t2: # t1 t2 中存在空节点 返回其中的非零节点
            return t1 or t2

        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)

        return t1


class Solution0(object):
    def __init__(self):
        self.list = []

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = [root]
        while queue:
            values = [x.val if x else None for x in queue]
            if values != values[::-1]: return False
            queue = [child for x in queue if x for child in (x.left, x.right)]
        return True