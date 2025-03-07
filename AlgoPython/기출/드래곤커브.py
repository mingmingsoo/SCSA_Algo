'''
문제설명
    드래곤 정보에 따라 끝점을 기준으로 시계 90도 회전
    격자 밖 걱정 안해도됨

구상
    이게 각 드래곤마다 그려주고 표시해야되는데...
    이게 어렵다.
    아 넘버링으로 하겠다. -> 아님.
입력
    드래곤 정보
주의 0과 101 시험해봐야함
'''
from collections import deque

size = 202  # 101
grid = [[0] * size for i in range(size)]
dragon_num = int(input())  # 드래곤 총 몇개인지

row = [0, -1, 0, 1]
col = [1, 0, -1, 0]

for d_n in range(dragon_num):

    c, r, d, last_level = map(int, input().split())

    if last_level == 0:
        grid[r][c] = 1
        # 일단 0세대 만들어주기
        nr = r + row[d]
        nc = c + col[d]

        grid[nr][nc] = 1
        continue
    # 시작점
    ele_grid = [[0] * size for i in range(size)]

    ele_grid[r][c] = 2 # 머리표시
    # 일단 0세대 만들어주기
    nr = r + row[d]
    nc = c + col[d]
    ele_grid[nr][nc] = 1
    level = 1
    while level <= last_level:
        # print(nr, nc)
        # 끝점을 기준으로 시계 90도 회전
        # 맵은 level+1
        # print("===============")
        # for _ in ele_grid:
        #     print(_)

        new_size = 101
        small_grid = [[0] * new_size for i in range(new_size)]
        for i in range(new_size):
            for j in range(new_size):
                small_grid[i][j] = ele_grid[i + nr - (new_size) // 2][j + nc - (new_size) // 2]


        for i in range(size):
            for j in range(size):
                if ele_grid[i][j] ==2:
                    ele_grid[i][j] = 1
        #
        # print("===============")
        # for _ in small_grid:
        #     print(_)

        new_small_grid = [[0] * (new_size) for i in range(new_size)]
        for i in range(new_size):
            for j in range(new_size):
                new_small_grid[i][j] = small_grid[new_size - j - 1][i]

        # print("===============")
        # for _ in new_small_grid:
        #     print(_)
        for i in range(new_size):
            for j in range(new_size):
                if new_small_grid[i][j] != 0:
                    ele_grid[i + nr - (new_size) // 2][j + nc - (new_size) // 2] = new_small_grid[i][j]

        level += 1

        for i in range(size):
            for j in range(size):
                if ele_grid[i][j] ==2:
                    ele_grid[i][j] = 1
                    nr = i
                    nc = j
                    break
        ele_grid[r][c] = 2
        # for _ in ele_grid:
        #     print(*_)

    for i in range(size):
        for j in range(size):
            if ele_grid[i][j] != 0:
                grid[i][j] = 1

ans = 0
for i in range(size - 1):
    for j in range(size - 1):
        if grid[i][j] == 1 and grid[i + 1][j] == 1 and grid[i][j + 1] == 1 and grid[i + 1][j + 1] == 1:
            ans += 1
# for _ in grid:
#     print(*_)
print(ans)
