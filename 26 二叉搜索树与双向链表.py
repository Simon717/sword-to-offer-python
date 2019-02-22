# -*- coding: utf-8 -*-
"""
   File Name：     26 二叉搜索树与双向链表
   Description :
   Author :       YYJ
   date：          2019-02-20
"""

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
怎么将两种不同的情况合并成一种情况 就可以简化流程
主要的难点在于 处理完左子树之后 根节点如何跟左子树链接
在递归中使用前后双指针 ？ 
"""
class Solution:
    def Convert(self, pRootOfTree):
        if pRootOfTree == None:
            return None
        if not pRootOfTree.left and not pRootOfTree.right: # 遇到叶子节点 直接返回到它的根节点
            return pRootOfTree

        # 处理左子树
        self.Convert(pRootOfTree.left)
        left = pRootOfTree.left #

        # 连接根与左子树最大结点
        if left:
            while left.right:
                left = left.right
            pRootOfTree.left, left.right = left, pRootOfTree

        # 处理右子树
        self.Convert(pRootOfTree.right)
        right = pRootOfTree.right

        # 连接根与右子树最小结点
        if right:
            while right.left:
                right = right.left
            pRootOfTree.right, right.left = right, pRootOfTree

        # 只是为了最终返回回最小节点 对中间的递归调用没有意义
        while pRootOfTree.left:
            pRootOfTree = pRootOfTree.left

        return pRootOfTree

# 通过...
class Solution0:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return
        self.pLast = TreeNode(None) # 作为辅助节点 因为中序遍历第一个节点时不存在“上一个节点”
        self.Convert_helper(pRootOfTree)

        pRes = pRootOfTree
        while pRes.left:
            pRes = pRes.left
        return pRes

    def Convert_helper(self, root):
        if not root:
            return
        pCur = root
        if root.left:
            self.Convert_helper(root.left)

        self.pLast.right = pCur
        if self.pLast.val: # 中序遍历的第一个节点 不需要连接pLast
            pCur.left = self.pLast

        self.pLast = pCur # 当前节点转化完毕 更新pLast
        if root.right:
            self.Convert_helper(root.right)




# 思路废了 通过率20%
# class Solution:
#
#     def Convert(self, pRootOfTree):
#         flag = False
#         a, b = self.Convert_helper(pRootOfTree, flag)
#         return a
#
#     def Convert_helper(self, pRootOfTree, flag):
#         # write code here
#         if not pRootOfTree:
#             return
#
#         # 拆到底
#         if self.isLeaf(pRootOfTree):
#             flag = True
#             return
#         if self.isLeaf(pRootOfTree.left) and self.isLeaf(pRootOfTree.right):
#             pRootOfTree.left.right = pRootOfTree
#             pRootOfTree.right.left = pRootOfTree
#
#             return pRootOfTree.left, pRootOfTree.right
#
#         # 中间状态
#         else:
#             p1, p2 = self.Convert_helper(pRootOfTree.left)
#             p3, p4 = self.Convert_helper(pRootOfTree.right)
#             p2.right = pRootOfTree
#             pRootOfTree.left = p2
#             p3.left = pRootOfTree
#             pRootOfTree.right = p3
#
#             return p1, p4


    def isLeaf(self, root):
        return not(root.left and root.right)

"""
1. 利用中序遍历 得到排序的数据
2. 将数据进行左右连接 
并没有产生新的节点 只是将各个节点的地址存入了list
"""
class Solution1:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return

        self.nodes = []
        self.midorder(pRootOfTree)
        for i, v in enumerate(self.nodes[:-1]):
            v.right = self.nodes[i + 1]
            self.nodes[i + 1].left = v
        return self.nodes[0]

    def midorder(self, root):
        if not root:
            return
        self.midorder(root.left)
        self.nodes.append(root)
        self.midorder(root.right)

if __name__ == '__main__':
    pNode1 = TreeNode(8)
    pNode2 = TreeNode(6)
    pNode3 = TreeNode(10)
    pNode4 = TreeNode(5)
    pNode5 = TreeNode(7)
    pNode6 = TreeNode(9)
    pNode7 = TreeNode(11)

    pNode1.left = pNode2
    pNode1.right = pNode3
    pNode2.left = pNode4
    pNode2.right = pNode5
    pNode3.left = pNode6
    pNode3.right = pNode7

    S = Solution0()
    newList = S.Convert(pNode1)
    print(newList.val)