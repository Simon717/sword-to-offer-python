# -*- coding: utf-8 -*-
"""
   File Name：     24 二叉树中和为某一值的路径
   Description :
   Author :       YYJ
   date：          2019-02-18
"""

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return

        res = []

        def recursion(root, path, curSum):
            path.append(root.val)
            curSum += root.val
            if curSum == expectNumber and (not root.lef and not root.right):
                res.append(path)

class Solution0:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        result = []

        def FindPath2(root, path, currentNum):
            currentNum += root.val
            # root使用append转成了列表，因为最后要一个序列，root本身还是树结构
            path.append(root)
            # 判断是不是到叶子节点了，到叶子节点了就要判断值的和是不是相等
            flag = root.left == None and root.right == None
            # 返回值是一个等于整数的序列
            if currentNum == expectNumber and flag:
                onepath = []
                for node in path:
                    onepath.append(node.val)
                result.append(onepath)

            if currentNum < expectNumber:
                if root.left:
                    FindPath2(root.left, path, currentNum)
                if root.right:
                    FindPath2(root.right, path, currentNum)
            # 拿到一个正确的路径后要弹出，回到上一次父节点继续递归
            path.pop()

        FindPath2(root, [], 0)
        return result