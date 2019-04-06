# -*- coding: utf-8 -*-
"""
   File Name：     链表中环的入口结点
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
    def EntryNodeOfLoop(self, pHead):
        # write code here
        p1 = pHead
        seed = []
        while p1:
            if p1 in seed:
                return p1
            seed.append(p1)
            p1 = p1.next
        return None

"""
标准解法  快慢指针
"""
class Solution_:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead:
            return None

        k = self.Len(pHead)
        if not k:
            return None

        p1 = p2 = pHead
        for i in range(k):
            p2 = p2.next
        while p2 != p1:
            p1 = p1.next
            p2 = p2.next
        return p1

    def Len(self, root):
        pSlow = pFast = root
        if not pFast.next:
            return None
        pFast = pFast.next

        flag = False
        while pFast.next:  # 要对无环的情况考虑 所以判断条件不能是  pFast != pSlow 否则死循环
            if pSlow == pFast:
                flag = True
                break
            pSlow = pSlow.next
            pFast = pFast.next
            if pFast: # 必须加速 才可能相遇...
                pFast = pFast.next
        if not flag: return None

        cnt = 1
        pFast = pFast.next
        while pFast != pSlow:
            cnt += 1
            pFast = pFast.next

        return cnt


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l2

    solu = Solution_()
    print(solu.EntryNodeOfLoop(l1).val)

