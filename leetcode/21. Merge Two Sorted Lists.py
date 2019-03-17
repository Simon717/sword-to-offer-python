# -*- coding: utf-8 -*-
"""
   File Name：     21. Merge Two Sorted Lists
   Description :
   Author :       simon
   date：          19-3-15
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = pl = ListNode(0)  # 辅助节点
        while l1 and l2:
            if l1.val <= l2.val:
                pn = l1
                l1 = l1.next
            else:
                pn = l2
                l2 = l2.next

            pl.next = pn
            pl = pn

        pl.next = l1 or l2

        return dummy.next

    # iteratively
    def mergeTwoLists1(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1 # 直接脸上当前节点 少使用一个节点
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

"""
递归解 真TM优雅
"""
class SolutionRec(object):
    def mergeTwoLists(self, l1, l2):
        if not l1 or not l2: # 两个链表其中一个是空链表
            return l1 or l2  # 返回其中非空的链表 （就是另一个非空的链表）

        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    # in-place, iteratively # TODO meikan
    def mergeTwoLists0(self, l1, l2):
        if None in (l1, l2):
            return l1 or l2
        dummy = cur = ListNode(0)
        dummy.next = l1
        while l1 and l2:
            if l1.val < l2.val:
                l1 = l1.next
            else:
                nxt = cur.next
                cur.next = l2
                tmp = l2.next
                l2.next = nxt
                l2 = tmp
            cur = cur.next

        cur.next = l1 or l2
        return dummy.next
