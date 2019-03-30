# -*- coding: utf-8 -*-
"""
   File Name：     141. Linked List Cycle
   Description :
   Author :       simon
   date：          19-3-25
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False

        pSlow, pFast = head, head.next
        while pFast and pFast.next:
            pSlow = pSlow.next
            pFast = pFast.next.next
            if pFast == pSlow:  # 一定得先挪指针后判断 这样可以保证最后一个进入循环的元素被判断到
                return True
        return False

"""
使用hash表记录已经走过的节点 
这种有没有重复元素的问题 --> hash
"""
class Solution(object):
    def hasCycle(self, head):
        dic = {}

        while head:
            dic[head] = dic.get(head, 0) + 1
            if dic[head] > 1:
                return True
            head = head.next
        return False