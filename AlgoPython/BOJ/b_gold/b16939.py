'''
문제설명
    면 6개 담고 돌릴 수 있는 조합 확인
구상
    조합
    1.오른쪽 왼쪽
    2.뚜겅 바닥
    3. 앞면 뒷면
'''

grid = [[[0] * 2 for i in range(2)] for i in range(6)]
# 면 채워~
color = list(map(int, input().split()))

idx = 0  # 면
for i in range(0, 24, 4):
    grid[idx][0][0] = color[i]
    grid[idx][0][1] = color[i + 1]
    grid[idx][1][0] = color[i + 2]
    grid[idx][1][1] = color[i + 3]
    idx += 1
ans = 0


def is_same(grid_tmp):
    # 모든 면의 색깔이 같으면
    for h in range(6):
        first = grid_tmp[h][0][0]
        for i in range(2):
            for j in range(2):
                if (first != grid_tmp[h][i][j]):
                    return False
    return True


def is_left(grid):
    grid_copy = [[[0] * 2 for i in range(2)] for i in range(6)]

    for h in range(6):
        for i in range(2):
            for j in range(2):
                grid_copy[h][i][j] = grid[h][i][j]

    # 왼쪽 회전. 뒤쪽으로
    # 왼쪽 값 바뀌고 # 왼쪽 면 회전.
    grid_copy[0][0][0] = grid[1][0][0]
    grid_copy[0][1][0] = grid[1][1][0]
    grid_copy[1][0][0] = grid[2][0][0]
    grid_copy[1][1][0] = grid[2][1][0]
    grid_copy[2][0][0] = grid[5][1][1]
    grid_copy[2][1][0] = grid[5][0][1]
    grid_copy[5][1][1] = grid[0][0][0]
    grid_copy[5][0][1] = grid[0][1][0]

    for i in range(2):
        for j in range(2):
            grid_copy[3][i][j] = grid[3][j][1 - i]

    return grid_copy


def is_right(grid):
    grid_copy = [[[0] * 2 for i in range(2)] for i in range(6)]

    for h in range(6):
        for i in range(2):
            for j in range(2):
                grid_copy[h][i][j] = grid[h][i][j]

    grid_copy[0][0][1] = grid[1][0][1]
    grid_copy[0][1][1] = grid[1][1][1]
    grid_copy[1][0][1] = grid[2][0][1]
    grid_copy[1][1][1] = grid[2][1][1]
    grid_copy[2][0][1] = grid[5][1][0]
    grid_copy[2][1][1] = grid[5][0][0]
    grid_copy[5][1][0] = grid[0][0][1]
    grid_copy[5][0][0] = grid[0][1][1]

    for i in range(2):
        for j in range(2):
            grid_copy[4][i][j] = grid[4][1 - j][i]

    return grid_copy


def is_front(grid):
    grid_copy = [[[0] * 2 for i in range(2)] for i in range(6)]

    for h in range(6):
        for i in range(2):
            for j in range(2):
                grid_copy[h][i][j] = grid[h][i][j]

    grid_copy[0][1][0] = grid[3][1][1]  # 3 16
    grid_copy[0][1][1] = grid[3][0][1]  # 4 14
    grid_copy[3][1][1] = grid[2][0][1]  # 10
    grid_copy[3][0][1] = grid[2][0][0]  # 9
    grid_copy[2][0][1] = grid[4][0][0]  # 17
    grid_copy[2][0][0] = grid[4][1][0]  # 19
    grid_copy[4][0][0] = grid[0][1][0]  # 3
    grid_copy[4][1][0] = grid[0][1][1]  # 4

    for i in range(2):
        for j in range(2):
            grid_copy[1][i][j] = grid[1][1 - j][i]  # 시계

    return grid_copy


def is_back(grid):
    grid_copy = [[[0] * 2 for i in range(2)] for i in range(6)]

    for h in range(6):
        for i in range(2):
            for j in range(2):
                grid_copy[h][i][j] = grid[h][i][j]

    grid_copy[0][0][0] = grid[3][1][0]  # 1 15
    grid_copy[0][0][1] = grid[3][0][0]  # 2 13
    grid_copy[3][1][0] = grid[2][1][1]  # 12
    grid_copy[3][0][0] = grid[2][1][0]  # 11
    grid_copy[2][1][1] = grid[4][0][1]  # 18
    grid_copy[2][1][0] = grid[4][1][1]  # 20
    grid_copy[4][0][1] = grid[0][0][0]  # 1
    grid_copy[4][1][1] = grid[0][0][1]  # 2

    for i in range(2):
        for j in range(2):
            grid_copy[5][i][j] = grid[5][j][1 - i]  # 반시계

    return grid_copy


def is_top(grid):
    grid_copy = [[[0] * 2 for i in range(2)] for i in range(6)]

    for h in range(6):
        for i in range(2):
            for j in range(2):
                grid_copy[h][i][j] = grid[h][i][j]

    grid_copy[1][0][0] = grid[3][0][0]  # 5 13
    grid_copy[1][0][1] = grid[3][0][1]  # 6 14
    grid_copy[3][0][0] = grid[5][0][0]  # 21
    grid_copy[3][0][1] = grid[5][0][1]  # 22
    grid_copy[5][0][0] = grid[4][0][0]  # 17
    grid_copy[5][0][1] = grid[4][0][1]  # 18
    grid_copy[4][0][0] = grid[1][0][0]  # 5
    grid_copy[4][0][1] = grid[1][0][1]  # 6

    for i in range(2):
        for j in range(2):
            grid_copy[0][i][j] = grid[0][j][1 - i]  # 반시계

    return grid_copy


def is_bottom(grid):
    grid_copy = [[[0] * 2 for i in range(2)] for i in range(6)]

    for h in range(6):
        for i in range(2):
            for j in range(2):
                grid_copy[h][i][j] = grid[h][i][j]

    grid_copy[1][1][0] = grid[3][1][0]  # 7 15
    grid_copy[1][1][1] = grid[3][1][1]  # 8 16
    grid_copy[3][1][0] = grid[5][1][0]  # 23
    grid_copy[3][1][1] = grid[5][1][1]  # 24
    grid_copy[5][1][0] = grid[4][1][0]  # 19
    grid_copy[5][1][1] = grid[4][1][1]  # 20
    grid_copy[4][1][0] = grid[1][1][0]  # 7
    grid_copy[4][1][1] = grid[1][1][1]  # 8

    for i in range(2):
        for j in range(2):
            grid_copy[2][i][j] = grid[2][1 - j][i]  # 시계

    return grid_copy


def valid():
    global ans

    grid_tmp = is_left(grid)
    if (is_same(grid_tmp)):
        ans = 1
        return

    grid_tmp2 = is_left(grid_tmp)

    grid_tmp3 = is_left(grid_tmp2)
    if (is_same(grid_tmp3)):
        ans = 1
        return

    grid_tmp = is_right(grid)
    if (is_same(grid_tmp)):
        ans = 1
        return

    grid_tmp2 = is_right(grid_tmp)

    grid_tmp3 = is_right(grid_tmp2)
    if (is_same(grid_tmp3)):
        ans = 1
        return

    grid_tmp = is_top(grid)
    if (is_same(grid_tmp)):
        ans = 1
        return

    grid_tmp2 = is_top(grid_tmp)

    grid_tmp3 = is_top(grid_tmp2)
    if (is_same(grid_tmp3)):
        ans = 1
        return

    grid_tmp = is_bottom(grid)
    if (is_same(grid_tmp)):
        ans = 1
        return

    grid_tmp2 = is_bottom(grid_tmp)

    grid_tmp3 = is_bottom(grid_tmp2)
    if (is_same(grid_tmp3)):
        ans = 1
        return

    grid_tmp = is_front(grid)
    if (is_same(grid_tmp)):
        ans = 1
        return

    grid_tmp2 = is_front(grid_tmp)

    grid_tmp3 = is_front(grid_tmp2)
    if (is_same(grid_tmp3)):
        ans = 1
        return

    grid_tmp = is_back(grid)
    if (is_same(grid_tmp)):
        ans = 1
        return

    grid_tmp2 = is_back(grid_tmp)

    grid_tmp3 = is_back(grid_tmp2)
    if (is_same(grid_tmp3)):
        ans = 1
        return


valid()

print(ans)
