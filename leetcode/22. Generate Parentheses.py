# -*- coding: utf-8 -*-
"""
   File Name：     22. Generate Parentheses
   Description :
   Author :       simon
   date：          19-3-12
"""
"""
思路： 插入法
未能实现 
"""
#
# class Solution(object):
#     def generateParenthesis(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#         if not n:
#             return []
#
#         self.res = []
#
#         def DFS(path):
#             if len(path)//2 == n:
#                 self.res.append(path)
#                 return
#
#             idx = findValidIndex(path)
#             for i in idx:
#                 tp = path[:]
#                 tp.insert(i, ')')
#                 tp.insert(i, '(')
#                 DFS(tp)
#
#         def findValidIndex(path): # TODO 不好实现
#             return
#
#         DFS([])
#         return self.res



"""
官方解

left, right 表示左括号和右括号的数目

仍然是标准的BT问题
我们需要学习的是怎么写check函数 
根据不同的情况放置不能的元素到解的整个路径上
"""

class Solution_BT(object):
    def generateParenthesis(self, N):
        res = []

        def backtrack(S, left, right):
            if len(S) == 2 * N:
                res.append(S)
                return

            if left < N: # 只要左括号没有放完 当前就还可以放左括号
                backtrack(S + '(', left + 1, right)
            if right < left: # 只要右括号的数目小于当前左括号的数目 就还可以放置右括号
                backtrack(S + ')', left, right + 1)

        backtrack("", 0, 0)
        return res

"""
选择： '(' ')'
限制： left < N  right < left
结束条件： 达到长度 必然合法 因为在限制条件下已经保证了其合法性
"""
class Solution:
    def generateParenthesis(self, N):
        def DFS(path, left, right):
            if len(path) == 2*N:
                res.append(path)
                return

            if left < N:
                DFS(path+'(', left+1, right)

            if right < left:
                DFS(path+')', left, right+1)
        res = []
        DFS('', 0, 0)
        return res

# class Solution_Brute_Force(object):
#     def generateParenthesis(self, n):
#         def generate(A):
#             if len(A) == 2*n:
#                 if valid(A):
#                     res.append("".join(A))
#             else:
#                 A.append('(')
#                 generate(A)
#                 A.pop()
#                 A.append(')')
#                 generate(A)
#                 A.pop()
#
#         def valid(A):
#             ballence = 0
#             for c in A:
#                 if c == '(': ballence += 1
#                 else: ballence -= 1
#                 if ballence < 0: return False
#             return ballence == 0
#
#         res = []
#         generate([])
#         return res

"""
基本思想：
f(n) 怎么由f(n-1)而来 递归
将f(n-1)中的每一个括号插入到一个括号中 一共有两个位置 ({}){} 就是图中花括号表示的位置
"""
# class Solution_Closure(object):
#     def generateParenthesis(self, N):
#         if N == 0: return [''] # 虽然return 是list 但是使用for loop直接得到里面的字符串
#
#         res = []
#         for c in range(N):
#             for left in self.generateParenthesis(c):
#                 for right in self.generateParenthesis(N-1-c):
#                     res.append('({}){}'.format(left, right))
#         return res

if __name__ == '__main__':
    solu = Solution_Closure()
    print(solu.generateParenthesis(3))