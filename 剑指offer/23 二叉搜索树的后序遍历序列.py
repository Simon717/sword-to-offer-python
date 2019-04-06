# -*- coding: utf-8 -*-
"""
   File Name：     23 二叉搜索树的后序遍历序列
   Description :
   Author :       YYJ
   date：          2019-02-18
"""
# -*- coding:utf-8 -*-
class Solution0:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        if len(sequence) == 1:
            return True

        p = 0
        while sequence[p] < sequence[-1]:
            p += 1
        split = p # p是第一个不满足判断条件的index

        while p < len(sequence): # 检查右子树不要小于根节点的数
            if sequence[p] < sequence[-1]:
                return False
            p += 1

        left = True
        if split:
            left = self.VerifySquenceOfBST(sequence[:split])

        right = True
        if split<len(sequence)-1:
            right = self.VerifySquenceOfBST(sequence[split:-1])

        return left and right

class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False

        root = sequence[-1]

        p = 0
        for node in sequence[:-1]:
            if node > root:
                break
            p += 1

        for node in sequence[p:-1]:
            if node < root:
                return False

        left = True
        # i>0 意味i =0 或者1 的时候，两个元素在二叉树没有排序之分的，但是3个元素就有了左右子树之分
        if p > 0:
            left = self.VerifySquenceOfBST(sequence[:p])

        right = True
        # len(sequence)>=3才有左右之分的
        if p < len(sequence) - 2 and left:
            right = self.VerifySquenceOfBST(sequence[p + 1:])

        return left and right


if __name__ == '__main__':
    array = [5, 7, 6, 9, 11, 10, 8]
    array2 = [4, 6, 7, 5]
    array3 = [1, 2, 3, 4, 5]
    S = Solution0()
    print(S.VerifySquenceOfBST(array))
    print(S.VerifySquenceOfBST(array2))
    print(S.VerifySquenceOfBST(array3))