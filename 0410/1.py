test = """2 12345678945 abc"""

DEBUG = 1 # DEBUG = 1 用于本地调试 DEBUG = 0 用于线上提交
if DEBUG:
    with open('test.txt', 'w') as f:
        f.writelines(test)
    with open('test.txt', 'r') as f:
        lines = f.readlines() # 利用txt文件的readlines 模拟sys.stdin.readlines() 不需要每一次手动输入测试样例 不然心态容易炸裂
else:
    import sys
    lines = sys.stdin.readlines()
if not lines:
    pass
else:
    array =lines[0].strip().split(' ')
    n = int(array[0])
    abc = array[1:]
    res = []
    # s = '00000000'
    for i in abc:
        while len(i)>=8:
            res.append(i[:8])
            i = i[8:]
        if i:
            res.append(i+'0'*(8-len(i)))
    a=sorted(res)
    a = " ".join(a)
    print(a)

# import sys
#
# ss = sys.stdin().readline().strip()
# # ss = 'abc2(A)'
# num = []
# middle = []
#
# for i in range(len(ss)):
#     # if ss[i].isdigit():
#     if ord(ss[i]) >= ord('0') and ord(ss[i]) <= ord('9'):
#         num.append(int(ss[i]))
#         continue
#     if ss[i] not in [')', ']', '}']:
#         middle.append(ss[i])
#         continue
#     cur = ''
#     while middle[-1] not in ['(', '[', '{']:
#         a = middle.pop()
#         cur += a
#     middle.pop()
#     cur = cur[::-1] * num.pop()
#     middle.extend(list(cur))
# middle = "".join(middle)[::-1]
# print(middle)


##第二题##
import sys

ss = sys.stdin.readline().strip()
# ss = 'abc2(A)'
num = []
middle = []

for i in range(len(ss)):
    # if ss[i].isdigit():
    if ord(ss[i]) >= ord('0') and ord(ss[i]) <= ord('9'):
        num.append(int(ss[i]))
        continue
    if ss[i] not in [')', ']', '}']:
        middle.append(ss[i])
        continue
    cur = ''
    while middle[-1] not in ['(', '[', '{']:
        a = middle.pop()
        cur += a
    middle.pop()
    cur = cur[::-1] * num.pop()
    middle += list(cur)
middle = "".join(middle)[::-1]
print(middle)


##第三题
test = """4 5
0 1 0 0 0
0 2 3 0 0
0 0 4 5 0
0 0 7 6 0
0 1 3 2
"""
#
DEBUG = 1 # DEBUG = 1 用于本地调试 DEBUG = 0 用于线上提交
if DEBUG:
    with open('test.txt', 'w') as f:
        f.writelines(test)
    with open('test.txt', 'r') as f:
        lines = f.readlines() # 利用txt文件的readlines 模拟sys.stdin.readlines() 不需要每一次手动输入测试样例 不然心态容易炸裂
else:
    import sys
    lines = sys.stdin.readlines()
high = lines[1:-1]
sttend=lines[-1]
high_ =[]
for l in high:
    l=l.strip().split(" ")
    high_.append(list(map(int,l)))
sttend = sttend.strip().split(" ")
sttend = list(map(int,sttend))
rows,cols = len(high_),len(high_[0])
res = 0
def DFS(i,j):
    global res
    if[i,j] == [sttend[2],sttend[3]]:
        res +=1
        return
    if 0<=i <rows and 0<=j<cols and high_[i][j]!=float('-inf'):
        temp =high_[i][j]
        high_[i][j] =float('-inf')
        if 0<= i+1<rows and 0<= j<cols and high_[i+1][j]>temp:
            DFS(i+1,j)
        if 0<= i-1<rows and 0<= j<cols and high_[i-1][j]>temp:
            DFS(i-1,j)
        if 0<= i<rows and 0<= j+1<cols and high_[i][j+1]>temp:
            DFS(i,j+1)
        if 0<= i<rows and 0<= j-1<cols and high_[i][j-1]>temp:
            DFS(i,j-1)
        high_[i][j]=temp
DFS(sttend[0],sttend[1])
print(res)
