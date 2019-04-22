# -*- coding: utf-8 -*-
"""
   File Name：     04 重建二叉树
   Description :
   Author :       YYJ
   date：          2019-02-12
"""


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution2:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre:
            return None

        root_val = pre[0]
        idx = tin.index(root_val)
        root = TreeNode(root_val)
        root.left = self.reConstructBinaryTree(pre[1:1 + idx], tin[:idx])
        root.right = self.reConstructBinaryTree(pre[1 + idx:], tin[idx + 1:])
        return root


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if pre == []:
            return None
        root = pre[0]
        node = TreeNode(root)
        root_idx = tin.index(root)
        node.left = self.reConstructBinaryTree(pre[1:1 + root_idx], tin[:root_idx])
        node.right = self.reConstructBinaryTree(pre[1 + root_idx:], tin[root_idx + 1:])
        return node


def PrintNodeAtLevel(treeNode, level):
    if not treeNode or level < 0:
        return 0
    if level == 0:
        print(treeNode.val)
        return 1
    PrintNodeAtLevel(treeNode.left, level - 1)
    PrintNodeAtLevel(treeNode.right, level - 1)


# 已知树的深度按层遍历输出树的值
def PrintNodeByLevel(treeNode, depth):
    for level in range(depth):
        PrintNodeAtLevel(treeNode, level)


if __name__ == '__main__':
    pre = [1, 2, 3, 5, 6, 4]
    tin = [5, 3, 6, 2, 4, 1]
    test = Solution()
    newTree = test.reConstructBinaryTree(pre, tin)
    PrintNodeByLevel(newTree, 5)
