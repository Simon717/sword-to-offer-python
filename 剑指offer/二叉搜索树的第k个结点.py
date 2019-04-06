# -*- coding: utf-8 -*-
"""
   File Name：     二叉搜索树的第k个结点
   Description :
   Author :       simon
   date：          19-3-18
"""
"""
题目描述
给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。
"""

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
深刻理解中序遍历
"""
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if k <= 0 or not pRoot:
            return
        self.res = None
        self.idx = 0

        def helper(root):
            if not root:
                return
            helper(root.left)
            self.idx += 1
            if self.idx == k:
                self.res = root
            helper(root.right)

        helper(pRoot)
        return  self.res

    def KthNode_iter(self, pRoot, k):
        if k <= 0 or not pRoot:
            return



if __name__ == '__main__':
    pRoot8 = TreeNode(2)
    pRoot9 = TreeNode(1)
    pRoot10 = TreeNode(3)
    pRoot8.left = pRoot9
    pRoot8.right = pRoot10

    solu = Solution()
    print(solu.KthNode(pRoot8, 2).val)