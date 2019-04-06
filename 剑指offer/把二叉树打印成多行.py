# -*- coding: utf-8 -*-
"""
   File Name：     把二叉树打印成多行
   Description :
   Author :       simon
   date：          19-3-19
"""
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
题目重复
都是用队列处理 二叉树层级遍历
"""
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        res, queue = [], [pRoot]
        while queue:
            val = [node.val for node in queue if node]
            res.append(val)
            queue = [child for node in queue if node for child in (node.left, node.right)]
        return res[:-1]