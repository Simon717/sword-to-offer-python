# -*- coding: utf-8 -*-
"""
   File Name：     17 合并两个排序的链表
   Description :
   Author :       YYJ
   date：          2019-02-16
"""
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 == None:
            return pHead2
        elif pHead2 == None:
            return pHead1

        p1, p2 = pHead1, pHead2
        dummy = ListNode(0) # 新建链表必须有头节点
        p3 = dummy
        while p1 and p2:
            if p1.val <= p2.val:
                p3.next = p1 # 链表的链接
                p1 = p1.next
            else:
                p3.next = p2
                p2 = p2.next
            p3 = p3.next # 指针移动

        if p1:
            p3.next = p1
        elif p2:
            p3.next = p2

        return dummy.next

    def Merge0(self, pHead1, pHead2):
        if pHead1 == None:
            return pHead2
        elif pHead2 == None:
            return pHead1

        if pHead1.val < pHead2.val: # 不断拆解问题
            pM = pHead1 # 只是为了记住头节点
            pHead1.next = self.Merge(pHead1.next, pHead2)
        else:
            pM = pHead2
            pHead2.next = self.Merge(pHead1, pHead2.next)
        return pM

    def Merge1(self, pHead1, pHead2):
        # write code here
        dummy = ListNode(0)
        pHead = dummy

        while pHead1 and pHead2:
            if pHead1.val >= pHead2.val:
                dummy.next = pHead2
                pHead2 = pHead2.next
            else:
                dummy.next = pHead1
                pHead1 = pHead1.next

            dummy = dummy.next
        if pHead1:
            dummy.next = pHead1
        elif pHead2:
            dummy.next = pHead2
        return pHead.next


node1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(5)
node1.next = node2
node2.next = node3

node4 = ListNode(2)
node5 = ListNode(4)
node6 = ListNode(6)
node4.next = node5
node5.next = node6

S = Solution()

print(S.Merge(node1, node4).next.val)