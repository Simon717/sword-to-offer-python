# -*- coding: utf-8 -*-
"""
   File Name：     华为0403
   Description :
   Author :       simon
   date：          19-4-4
"""

# 在这里修改测试样例
test = """090sddd
asdff--
dfdsf
"""

DEBUG = 1 # DEBUG = 1 用于本地调试 DEBUG = 0 用于线上提交
if DEBUG:
    with open('test.txt', 'w') as f:
        f.writelines(test)
    with open('test.txt', 'r') as f:
        lines = f.readlines() # 利用txt文件的readlines 模拟sys.stdin.readlines() 不需要每一次手动输入测试样例 不然心态容易炸裂
else:
    import sys
    lines = sys.stdin.readlines().strip()

valid = []
invalid = []
for line in lines:
    line = line.strip()
    # 先判断是否非法
    flag = 0
    for s in line:
        if not s.isalnum():
            invalid.append(line)
            flag = 1
            break

    # 合法 去重
    if not flag:
        tpstr = ''
        for s in line:
            if s not in tpstr:
                tpstr += s
        valid.append(tpstr)

# print(valid)
# print(invalid)

# 循环右移10位
valid10 = []
for s in valid:
    split = 10 % len(s)
    valid10.append(s[split:]+s[:split])
# print(valid10)

# 排序
asc = []
for s in valid10:
    asc.append(''.join(sorted((s))))
# print(asc)
str1 = ' '.join(valid)
str2 = ' '.join(invalid)
str3 = ' '.join(valid10)
str4 = ' '.join(asc)
res = [str1, str2, str3, str4]
print(' '.join(res))