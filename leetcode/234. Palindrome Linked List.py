# -*- coding: utf-8 -*-
"""
   File Name：     234. Palindrome Linked List
   Description :
   Author :       simon
   date：          19-3-25
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

"""
标准的链表双指针解法
注意；题目没有说明的时候 可以
"""
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        def Inverse(root):
            aux = ListNode(None)
            p = root.next
            root.next = aux
            while p and p.next:
                tp = p.next
                p.next = root
                root = tp
                p = p.next
            return root


        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            frontSlow = slow
            slow = slow.next

        p = frontSlow
        while p.val != frontSlow.val:
            p = p.next
        frontSlow.next = None
        p = Inverse(p)

        p1, p2 = p, head
        while p1 and p2:
            if p1.val == p2.val:
                p1 = p1.next
                p2 = p2.next
            else:
                return False
        return True


class Solution_(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        # 找到中间节点
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # 翻转后半部分
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # 比较前后两部分
        while prev: # while prev and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True

class Solution__:
    def isPalindrome(self, head):
        # 找到链表终中点 考虑奇数偶数两种情况 最终slow的位置正中间（奇数） 中间偏右的节点（偶数）
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # 翻转链表
        prev = self.InerseList(slow)

        # 顺序检查两个链表
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True

    def InerseList(self, root):
        pre = None
        while root:
            tp = root.next
            root.next = pre
            pre = root
            root = tp

        return pre


if __name__ == '__main__':
    n1 = ListNode(0)
    n2 = ListNode(0)
    n4 = ListNode(3)
    n3 = ListNode(1)
    n1.next = n2
    n2.next = n4
    n4.next = n3
    solu = Solution__()
    print(solu.isPalindrome(n1))