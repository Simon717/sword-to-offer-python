# -*- coding: utf-8 -*-
"""
   File Name：     3. Longest Substring Without Repeating Characters
   Description :
   Author :       simon
   date：          19-3-22
"""

"""
使用hash表作为滑动窗口
比较难想到用hash表
"""
class Solution_(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        usedChar, str_len, start = {}, 0, 0
        for i, char in enumerate(s):
            if char in usedChar.keys(): # 遇到见过的字符
                str_len = max(str_len, i - start) # 刷新字符串长度
                start = max(start, usedChar[char] + 1) # 刷新起点
            usedChar[char] = i # 记录字符最新出现的位置
        return max(str_len, len(s) - start)


class Solution_128:
    def lengthOfLongestSubstring(self, s):
        dic, maxLen, stt = [0]*128, 0, 0
        for i, char in enumerate(s):
            maxLen = max(maxLen, i - stt)
            stt = max(stt, dic[ord(char)] + 1)
            dic[ord(char)] = i
        return max(maxLen, len(s)-stt)

"""
我的解法
使用一个队列用于存放子串 
时间复杂度 O(n)
"""
class Solution__(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        queue = []
        maxLen = 0
        for x in s:
            if x in queue:
                while queue[0] != x:
                    queue.pop(0)
                queue.pop(0)
            queue.append(x)

            if len(queue) > maxLen:
                maxLen = len(queue)
        return maxLen




"""
双指针 + set
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right = 0, 0
        usedChar = set()
        maxLen = 0
        while left < len(s) and right < len(s):
            if s[right] in usedChar:
                while s[left] not in usedChar: # 直接找到这个重复出现的元素
                    left += 1
                usedChar.remove(s[left])
                left += 1
                # if s[left] in usedChar:
                #     usedChar.remove(s[left])
                # left += 1
            else:
                usedChar.add(s[right])
                right += 1
                maxLen = max(maxLen, len(usedChar))
        return maxLen

# 完全可以直接用list 但是速度很慢
class Solution0(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right = 0, 0
        usedChar = []
        maxLen = 0
        while left < len(s) and right < len(s):
            if s[right] in usedChar:
                while s[left] not in usedChar: # 直接找到这个重复出现的元素
                    left += 1
                usedChar.remove(s[left])
                left += 1
            else:
                usedChar.append(s[right])
                right += 1
                maxLen = max(maxLen, len(usedChar))
        return maxLen