# -*- coding: utf-8 -*-
"""
   File Name：     体育场 back
   Description :
   Author :       simon
   date：          19-4-13
"""

# -*- coding: utf-8 -*-
"""
   File Name：     京东 体育场
   Description :
   Author :       simon
   date：          19-4-13
"""
# 在这里修改测试样例
test = """6
2 1
3 2
4 3
5 2
6 1
"""

DEBUG = 1 # DEBUG = 1 用于本地调试 DEBUG = 0 用于线上提交
if DEBUG:
    with open('test.txt', 'w') as f:
        f.writelines(test)
    with open('test.txt', 'r') as f:
        lines = f.readlines() # 利用txt文件的readlines 模拟sys.stdin.readlines() 不需要每一次手动输入测试样例 不然心态容易炸裂
else:
    import sys
    lines = sys.stdin.readlines()

n = int(lines[0].strip())
lines = lines[1:]
matrix = []
for line in lines:
    tp = line.strip().split()
    matrix.append(list(map(int, tp)))

queue = [1]
for i, line in enumerate(matrix):
    if 1 in line:
        tp = matrix[i]
        del matrix[i]
        break
tp.remove(1)
left = tp[0]

tp = []
for i, line in enumerate(matrix):
    if 1 in line:
        tp = matrix[i]
        del matrix[i]
        break
if tp:
    tp.remove(1)
    right = tp[0]
else:
    right = 0

# print(left, right) # 2 6
# print(matrix)

cnt_left, cnt_right = 0, 0
queue = [left]
while queue:
    # print(queue)
    cnt_left += len(queue)
    # print(cnt_left)
    tp_queue = []
    for root in queue:
        # child = []
        for i, line in enumerate(matrix):
            if root in line:
                # child.append(line)
                # del matrix[i]
                matrix[i].remove(root)
                tp_queue.append(matrix[i][0])
                matrix[i].pop()
        # print(tp_queue)
        # for c in child:
        #     # c.remove(root)
        #     tp_queue.append(c[0])
    queue = tp_queue

# print(cnt_left)
if right:
    # queue = [right]
    # while queue:
    #     cnt_right += len(queue)
    #     tp_queue = []
    #     for root in queue:
    #         child = []
    #         for i, line in enumerate(matrix):
    #             if root in line:
    #                 child.append(line)
    #                 del matrix[i]
    #                 # matrix[i].remove(root)
    #         for c in child:
    #             c.remove(root)
    #             tp_queue.append(c[0])
    #     queue = tp_queue
    queue = [right]
    while queue:
        # print(queue)
        cnt_right += len(queue)
        tp_queue = []
        for root in queue:
            # child = []
            for i, line in enumerate(matrix):
                if root in line:
                    # child.append(line)
                    # del matrix[i]
                    matrix[i].remove(root)
                    tp_queue.append(matrix[i][0])
                    matrix[i].pop()
            # print(tp_queue)
            # for c in child:
            #     # c.remove(root)
            #     tp_queue.append(c[0])
        queue = tp_queue

# print(cnt_right)
print(max(cnt_right, cnt_left))