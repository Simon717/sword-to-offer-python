# -*- coding: utf-8 -*-
"""
   File Name：     19 二叉树的镜像
   Description :
   Author :       YYJ
   date：          2019-02-16
"""
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root): # 先修改子树 再交换本级的左右节点
        # write code here
        if root == None:
            return

        root.left, root.right = self.Mirror(root.right), self.Mirror(root.left)
        return root

    def Mirror0(self, root): # 先交换本级的左右节点 再修改子树
        if not root:
            return

        root.left, root.right = root.right, root.left #
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root

    def Mirror_bug(self, root):

        root.right = self.Mirror(root.left) # 没有分析明白为什么错
        root.left  = self.Mirror(root.right) # 低级错误 先对root.right进行修改 后一句实际上想要的是未修改之前的值
        # 正确写法
        root.left, root.right = self.Mirror(root.right), self.Mirror(root.left)


# 非递归实现
    def Mirror2(self, root):
        if root == None:
            return
        stackNode = []
        stackNode.append(root)
        while len(stackNode) > 0:
            nodeNum = len(stackNode) - 1
            tree = stackNode[nodeNum]
            stackNode.pop()
            nodeNum -= 1
            if tree.left != None or tree.right != None:
                tree.left, tree.right = tree.right, tree.left
            if tree.left:
                stackNode.append(tree.left)
                nodeNum += 1
            if tree.right:
                stackNode.append(tree.right)
                nodeNum += 1
    # 非递归实现
    def MirrorNoRecursion(self, root):
        if root == None:
            return
        nodeQue = [root]
        while len(nodeQue) > 0:
            curLevel, count = len(nodeQue), 0
            while count < curLevel:
                count += 1
                pRoot = nodeQue.pop(0)
                pRoot.left, pRoot.right = pRoot.right, pRoot.left
                if pRoot.left:
                    nodeQue.append(pRoot.left)
                if pRoot.right:
                    nodeQue.append(pRoot.right)


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

    pRoot8 = TreeNode(8)
    pRoot9 = TreeNode(9)
    pRoot10 = TreeNode(2)
    pRoot8.left = pRoot9
    pRoot8.right = pRoot10

    S = Solution()
    print(S.Mirror(pRoot1).left.val)