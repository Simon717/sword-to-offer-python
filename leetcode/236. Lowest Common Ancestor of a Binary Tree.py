# -*- coding: utf-8 -*-
"""
   File Name：     236. Lowest Common Ancestor of a Binary Tree
   Description :
   Author :       simon
   date：          19-3-31
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
自低向上 不断在每一个节点标记当前节点的子节点内有没有要查找的节点 有就标记 true 没有标记 False 
不断向上层传递

这中解法没办法在找到节点之后立即返回
"""
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.res = None

        def helper(root):
            if not root:
                return False, False
            tp1, tp2 = helper(root.left)
            tp3, tp4 = helper(root.right)
            a = True if root == p else False
            b = True if root == q else False
            a = a or (tp1 or tp3)
            b = b or (tp2 or tp4)
            if a and b:
                self.res = root
                return False, False # 找到之后防止被后面的根节点刷新掉了底层的结果  直接return False
            return a, b

        helper(root)
        return self.res

"""
优雅解法
"""
class Solution_:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q: # 包含一个节点 直接return回去这个节点
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right: # 当左边和右边各有一个pq
            return root # 找到最终节点
        return left or right