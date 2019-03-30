# -*- coding: utf-8 -*-
"""
   File Name：     17. Letter Combinations of a Phone Number
   Description :
   Author :       simon
   date：          19-3-23
"""


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        n = len(digits)
        self.res = []

        def DFS(index, path): # 使用index控制递归深度
            if index == n:
                self.res.append(''.join(path))
                return
            for i in phone[digits[index]]:
                DFS(index+1, path+[i])

        DFS(0, [])
        return self.res

test = '23'
solu = Solution()
print(solu.letterCombinations(test))

