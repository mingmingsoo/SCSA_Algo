'''
배열을 한칸씩 돌리는데
mod 찾아내기
'''
import sys

input = sys.stdin.readline

cnt = 0


def rotation(grid):
    global cnt
    N, M = n, m
    r = c = 0
    while not (r == n // 2 or c == m // 2): # 대박 and가 아니규 or임 ;;;;
        mod = (N - r) * 2 + (M - c - 2) * 2
        if mod == 0:
            new_rot = 0
        else:
            new_rot = rot % mod
        for idx in range(new_rot):
            tmp = grid[r][c]
            for j in range(c, M - 1):
                grid[r][j] = grid[r][j + 1]
            for i in range(r, N - 1):
                grid[i][M - 1] = grid[i + 1][M - 1]
            for j in range(M - 1, c, -1):
                grid[N - 1][j] = grid[N - 1][j - 1]
            for i in range(N - 1, r, -1):
                grid[i][c] = grid[i - 1][c]
            grid[r + 1][c] = tmp

        r += 1
        c += 1
        N -= 1
        M -= 1
    return grid


n, m, rot = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
grid = rotation(grid)
for _ in grid:
    print(*_)
