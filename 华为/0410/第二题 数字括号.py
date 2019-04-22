# -*- coding: utf-8 -*-
"""
   File Name：     第二题 数字括号
   Description :
   Author :       simon
   date：          19-4-11
"""
# 在这里修改测试样例
test = """abc10(A)
"""

DEBUG = 1  # DEBUG = 1 用于本地调试 DEBUG = 0 用于线上提交
if DEBUG:
    with open('test.txt', 'w') as f:
        f.writelines(test)
    with open('test.txt', 'r') as f:
        lines = f.readlines()  # 利用txt文件的readlines 模拟sys.stdin.readlines() 不需要每一次手动输入测试样例 不然心态容易炸裂
else:
    import sys

    lines = sys.stdin.readlines()

line = lines[0].strip()
stack = []
for c in line:
    if c not in [']', '}', ')']:
        stack.append(c)
        continue
    # 遇到右括号
    tp = ''
    while stack[-1] not in ['(', '{', '[']:  # 压入一些看似没有用的东西是为了方便定届
        tp += stack.pop()
    stack.pop()
    num = ''
    while stack and stack[-1].isdigit():
        num += stack.pop()
    num = int(num[::-1])
    tp = tp * num
    stack.extend(list(tp[::-1])) # 必须转成list 按照元素存放
print(''.join(stack[::-1]))
