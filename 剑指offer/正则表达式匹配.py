# -*- coding: utf-8 -*-
"""
   File Name：     正则表达式匹配
   Description :
   Author :       simon
   date：          19-3-17
"""
'''
请实现一个函数用来匹配包括'.'和'*'的正则表达式。
模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
'''


# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        if not s or not pattern:  # 00 01 10
            return False
        # 如果s和pattern匹配, 直接True
        if s == pattern:
            return True
        # 如果pattern为'', 因为s和pattern不相等, 直接False
        elif pattern == '':
            return False

        # 当s为'', 如果pattern为'.', 则返回True
        # 当s为'', 如果pattern长度为1且不为'.', 或者pattern第二个字符不是*, 则pattern不可能为空, 返回False
        # 若pattern长度不为1, 且第二个字符为*, pattern还有空的可能, 从第三个字符开始迭代
        elif s == '':
            if pattern == ".":
                return True
            elif len(pattern) == 1 or pattern[1] != '*':
                return False
            else:
                return self.match(s, pattern[2:])

        # 如果pattern长度不小于二, 而且pattern的第二个字符不是*的情况下
        # 当 pattern[0] 不等于s[0], 且不为 . 的时候, s和pattern必不相等
        # 否则, s 和 pattern 都右移一位, 继续比较
        if len(pattern) >= 2 and pattern[1] != '*':
            if s[0] != pattern[0] and pattern[0] != '.':
                return False
            else:
                return self.match(s[1:], pattern[1:])
        # 如果pattern长度不小于2, 且pattern第二个字符为*的情况下
        # 如果s[0]不等于pattern[0], 且pattern[0]不为 . , 那么第一位比较不成功, pattern必须后移两位继续比较后面是否能和s第一位匹配
        # 如果s[0]等于pattern[0], 或者pattern[0]为 . , 第一位匹配, 那么会有
        # 1. aaa 和 a*a 这种情况, 星号代表了多个a, 因此s需要不断右移一位继续比较
        # 2. a 和 a*a 中这情况, 这时候星号代表0个a, 因此s不需要右移, pattern需要右移两位
        # 3. abc 和 a*bc 这种情况, 星号代表了1个a, s右移一位, pattern右移两位继续比较
        elif len(pattern) >= 2 and pattern[1] == '*':
            if s[0] != pattern[0] and pattern[0] != '.':
                return self.match(s, pattern[2:])
            else:
                return self.match(s[1:], pattern) or self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:])
        # 除去上述pattern不小于2情况, 只剩下pattern等于1的情况, 因此如果pattern为".", 而且s长度为1, 返回True
        elif pattern == '.' and len(s) == 1:
            return True
        return False


# -*- coding:utf-8 -*-
"""
通过率 96%
剩下的超过递归深度
"""


class Solution_:
    # s, pattern都是字符串
    def match(self, s, pattern):
        if not s and not pattern:  # 0 0
            return True
        if s and not pattern:  # 1 0
            return False

        if len(pattern) >= 2 and pattern[1] == '*':
            if pattern[0] == '.':  # .*
                return self.match(s, pattern[2:]) or self.match(s[1:], pattern)
            else:  # a*
                if s and pattern[0] == s[0]:  # ab a*
                    return self.match(s[1:], pattern) or self.match(s, pattern[2:])  # 替代0个a or 替代1个a
                else:  # bb a*
                    return self.match(s, pattern[2:])
        elif pattern[0] == '.':
            if s:
                return self.match(s[1:], pattern[1:])
            else:
                return False
        else:
            if s and pattern[0] == s[0]:
                return self.match(s[1:], pattern[1:])
            else:
                return False


"""
牛客AC 

ab a*
1. 耗尽* 
    相当于没使用 ab ''
    抵消了一次 b ''
2. 没有耗尽
    b a*
"""


class Solution__:
    def match(self, s, pattern):
        if not s and not pattern:  # 0 0
            return True
        if s and not pattern:  # 1 0 没有模式只有字符 肯定无法完成匹配
            return False

        # 01  11
        if len(pattern) >= 2 and pattern[1] == '*':
            if s and (pattern[0] == s[0] or pattern[0] == '.'):
                return self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern)
            else:
                return self.match(s, pattern[2:])
        elif s and (pattern[0] == s[0] or pattern[0] == '.'):
            return self.match(s[1:], pattern[1:])
        else:
            return False


if __name__ == '__main__':
    a = 'aba'
    p = '.*'
    solu = Solution__()
    print(solu.match(a, p))


#
# if __name__ == '__main__':
#     s = Solution()
#     print(s.match('aaa', 'a*a'))


# when there is a "*", either you can skip this pattern (appears 0 times),
# or you can match one or more times
class Solution(object):
    def isMatch(self, text, pattern):
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    res = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j + 1 < len(pattern) and pattern[j + 1] == '*': # 有*
                        res = dp(i, j + 2) or first_match and dp(i + 1, j) # *相当于没出现 or 第一个字符匹配 and *使用一次
                    else: # 没有*
                        res = first_match and dp(i + 1, j + 1) # 第一个字符必须匹配 and 考虑后面

                memo[i, j] = res # 存下当前解
            return memo[i, j]

        return dp(0, 0)
