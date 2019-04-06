# -*- coding: utf-8 -*-
"""
   File Name：     按之字形顺序打印二叉树
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

class Solution:
    def Print(self, pRoot):
        # write code here
        queue = [pRoot]
        res = []
        flag = False
        while queue:
            val = [node.val for node in queue if node]
            res.append(val)
            if  flag:
                queue = [child for node in queue[::-1] if node for child in (node.left, node.right)] # 对上一轮队列取反 求出其中飞空节点的孩子节点
            else:
                queue = [child for node in queue[::-1] if node for child in (node.right, node.left)]
            flag = not flag
        return res[:-1]