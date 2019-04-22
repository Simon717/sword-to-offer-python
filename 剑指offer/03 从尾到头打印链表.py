# -*- coding: utf-8 -*-
"""
   File Name：     03 从尾到头打印链表
   Description :
   Author :       YYJ
   date：          2019-02-12
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution2:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        res = []
        while listNode:
            res.append(listNode.val)
            listNode = listNode.next
        return res[::-1]


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if type(listNode) == None:
            return []
        if listNode.val == None:
            return []

        out = []
        head = listNode
        while head:
            # out.insert(0, head.val)
            out.append(head.val)
            head = head.next

        out.reverse()

        return out


if __name__ == '__main__':
    node1 = ListNode(10)
    node2 = ListNode(11)
    node3 = ListNode(13)
    node1.next = node2
    node2.next = node3

    testnode = ListNode()

    solu = Solution()
    print(solu.printListFromTailToHead(node1))
    print(solu.printListFromTailToHead(testnode))
