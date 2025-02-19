import math

'''
90도 회전이 아니라
한칸 옮기는 것임.
# 반시계 회전.
'''
import copy

n, m, rotation = map(int, input().split())

orignin_n = n
orignin_m = m
grid = [list(map(int, input().split())) for i in range(n)]
ro_grid = [[0] * m for i in range(n)]
row = [0, 1, 0, -1]
col = [1, 0, -1, 0]
cnt = 0

while cnt < rotation:
    r, c = 0, 0
    d = 0
    start_r = 0
    start_c = 0
    n = orignin_n
    m = orignin_m
    while True:
        if (r == orignin_n // 2 or c == orignin_m // 2):
            break  # 회전 중지

        while True:
            if (ro_grid[r][c] != 0):
                r += 1
                c += 1
                n -= 1
                m -= 1
                start_r += 1
                start_c += 1
                d = 0
                break

            nr = r + row[d]
            nc = c + col[d]

            if (start_r <= nr < n and start_c <= nc < m):
                ro_grid[r][c] = grid[nr][nc]
                r = nr
                c = nc
            else:
                d = (d + 1) % 4
    cnt += 1
    grid = [_[:] for _ in ro_grid]
    ro_grid = [[0] * orignin_m for i in range(orignin_n)]
for _ in grid:
    print(*_)

# num = 1
# for i in range(300):
#     for j in range(300):
#         print(num, end = " ")
#         num+=1
#     print()
