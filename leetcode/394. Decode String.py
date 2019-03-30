# -*- coding: utf-8 -*-
"""
   File Name：     394. Decode String
   Description :
   Author :       simon
   date：          19-3-27
"""

"""
递归
思路必须清晰..
"""
class Solution_(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''

        def decode(s):
            if '[' not in s: # 无法解码 直接return出去
                return s

            # 可解码
            # 字符区 数字区 [。。。] 找到三个部分的index就可以  abc123[...]abc...

            left = s.find('[')
            cnt = 1
            i = left + 1
            while i < len(s) and cnt > 0 : # 每一个while循环 都要记得 i++
                if s[i] == '[': cnt += 1
                if s[i] == ']': cnt -= 1  # 见过多少个左就也得见过多少个右 才算是匹配的括号
                i += 1
            right = i - 1

            # 字符区
            i = 0
            while i < left and not s[i].isdigit():
                i += 1

            # 数字区
            num = int(s[i:left])

            return s[:i] + num * decode(s[left+1:right]) + decode(s[right+1:])

        return decode(s)
"""
堆栈解
实在太秀了
"""
class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 0:
            return ''

        stack = [['', 1]] # [['', 1], ['a', 3], ['c', 2]]  --> [['', 1], ['acc', 3]]
        num = 0
        for i, c in enumerate(s):
            print()
            if c.isdigit():
                num = num * 10 + int(c)
            elif c.isalpha():
                stack[-1][0] += c
            elif c == '[':  # 遇到左括号 压入堆栈
                stack.append(['', num])
                num = 0
            elif c == ']':  # 遇到右括号 弹出堆栈 将字符串乘上次数之后 加入到上一级的字符串中
                prev_str, cnt = stack.pop()
                stack[-1][0] += prev_str * cnt
        return stack[0][0]

"""
递归解
"""
class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 0:
            return ''

        def helper(s):
            open_idx = s.find('[')
            if open_idx != -1: # -1 表示 开括号不存在
                open_cnt = 1
                idx = open_idx + 1
                while idx < len(s) and open_cnt > 0:  # 找到与第一个 '[' 匹配的 ']'
                    if s[idx] == '[':
                        open_cnt += 1
                    elif s[idx] == ']':
                        open_cnt -= 1
                    idx += 1
                close_idx = idx - 1
                tmp_str = ''
                cnt, i = 0, 0
                while i < open_idx and not s[i].isdigit():  # 找到数字前可能有的字符串，见test case2
                    tmp_str += s[i]
                    i += 1
                cnt = int(s[i:open_idx])
                return tmp_str + cnt * helper(s[open_idx + 1:close_idx]) + helper(s[close_idx + 1:])
            else:
                return s

        return helper(s)

if __name__ == '__main__':
    test = '3[a]'
    test = '"3[z]2[2[y]pq4[2[jk]e1[f]]]ef"'
    # test = "10[s]"
    solu = Solution_()
    print(solu.decodeString(test))

