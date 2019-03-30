# -*- coding: utf-8 -*-
"""
   File Name：     160. Intersection of Two Linked Lists
   Description :
   Author :       simon
   date：          19-3-25
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        def getLen(root):
            res = 0
            while root:
                res += 1
                root = root.next
            return res

        lenA = getLen(headA)
        lenB = getLen(headB)
        p1, p2 = headA, headB
        if lenA > lenB:
            for _ in range(lenA- lenB): p1 = p1.next
        else:
            for _ in range(lenB - lenA): p2 = p2.next

        while p1 and p2:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next
        return None

if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n1.next = n3
    n2.next = n3
    solu = Solution()
    print(solu.getIntersectionNode(n1, n2).val)