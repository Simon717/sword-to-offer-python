# -*- coding: utf-8 -*-
"""
   File Name：     114. Flatten Binary Tree to Linked List
   Description :
   Author :       simon
   date：          19-3-31
"""

"""
处理顺序 左右根
"""
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        left = self.flatten(root.left)
        right = self.flatten(root.right)
        root.left = None # 需要手动将左子树置空
        root.right = left
        tp = root
        while tp.right:
            tp = tp.right
        tp.right = right
        return root


"""
遍历顺序 右左根 使用prev存放前一次的节点 这样 左的右就是prev=右 根的右就是prev=左
实现了根的右是左 左的右是右 顺次连接上
"""
class Solution_:
    def __init__(self):
        self.prev = None

    def flatten(self, root):
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root
