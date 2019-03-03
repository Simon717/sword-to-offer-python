# -*- coding: utf-8 -*-
"""
   File Name：     backtracking
   Description :
   Author :       simon
   date：          19-3-2
"""


def display(a):
    l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
    print([l[a[i]] for i in range(len(a))])


def backtracking(n, m, check, handle):
    def dfs(a, k): # a 当前已经确定的解 k 当前需要解决的位置
        for i in range(n): # 相当于开辟了n个分支 在每一个分支底下进行递归
            a[k] = i       # 第一个位置可能填入所有的可能值 继续向下递归
            if check(a, k):     # 检查当前解是否合法
                if k == m - 1:  # 所有位置处理完毕
                    handle(a)
                else:
                    dfs(a, k + 1) # 处理下个位置

    a = [0] * m
    dfs(a, 0)


def backtracking0(n, m, check, handle):
    k, a = 0, [-1] * m
    while k >= 0:
        print(a)
        a[k] += 1
        while a[k] < n and not check(a, k):
            a[k] += 1
        if a[k] == n or k == m:
            k -= 1
        else:
            if k == m - 1:
                handle(a)
            else:
                k += 1
                a[k] = -1


def counter(n, m):
    backtracking0(n, m, lambda a, k: True, print)


def permutation(n, m):
    def check(a, k):
        for i in range(k):
            if a[i] == a[k]:
                return False
        return True

    backtracking(n, m, check, display)


def combination(n, m):
    def check(a, k):
        for i in range(k):
            if a[i] >= a[k]:
                return False
        return True

    backtracking(n, m, check, display)


def nqueen(n):
    def check(a, k):
        for i in range(k):
            if a[i] == a[k] or abs(a[i] - a[k]) == k - i:
                return False
        return True

    backtracking(n, n, check, print)


def deep_first_search(g):
    def check(a, k):
        if k == 0:
            return True
        for i in range(k):
            if a[i] == a[k]:
                return False
        for i in range(k - 1, -1, -1):
            if g[a[i]][a[k]] == 1:
                return True
        return False

    def dfs(n, check, handle):
        k, a = 0, [-1 for i in range(n)]
        while k >= 0:
            a[k] += 1
            while a[k] < n and not check(a, k):
                a[k] += 1
            if a[k] == n:
                k -= 1
            else:
                if k == n - 1:
                    handle(a)
                else:
                    k += 1
                    a[k] = -1

    n = len(g)
    dfs(n, check, display)


graph = [
    [0, 1, 1, 1, 0],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0]
]

if __name__ == '__main__':
    print("counter =>")
    counter(3, 2)
    # #
    # print("permutation =>")
    # permutation(3, 2)
    #
    # print("combination =>")
    # combination(3, 2)
    # #
    # print("nqueen =>")
    # nqueen(4)
    #
    # print("paths =>")
    # deep_first_search(graph)