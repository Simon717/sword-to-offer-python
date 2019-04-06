# -*- coding: utf-8 -*-
"""
   File Name：     25 复杂链表的复制
   Description :
   Author :       YYJ
   date：          2019-02-19
"""

# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if pHead == None:
            return None

        self.CloneNodes(pHead)
        self.CloneRandom(pHead)
        return self.mySplit(pHead)

    def CloneNodes(self, pHead):
        p = pHead
        while p:
            pCloned = RandomListNode(p.label)
            pCloned.next = p.next
            p.next = pCloned
            p = pCloned.next

    def CloneRandom(self, pHead):
        p = pHead
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next # 有空节点无所谓 赋值None就行 然后会正常终止代码

    def mySplit(self, pHead):
        pClonedHead = pHead.next
        pNode, pClonedNode = pHead, pHead.next
        while pClonedNode.next:
            pNode.next = pClonedNode.next  # 连箭
            pNode = pNode.next  # 移动
            pClonedNode.next = pNode.next  # 连箭
            pClonedNode = pClonedNode.next  # 移动
        pNode.next = pClonedNode.next  # 连箭
        return pClonedHead

    def Split(self, pHead): # 一旦不处理原来的链表就出错 为啥呢
        pClonedHead = pHead.next

        pNode, pClonedNode = pHead, pHead.next
        pNode.next = pClonedHead.next # 连箭
        pNode = pNode.next # 移动
        while pNode:
            pClonedNode.next = pNode.next # 连箭
            pClonedNode = pClonedNode.next # 移动
            pNode.next = pClonedNode.next # 连箭
            pNode = pNode.next # 移动
        return pClonedHead

if __name__ == '__main__':
    # node1 = RandomListNode(1)
    # node2 = RandomListNode(2)
    # node3 = RandomListNode(3)
    # node4 = RandomListNode(4)
    #
    # node1.next = node2
    # node2.next = node3
    # node3.next = node4
    #
    # node1.random = node3
    # node2.random = node4
    #
    # solu = Solution()
    #
    # p = solu.Clone(node1)
    # while p:
    #     print(p.label)
    #     p = p.next

    node1 = RandomListNode(1)
    node2 = RandomListNode(3)
    node3 = RandomListNode(5)
    node1.next = node2
    node2.next = node3
    node1.random = node3

    S = Solution()
    clonedNode = S.Clone(node1)
    print(clonedNode.random.label)
