# -*- coding: utf-8 -*-
"""
   File Name：     337. House Robber III
   Description :
   Author :       simon
   date：          19-3-25
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
最简单的方案： 但是重复计算太多
超时
"""

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        a = self.rob(root.left) +  self.rob(root.right)
        tp = 0
        if root.left:
            tp = self.rob(root.left.left) + self.rob(root.left.right)
        tp1 = 0
        if root.right:
            tp1 = self.rob(root.right.left) + self.rob(root.right.right)
        b = root.val + tp1 + tp
        return max(a, b)

"""
改进一 使用hash表记录底层已经确定的解
AC
"""
class Solution_hash(object):
    def __init__(self):
        self.hash = {}

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root in self.hash: return self.hash[root]

        a = self.rob(root.left) +  self.rob(root.right)
        tp = 0
        if root.left:
            tp = self.rob(root.left.left) + self.rob(root.left.right)
        tp1 = 0
        if root.right:
            tp1 = self.rob(root.right.left) + self.rob(root.right.right)
        b = root.val + tp1 + tp
        val = max(a, b)
        self.hash[root] = val
        return val

"""
动态规划
每一个节点计算两种情况的最有解 
"""
class Solution___:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return 0, 0
            pickl, nopickl = dfs(root.left)
            pickr, nopickr = dfs(root.right)
            pick = nopickl + nopickr + root.val
            nopick = max(pickl, nopickl) + max(pickr, nopickr)
            return (pick, nopick)
        return max(dfs(root))

    def rob_(self, root):
        def DFS(root):
            if not root:
                return 0,0
            pickL, nopickL = DFS(root.left)
            pickR, nopickR = DFS(root.right)
            pick = root.val + nopickL + nopickR
            nopick = max(pickL, nopickL) + max(pickR, nopickR)
            return pick, nopick
        return max(DFS(root))