# -*- coding: utf-8 -*-
"""
   File Name：     序列化二叉树
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
"""
对于最简单的二叉树
123来说 输出的序列化结果 1,2,#,#,3,#,#
12 输出 1,2,#,#,#
所有的叶子节点和只有一个孩子的节点都用#表示

所以此时中序遍历序列化二叉树非常简单
"""
class Solution:
    def Serialize(self, root):
        # write code here
        if not root:
            return  '#'
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)

    def Deserialize(self, s):
        # write code here
        s = s.split(',')
        return self.helper(s, 0)[0]

    def helper(self, s, index):
        if index > len(s) - 1 or s[index] == '#': # 判断这个边界条件 考虑第一个进入的节点 index=0 最后一个进入的应该是N-1
            return None, index + 1

        root = TreeNode(int(s[index]))
        index += 1
        root.left, index = self.helper(s, index)
        root.right, index = self.helper(s, index)
        return root, index


if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.left = n2
    # n1.right = n3

    solu = Solution()
    print(solu.Serialize(n1))
    print(solu.Deserialize(solu.Serialize(n1)).val)

