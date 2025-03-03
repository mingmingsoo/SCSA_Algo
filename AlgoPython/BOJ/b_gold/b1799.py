import sys

sys.setrecursionlimit(10 ** 5)

n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]

b1_list = []
b2_list = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            if (i + j) % 2 == 0:
                b1_list.append((i, j))
            else:
                b2_list.append((i, j))

X = [False] * (2 * n)
Y = [False] * (2 * n)
ans = 0


def dfs(b_list, idx, cnt):
    global ans
    if idx == len(b_list):
        ans = max(ans, cnt)
        return

    r, c = b_list[idx]
    x = r + c
    y = r - c
    if not X[x] and not Y[y]:
        X[x] = True
        Y[y] = True
        dfs(b_list, idx + 1, cnt + 1)  # 놔
        X[x] = False
        Y[y] = False

    dfs(b_list, idx + 1, cnt)  # 안놔


dfs(b1_list, 0, 0)
dfs(b2_list, 0, ans)
print(ans)
