# -*- coding: utf-8 -*-
"""
   File Name：     102. Binary Tree Level Order Traversal
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

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []

        queue = [root]
        while queue:
            res.append([x.val for x in queue if x ])
            queue = [child for x in queue if x for child in (x.left, x.right)]
        return res[:-1]

    def levelOrder_iter(self, root):
        res = []

        def DFS(root, level):
            if not root: return
            if len(res) <= level: res.append([]) # 每下探一层就新建当前层的list

            res[level].append(root.val) # 这里 前序中序后序 都可以实现层级遍历
            DFS(root.left, level+1)
            DFS(root.right, level+1)

        DFS(root, 0)
        return res
