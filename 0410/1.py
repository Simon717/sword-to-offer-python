##第三题
test = """4 5
0 1 0 0 0
0 2 3 0 0
0 0 4 5 0
0 0 7 6 0
0 1 3 2
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
high = lines[1:-1]
sttend = lines[-1]

matrix = []
for line in high:
    line = line.strip().split(" ")
    matrix.append(list(map(int, line)))

sttend = sttend.strip().split(" ")
sttend = list(map(int, sttend))

rows, cols = len(matrix), len(matrix[0])
res = 0

def DFS(i, j, prev):
    global res
    if not 0 <= i < rows or not 0 <= j < cols or matrix[i][j] <= prev:
        return
    if [i, j] == [sttend[2], sttend[3]]:
        res += 1
        return
    if 0 <= i < rows and 0 <= j < cols and matrix[i][j] != float('-inf'):
        temp = matrix[i][j]
        matrix[i][j] = float('-inf')
        DFS(i + 1, j, temp)
        DFS(i - 1, j, temp)
        DFS(i, j + 1, temp)
        DFS(i, j - 1, temp)
        matrix[i][j] = temp


DFS(sttend[0], sttend[1], -1)
print(res)
