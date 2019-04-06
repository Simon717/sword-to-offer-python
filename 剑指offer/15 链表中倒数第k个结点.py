# -*- coding: utf-8 -*-
"""
   File Name：     15 链表中倒数第k个结点
   Description :
   Author :       YYJ
   date：          2019-02-15
"""
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head == None or k <= 0:
            return None

        # 设定两个指针 第一个指针指向投节点 第二个指向k-1节点
        p1, p2 = head, head
        i = 0
        while p2.next and i < k-1:
            p2 = p2.next
            i += 1
        if i != k-1: # 链表没有K个元素
            return None

        while p2.next:
            p1, p2 = p1.next, p2.next
        return p1