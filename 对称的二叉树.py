# -*- coding: utf-8 -*-
"""
   File Name：     对称的二叉树
   Description :
   Author :       simon
   date：          19-3-18
"""

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetrical(self, pRoot):
        queue = [pRoot]
        while queue:
            val = [x.val if x else None for x in queue]
            if val != val[::-1]:
                return False
            queue = [child for node in queue if node for child in (node.left, node.right)] # 当前队列可能存在空节点 就不必往下寻找

        return True

    """
    这个循环解 清晰明了
    """
    def isSymmetric_Iter(self, root):
        queue = [root]
        while queue:
            values = [node.val if node else None for node in queue]
            if values != values[::-1]: return False
            queue = [child for node in queue if node  for child in (node.left, node.right)]  # 迭代探索当前queue中的节点的孩子节点


'''
请实现一个函数，用来判断一颗二叉树是不是对称的。
注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
'''

"""
递归解 
以root为根节点的树对称 --> root.left 和 root.right 对称
大树的对称分解成小树的对称
"""

class Solution_:
    def isSymmetrical(self, pRoot):
         return self.selfIsSymmetrical(pRoot, pRoot)

    def selfIsSymmetrical(self, pRoot1, pRoot2):
        if pRoot1 == None and pRoot2 == None: # 0 0
            return True
        if pRoot1 == None or pRoot2 == None: # 0 1
            return False
        if pRoot1.val != pRoot2.val: # 1 1
            return False
        return self.selfIsSymmetrical(pRoot1.left, pRoot2.right) and self.selfIsSymmetrical(pRoot1.right, pRoot2.left)
