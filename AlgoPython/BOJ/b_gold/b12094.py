def gravity(grid):
    for j in range(n):
        while True:
            down = 0
            for i in range(0, n - 1, 1):
                if grid[i][j] == 0 and grid[i + 1][j] != 0:
                    grid[i][j], grid[i + 1][j] = grid[i + 1][j], grid[i][j]
                    down += 1
            if down == 0:
                break


def merge(grid):
    for j in range(n):
        i = 0
        while i < n - 1:
            if grid[i][j] == grid[i + 1][j]:
                grid[i][j] = grid[i][j] * 2
                grid[i + 1][j] = 0
                i += 1
            i += 1


def rotation(grid):
    grid_copy = [_[:] for _ in grid]
    for i in range(n):
        for j in range(n):
            grid[i][j] = grid_copy[n - j - 1][i]


def perm(idx):
    global ans, grid

    maxi = 0
    for _ in grid:
        maxi = max(maxi, max(_))
    if maxi * (2 ** (5 - idx)) <= ans:
        return

    if idx == 5:
        for _ in grid:
            ans = max(ans, max(_))
        return
    grid_origin = [_[:] for _ in grid]
    for k in range(4):
        for i in range(rot[k]):
            rotation(grid)
        gravity(grid)
        merge(grid)
        gravity(grid)
        perm(idx + 1)
        grid = [_[:] for _ in grid_origin]


n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]
row = [-1, 1, 0, 0]
col = [0, 0, -1, 1]
ans = 0

rot = [0, 2, 3, 1]
perm(0)
print(ans)
