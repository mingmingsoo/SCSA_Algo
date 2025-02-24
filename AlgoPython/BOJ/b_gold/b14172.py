'''
일단 부분집합으로 검사해
'''

n, m = map(int, input().split())
grid = [[0] * m for i in range(n)]

ans = 0


def isOk(grid):
    for i in range(n - 1):
        for j in range(m - 1):
            if (grid[i][j] == 1 and grid[i + 1][j] == 1 and grid[i][j + 1] == 1 and grid[i + 1][j + 1] == 1):
                return True
    return False


def dfs(idx):
    global ans

    if (idx == n * m):

        if (isOk(grid)):
            ans += 1
        return

    r = idx // m
    c = idx % m

    grid[r][c] = 1  # 일단놔
    dfs(idx + 1)
    grid[r][c] = 0  # 아냐 안놔
    dfs(idx + 1)


dfs(0)
print(2 ** (n * m) - ans)
