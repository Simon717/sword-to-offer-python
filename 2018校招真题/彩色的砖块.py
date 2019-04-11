# -*- coding: utf-8 -*-
"""
   File Name：     彩色的砖块
   Description :
   Author :       simon
   date：          19-4-8
"""
s = input().strip()
s = list(s)
s = set(s)
if len(s) > 2:
    print(0)
else:
    print(len(s))