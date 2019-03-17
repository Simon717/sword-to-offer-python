# -*- coding: utf-8 -*-
"""
   File Name：     437 path sum 3
   Description :
   Author :       simon
   date：          19-3-16
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
bug
"""
class Solution0(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        return self.helper(root, sum, [], 0)

    def helper(self, root, sum, path, cnt):
        if not root:
            return cnt

        path.append(root.val)

        tempSum = 0
        for i in range(len(path) - 1, -1, -1):
            tempSum += path[i]
            if tempSum == sum:
                cnt += 1

        cnt = self.helper(root.left, sum, path, cnt)
        cnt = self.helper(root.right, sum, path, cnt)
        return cnt

class Solution(object):
    def pathSum(self, root, sum):
        """
        :param root:
        :param sum:
        :return:
        """
        return self.helper(root, sum, [])

    def helper(self, root, sum, path):
        if not root:
            return 0
        path.append(root.val)
        tempSum = 0
        cnt = 0
        for i in range(len(path) - 1, -1, -1):
            tempSum += path[i]
            if tempSum == sum:
                cnt += 1
        return cnt + self.helper(root.left, sum, path) + self.helper(root.right, sum, path)

"""
正确解分割线 
分析: 任何点都可能是起点 任何点也都可能是终点 
因此有两种思路： 递归所有的起点 + 递归所有的终点
或者是 只递归所有的终点 每一次考虑所有的起点 
"""
# 两层DFS
# 时间慢 内存小
class Solution_(object):
    # 考虑所有可能的起点
    def pathSum(self, root, sum): # 固定起点 不固定终点
        if not root:
            return 0

        return self.pathSumStart(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    # 考虑所有可能的终点
    def pathSumStart(self, root, sum): # 锁定root为起点
        if not root:
            return 0
        res = 1 if root.val==sum else 0
        return  res + self.pathSumStart(root.left, sum-root.val) + self.pathSumStart(root.right, sum-root.val)

# 一层DFS
# 时间快 内存大
class Solution__(object):
    def pathSum(self, root, sum):
        return self.helper(root, sum, [sum])

    def helper(self, root, sum, targets): # targets 存放了之前路径上的所有点 这些点都可能成为起点
        if not root: return 0
        cnt = 0
        for t in targets: # 遍历之前所有可能的起点
            if root.val == t: # 尝试以当前节点作为终点
                cnt += 1

        targets = [t - root.val for t in targets] + [sum]
        return cnt + self.helper(root.left, sum, targets) + self.helper(root.right, sum, targets)