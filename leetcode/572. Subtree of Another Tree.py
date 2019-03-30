# -*- coding: utf-8 -*-
"""
   File Name：     572. Subtree of Another Tree
   Description :
   Author :       simon
   date：          19-3-24
"""

"""
Naive approach, O(|s| * |t|)
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def helper(s, t):
            if not s and not t:
                return True
            if not s and t:
                return False
            if not t and s:
                return False

            if s.val == t.val:
                return helper(s.left, t) or helper(s.right, t) or (same(s.left, t.left) and same(s.right, t.right))
            else:
                return helper(s.left, t) or helper(s.right, t)

        def same(s, t):
            if not s and not t:
                return True
            if not s and t:
                return False
            if not t and s:
                return False

            if s.val == t.val:
                return same(s.left, s.left) and same(s.right, t.right)
            else:
                return False

        return  helper(s, t)


"""
思路清晰版 代码
"""
class Solution_(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def isSameTree(p, q):
            if not p and not q:
                return True
            if (p and not q) or (not p and q):
                return False
            return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        if not t:
            return True
        if not s and t:
            return False
        if isSameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


def isMatch(self, s, t):
    if not(s and t):
        return s is t
    return (s.val == t.val and
            self.isMatch(s.left, t.left) and
            self.isMatch(s.right, t.right))

def isSubtree(self, s, t):
    if self.isMatch(s, t): return True
    if not s: return False
    return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)