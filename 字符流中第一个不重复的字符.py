# -*- coding: utf-8 -*-
"""
   File Name：     字符流中第一个不重复的字符
   Description :
   Author :       simon
   date：          19-3-20
"""


# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.dic = {}
        self.queue = []

    def FirstAppearingOnce(self):
        # write code here
        for c in self.queue:  # 这里有bug 不知道是不是边弹出 边遍历会出现bug
            if self.dic[c] != 1:
                self.queue.pop(0)
            else:
                return c
        return '#'

    def Insert(self, char):
        # write code here
        if char not in self.dic.keys():
            self.dic[char] = 0
        self.dic[char] += 1
        self.queue.append(char)


# -*- coding:utf-8 -*-
class Solution_:
    # 返回对应char
    def __init__(self):
        self.dic = {}
        self.queue = [] # 先进先出 不满足出现次数为1时直接删除元素

    def FirstAppearingOnce(self):
        # write code here
        while len(self.queue) and self.dic[self.queue[0]] != 1: # 持续检查第一个元素是否满足条件 不满足条件直接删掉
            self.queue.pop(0)
        if not len(self.queue): return '#'
        return self.queue[0]

    def Insert(self, char):
        # write code here
        if char not in self.dic.keys():
            self.dic[char] = 0
        self.dic[char] += 1
        self.queue.append(char)