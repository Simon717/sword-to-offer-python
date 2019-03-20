# -*- coding: utf-8 -*-
"""
   File Name：     101 Symmetric Tree
   Description :
   Author :       simon
   date：          19-3-10
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
思路： 得到中序遍历序列 
"""

class Solution(object):
    def __init__(self):
        self.list = []

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        self.helper(root)
        res = self.list
        center = len(res) // 2
        a = res[:center]
        b = res[center + 1:][::-1]
        return a == b

    def helper(self, root):
        if not root:
            self.list.append('NULL')
            return
        self.helper(root.left)
        self.list.append(root.val)
        self.helper(root.right)

    """
    leetcode 
    """


    def isSymmetric00(self, root):
        def isSym(L, R):
            if not L and not R: return True
            if L and R and L.val == R.val:
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            return False

        if root is None:
            return True
        return isSym(root.left, root.right)

    def isSymmetric0(self, root):
        def isSym(L,R):
            if L and R and L.val == R.val: # 有左右 且值相等
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            return L == R
        return not root or isSym(root.left, root.right)

    """
    这个循环解 清晰明了
    """
    def isSymmetric_Iter(self, root):
        queue = [root]
        while queue:
            values = [node.val if node else None for node in queue]
            if values != values[::-1]: return False
            queue = [child for node in queue if node  for child in (node.left, node.right)]  # 迭代探索当前queue中的节点的孩子节点
        return True

    def isSymmetric_Iter0(self, root): # 使用队列实现二叉树的层级遍历
        if not root:
            return True

        queue = []
        queue.append((root.left, root.right))
        while queue:
            l, r = queue.pop(0)
            if not l and not r:
                continue
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            queue.append((l.left, r.right))
            queue.append((l.right, r.left))
        return True

# 二叉树 按层输出 按层打印
def printByLevel(root):
    if not root:
        return
    print("Print binary tree by level")
    queue = []
    queue.append(root)
    last = root
    level = 1
    print("Level " + str(level) + ':', end=' ')
    while queue:
        root = queue.pop(0)
        print(root.val, end=' ')
        if root.left:
            nlast = root.left
            queue.append(root.left)
        if root.right:
            nlast = root.right
            queue.append(root.right)
        if root == last and queue:
            last = nlast
            print()
            level += 1
            print("Level " + str(level) + ":", end=' ')

if __name__ == '__main__':
    n0 = TreeNode(1)
