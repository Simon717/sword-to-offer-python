# -*- coding: utf-8 -*-
"""
   File Name：     37 两个链表的第一个公共结点
   Description :
   Author :       simon
   date：          19-2-27
"""

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
通过测试 感觉还有问题
"""
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None
        if pHead1 == pHead2:
            return pHead1

        p1, p2 = pHead1, pHead2
        p1_stack, p2_stack = [None], [None]
        while p1:
            p1_stack.append(p1)
            p1 = p1.next
        while p2:
            p2_stack.append(p2)
            p2 = p2.next
        for i in range(min(len(p1_stack), len(p2_stack))):
            tp1, tp2 = p1_stack.pop(), p2_stack.pop()
            if tp1 != tp2:
                break
        return tp1.next

'''
思路：共同节点，意味着从共同节点开始之后所有的节点数都是相同的，这是链表，只要有一个共同节点，那么之后所有的指向
也是重复的。先依次遍历两个链表，记录两个链表的长度m和n，如果 m > n，那么我们就先让长度为m的链表走m-n个结点，然后
两个链表同时遍历，当遍历到相同的结点的时候停止即可。对于 m < n，同理。
32ms
5632k
'''
class Solution0:
    def FindFirstCommonNode(self, pHead1, pHead2):
        nLength1 = self.GetListLength(pHead1)
        nLength2 = self.GetListLength(pHead2)
        nLengthDiff = abs(nLength1 - nLength2)

        if nLength1 > nLength2:
            pListHeadLong = pHead1
            pListHeadShort = pHead2
        else:
            pListHeadLong = pHead2
            pListHeadShort = pHead1

        for i in range(nLengthDiff):
            pListHeadLong = pListHeadLong.next

        while pListHeadLong != None and pListHeadShort != None and pListHeadLong != pListHeadShort:
            pListHeadLong = pListHeadLong.next
            pListHeadShort = pListHeadShort.next

        pFirstCommonNode = pListHeadLong
        return pFirstCommonNode

    def GetListLength(self, pHead):
        nLength = 0
        while pHead != None:
            pHead = pHead.next
            nLength += 1
        return nLength
