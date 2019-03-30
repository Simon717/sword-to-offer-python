# -*- coding: utf-8 -*-
"""
   File Name：     20. Valid Parentheses
   Description :
   Author :       simon
   date：          19-3-23
"""

"""
思路： 不断从中间删除'()', '[]', '{}' 直到最后变成空字符串
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        if len(s)%2:
            return False

        s = list(s)
        for _ in range(len(s)//2):
            i = 0
            while i < len(s):
                if i+1 < len(s) and s[i] + s[i+1] in ['()', '[]', '{}']:
                    s.remove(s[i])
                    s.remove(s[i])
                else:
                    i += 1
        return s == []


"""
官方解

从左往右扫描符号 
遇到左半部分括号压入堆栈 
遇到有半部分的时候就弹出堆栈的元素 
二者需要配对

从左往右观察合法的括号的时候可以发现后出现的左括号会先得到右括号的匹配
这就是先入后出 后入先出的特性
可以联想到使用堆栈
"""
class Solution_(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = []
        right2left = { ")": "(",
                       "}": "{",
                       "]": "["}
        for char in s:
            if char in right2left: # 遇到了右半部分 弹出堆栈元素 判断是否匹配
                top_element = left.pop() if left else '#'
                if right2left[char] != top_element:
                    return False
            else: # 遇到左半部分 压入堆栈等待匹配
                left.append(char)
        return not left

test = '({[[]]})'
solu = Solution()
print(solu.isValid(test))