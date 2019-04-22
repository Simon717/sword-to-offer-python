# -*- coding: utf-8 -*-
"""
   File Name：     京东 括号匹配方案
   Description :
   Author :       simon
   date：          19-4-12
"""
line = input().strip()
stack = []

res = []
tp = 0
for i in list(line):
    if i == '(':
        stack.append(i)
        prev = i
        continue
    if i == ')':
        stack.pop()
        prev = i
