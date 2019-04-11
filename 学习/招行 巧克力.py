# -*- coding: utf-8 -*-
"""
   File Name：     招行 巧克力
   Description :
   Author :       simon
   date：          19-4-9
"""

def helper(n):
    def DFS(num):
        global res
        if num <= 0:
            res += 1
            return
        for i in range(1, num+1):
            DFS(num-i)
    for i in range(6, n):
        DFS(n-i)
    return res % 666666666


if __name__ == '__main__':
    n = 12
    if n < 6:
        print 0
    else:
        print (2**(n-6)) % 6



