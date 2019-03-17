# -*- coding: utf-8 -*-
"""
   File Name：     206. Reverse Linked List
   Description :
   Author :       simon
   date：          19-3-13
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

"""
超时
"""
class Solution0(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return

        res = []
        self.helper(head, res)
        return res[0]

    def helper(self, root, res):
        # if not root:
        #     return
        if not root.next:
            res.append(root)
            return
        p = root.next
        self.helper(root.next, res)
        p.next = root

"""
根本上说就是利用递归函数栈 解决链表的单项问题
实现从后往前 反向链表
提前存储next的节点
"""
class Solution_Me(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.helper(head)

    def helper(self, root):
        if not root:
            return
        if not root.next:
            return root
        p = root.next
        head = self.helper(root.next)
        p.next = root
        root.next = None
        return head


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.helper(head)[0]

    def helper(self, root):
        if not root.next:
            return root, root
        head, tail = self.helper(root.next)
        tail.next = root
        root.next = None
        return head, root


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)

    node1.next = node2

    solu = Solution()
    print(solu.reverseList(node1).next.val)