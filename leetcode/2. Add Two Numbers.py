# -*- coding: utf-8 -*-
"""
   File Name：     2. Add Two Numbers
   Description :
   Author :       simon
   date：          19-4-7
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = head = ListNode(None)
        carry = 0
        while True:
            if not l1 and not l2:
                if not carry:
                    break
                else:
                    head.next = ListNode(carry)
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            num, carry = (v1 + v2 + carry) % 10, (v1 + v2 + carry) // 10
            head.next = ListNode(num)
            head = head.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next


"""
递归解
"""
class Solution_:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2: # 00
            return
        elif not (l1 and l2): # 01 10
            return l1 or l2
        else: # 11
            if l1.val + l2.val < 10:
                l3 = ListNode(l1.val+l2.val)
                l3.next = self.addTwoNumbers(l1.next, l2.next)
            else:
                l3 = ListNode(l1.val+l2.val-10) # 先处理低位
                l3.next = self.addTwoNumbers(l1.next, self.addTwoNumbers(l2.next, ListNode(1))) #　高位进位 此时相当于三个数相加
        return l3