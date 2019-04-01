# -*- coding: utf-8 -*-
"""
   File Name：     19. Remove Nth Node From End of List
   Description :
   Author :       simon
   date：          19-4-1
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        if not head:
            return None
        p = dummy = ListNode(None)
        p.next = head
        slow = fast = p
        for _ in range(n):
            fast = fast.next
        while fast and fast.next:
            fast, slow = fast.next, slow.next
        tp = slow.next.next
        slow.next = tp
        return dummy.next