n, m = map(int, input().split())
size = max(n, m)
grid = [[" "] * m for i in range(n)]
tmpQ = list(map(int, input().split()))
tmpK = list(map(int, input().split()))
tmpP = list(map(int, input().split()))
QNum = tmpQ.pop(0)
KNum = tmpK.pop(0)
PNum = tmpP.pop(0)
for i in range(QNum):
    grid[tmpQ.pop(0) - 1][tmpQ.pop(0) - 1] = "Q"
for i in range(KNum):
    grid[tmpK.pop(0) - 1][tmpK.pop(0) - 1] = "K"
for i in range(PNum):
    grid[tmpP.pop(0) - 1][tmpP.pop(0) - 1] = "P"

SafeGrid = [[0] * m for i in range(n)]
row = [1, 0, -1, 0, 1, 1, -1, -1]
col = [0, 1, 0, -1, 1, -1, 1, -1]
row2 = [-2, -1, 1, 2, 1, 2, -2, -1]
col2 = [-1, -2, -2, -1, 2, 1, 1, 2]


def Qcheck(r, c):
    for k in range(8):
        for l in range(1, size):
            nr = r + row[k] * l
            nc = c + col[k] * l
            if (0 <= nr < n and 0 <= nc < m and grid[nr][nc] == " "):
                SafeGrid[nr][nc] = 1
            else:
                break


def Kcheck(r, c):
    for k in range(8):
        nr = r + row2[k]
        nc = c + col2[k]
        if (0 <= nr < n and 0 <= nc < m and grid[nr][nc] == " "):
            SafeGrid[nr][nc] = 1


for i in range(n):
    for j in range(m):
        if (grid[i][j] == "Q"):
            SafeGrid[i][j] = 1
            Qcheck(i, j)
        elif (grid[i][j] == "K"):
            SafeGrid[i][j] = 1
            Kcheck(i, j)
        elif (grid[i][j] == "P"):
            SafeGrid[i][j] = 1

safe = 0
for i in range(n):
    for j in range(m):
        if (SafeGrid[i][j] == 0):
            safe += 1
print(safe)
