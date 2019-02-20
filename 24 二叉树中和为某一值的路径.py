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
            if curSum == expectNumber and (not root.left and not root.right):
                res.append(curPath[:]) # 这里必须使用切片操作 拿到curPath的副本 因为res里的curPath只是引用 后面curPath会弹出 导致最终生成的都是空list

            if curSum < expectNumber:
                if root.left:
                    recFindPath(root.left, curPath, curSum)
                if root.right:
                    recFindPath(root.right, curPath, curSum)
            curPath.pop() # 前序遍历完成之后 [根左右] 之后会回到上层所以根节点出栈

        recFindPath(root, [], 0)
        return res

if __name__ == '__main__':
    pNode1 = TreeNode(10)
    pNode2 = TreeNode(5)
    pNode3 = TreeNode(12)
    pNode4 = TreeNode(4)
    pNode5 = TreeNode(7)

    pNode1.left = pNode2
    pNode1.right = pNode3
    pNode2.left = pNode4
    pNode2.right = pNode5

    S = Solution()
    print(S.FindPath(pNode1, 22))