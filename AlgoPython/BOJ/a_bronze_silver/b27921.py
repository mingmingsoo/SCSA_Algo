n1, m1 = map(int, input().split())
grid1 = [list(input()) for i in range(n1)]

n2, m2 = map(int, input().split())
grid2 = [list(input()) for i in range(n2)]

# 맵 큰거
grid = [[0] * 30 for i in range(30)]

# grid1을 박아두겠음
for i in range(10, 10 + n1):
    for j in range(10, 10 + m1):
        if (grid1[i - 10][j - 10] == "O"):
            grid[i][j] = -1
coin = 1000
for i in range(0, 30 - n2 + 1):
    for j in range(0, 30 - m2 + 1):
        # 얘네가 시작점
        grid_copy = [_[:] for _ in grid]
        for x in range(i, i + n2):
            for y in range(j, j + m2):
                if (grid2[x - i][y - j] == "O"):
                    grid_copy[x][y] *= -1
        ele_coin = 0
        for row in grid_copy:
            ele_coin += row.count(-1)
        coin = min(coin, ele_coin)
print(coin)
