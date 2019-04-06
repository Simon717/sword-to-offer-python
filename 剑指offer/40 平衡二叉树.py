# -*- coding: utf-8 -*-
"""
   File Name：     40 平衡二叉树
   Description :
   Author :       simon
   date：          19-3-3
"""

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.flag = True

    def IsBalanced_Solution(self, pRoot):
        self.getDepth(pRoot)
        return self.flag

    """实质上是后序遍历"""
    def getDepth(self, pRoot): # 计算当前节点的深度
        # write code here
        if not pRoot:
            return 0

        left = self.getDepth(pRoot.left)
        right = self.getDepth(pRoot.right)
        if abs(left - right) > 1: # TODO 如何快速跳出递归 技巧 设置一个最大整数 加速递归
            self.flag = False
            return 9999999 #
        return max(left, right) + 1 # 当前节点深度 = 1（自己） + 孩子节点中较深的那个的深度
"""
改进版 
时间复杂度： O(n)
空间复杂度 O(1)
"""
class Solution_:
    def IsBalanced_Solution(self, pRoot):
        return self.getDepth(pRoot) != -1

    def getDepth(self, pRoot): # 计算当前节点的深度
        # write code here
        if not pRoot:
            return 0

        left = self.getDepth(pRoot.left)
        right = self.getDepth(pRoot.right)
        if left == -1 or right == -1 or abs(left - right) > 1: # 利用判断语句加速递归
            return -1 # 一旦发现树不平衡 return -1 在上层再对-1进行判断 遇到之后继续传递-1  就可以快速结束递归
        return max(left, right) + 1 # 当前节点深度 = 1（自己） + 孩子节点中较深的那个的深度


if __name__ == '__main__':
    pRoot1 = TreeNode(8)
    pRoot2 = TreeNode(8)
    pRoot3 = TreeNode(7)
    pRoot4 = TreeNode(9)
    pRoot5 = TreeNode(2)
    pRoot6 = TreeNode(4)
    pRoot7 = TreeNode(7)
    pRoot1.left = pRoot2
    pRoot1.right = pRoot3
    pRoot2.left = pRoot4
    pRoot2.right = pRoot5
    pRoot5.left = pRoot6
    pRoot5.right = pRoot7

    solu = Solution()
    print(solu.IsBalanced_Solution(pRoot1))