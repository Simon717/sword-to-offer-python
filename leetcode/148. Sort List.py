# -*- coding: utf-8 -*-
"""
   File Name：     148. Sort List
   Description :
   Author :       simon
   date：          19-3-31
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

"""
别人写的归并
"""
class Solution_merge(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        second = self.findMid(head)  # 找到链表后半段的head
        l = self.sortList(head)
        r = self.sortList(second)
        return self.merge(l, r)

    def merge(self, l, r):  # O(NlgN)
        if not l or not r:
            return l or r

        dummy = p = ListNode(None)

        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next
        p.next = l or r  # l and r at least one is None
        return dummy.next

    """
    1  2
    对于两个元素的情况 必须让slow停在第一个元素处 否则就陷入死循环 所以需要 while fast.next and fast.next.next:
    """
    def findMid(self, head):
        slow = fast = head
        while fast.next and fast.next.next: # 这一行很关键 必须这么写 需要考虑到最基本的情况 当前链表只有两个元素 三个元素 一个元素
            slow = slow.next
            fast = fast.next.next
        right = slow.next
        slow.next = None

        return right

"""
链表 快速排序
"""
class Solution_quick(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        l_dummy, m_dummy, r_dummy = ListNode(None), ListNode(None), ListNode(None)
        l, m, r = l_dummy, m_dummy, r_dummy

        # 经过这一段 操作 中间部分已经不需要操作
        pivot = head.val
        while head:
            if head.val < pivot:
                l.next = head
                l = l.next
            elif head.val == pivot:
                m.next = head
                m = m.next
            else:
                r.next = head
                r = r.next
            head = head.next

        l.next, r.next = None, None # 让left right part 结尾
        l_dummy.next = self.sortList(l_dummy.next) # 分别处理 left part 和 right part
        r_dummy.next = self.sortList(r_dummy.next)

        l = l_dummy
        while l.next:
            l = l.next # 挪到left part的最后一个元素
        l.next = m_dummy.next
        m.next = r_dummy.next
        return l_dummy.next


