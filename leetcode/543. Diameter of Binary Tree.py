# -*- coding: utf-8 -*-
"""
   File Name：     543. Diameter of Binary Tree
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
        self.res = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def single_depth(root): #  计算单边的深度
            if not root:
                return -1 # 当处理叶子节点的左孩子时 给-1 之后回到叶子节点在+1 最终可以变成0 满足了单节点的深度为0

            left = single_depth(root.left)
            right = single_depth(root.right)
            self.res = max(self.res, 2 + left + right) # 负责刷新最大长度
            return 1 + max(left, right)

        single_depth(root)
        return self.res

    def diameterOfBinaryTree0(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0

        def single_depth(root):  # 计算单边的深度 这里记录的单边路径下节点的个数 不是线段的次数了 二者相差1
            if not root:
                return 0  #

            left = single_depth(root.left)
            right = single_depth(root.right)
            self.res = max(self.res, left + right)  # 负责刷新最大长度
            return 1 + max(left, right)

        single_depth(root)
        return self.res