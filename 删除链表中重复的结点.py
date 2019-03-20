# -*- coding: utf-8 -*-
"""
   File Name：     删除链表中重复的结点
   Description :
   Author :       simon
   date：          19-3-20
"""
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        aux = ListNode('x')
        aux.next = pHead    # 设置辅助节点  方便最后返回头指针
        pStt, pEnd = aux, pHead # pStt 指向了重复部分的第一个元素的前一个节点  pEnd指向重复部分的最后一个元素
        while pEnd:
            if pEnd.next and pStt.next.val == pEnd.next.val:
                while  pEnd.next and pStt.next.val == pEnd.next.val:
                    pEnd = pEnd.next
                pEnd = pEnd.next
                pStt.next = pEnd
            else:
                pStt = pStt.next
                pEnd = pEnd.next
        return aux.next