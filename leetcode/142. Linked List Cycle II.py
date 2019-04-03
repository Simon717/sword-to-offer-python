# -*- coding: utf-8 -*-
"""
   File Name：     142. Linked List Cycle II
   Description :
   Author :       simon
   date：          19-4-2
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next: # 快指针夺走了一圈？
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None

        # 这里是为啥
        while head != slow:
            slow = slow.next
            head = head.next
        return head