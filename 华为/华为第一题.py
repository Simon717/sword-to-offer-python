# -*- coding: utf-8 -*-
"""
   File Name：     华为第一题
   Description :
   Author :       simon
   date：          19-4-3
"""

"""
利用txt文件的readlines 模拟sys.stdin.readlines() 
不需要每一次手动输入测试样例 不然心态容易炸裂
"""

# 在这里修改测试样例
test = """3
2,5,6,7,9,5,7
1,7,4,3,4
"""

DEBUG = 0 # DEBUG = 1 用于本地调试 DEBUG = 0 用于线上提交
if DEBUG:
    with open('test.txt', 'w') as f:
        f.writelines(test)
    with open('test.txt', 'r') as f:
        lines = f.readlines() # 利用txt文件的readlines 模拟sys.stdin.readlines() 不需要每一次手动输入测试样例 不然心态容易炸裂
else:
    import sys
    lines = sys.stdin.readlines()

step = int(lines[0])
arrays = []
for line in lines[1:]:
    array = [int(x) for x in line.strip().split(',')]
    arrays.append(array)

res = []
while arrays:
    i = 0
    while i < len(arrays): #  必须使用while循环 否则数组越界
        res.append(arrays[i][:min(step, len(arrays[i]))])
        del arrays[i][:min(step, len(arrays[i]))]

        if not arrays[i]: # 如果删掉当前行 不用 i++
            del arrays[i]
        else: #  如果当前行没有被删除 需要 i++
            i += 1

# 因为print list 会有中括号 得想办法干掉中括号
# 一种方式是手动生成要打印的字符串
out = []
for arr in res:
    for num in arr:
        out.append(str(num))
print(','.join(out))

# 另一种是改变print函数的参数
tp = res[-1][-1]  # 留下最后一个元素 因为最后一个元素不需要，
res[-1].pop()
for arr in res:
    for num in arr:
        print(num, end=',') # 默认的print函数 end = '\n'
print(tp)