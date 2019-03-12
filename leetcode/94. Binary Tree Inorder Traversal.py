# -*- coding: utf-8 -*-
"""
   File Name：     94. Binary Tree Inorder Traversal
   Description :
   Author :       simon
   date：          19-3-12
"""
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right

class Solution0(object):
    def inorderTraversal(self, root):
        res, stack = [], []
        p = root # 看成一个”指针“
        while stack or p:
            if p: # 进栈 往左
                stack.append(p)
                p = p.left
            else: # 出栈 往右
                node = stack.pop()
                res.append(node.val)
                p = node.right
        return res