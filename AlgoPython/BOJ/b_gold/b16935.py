'''
문제 설명
    1번 연산: 상하반전
    2번 연산: 좌우반전
    3번 연산: 시계방향
    4번 연산: 반시계회전
    5번 연산:
    12 -> 41
    43    32
    6번 연산:
    12 -> 23
    43    14
입력
    n,m,order
    맵
    orderlist
구상
    1000번까지 회전은 괜찮아서
    성실히 구현
'''
n, m, tmp = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
order_list = list(map(int, input().split()))

def updown():
    grid_copy = [_[:] for _ in grid]
    for i in range(n):
        for j in range(m):
            grid[i][j] = grid_copy[n - i - 1][j]


def leftright():
    grid_copy = [_[:] for _ in grid]
    for j in range(m):
        for i in range(n):
            grid[i][j] = grid_copy[i][m - j - 1]

def right_rotation():
    global grid, n, m

    grid_copy = [_[:] for _ in grid]
    grid = [[0] * n for i in range(m)]

    for i in range(m):
        for j in range(n):
            grid[i][j] = grid_copy[n - j - 1][i]
    n, m = m, n

def left_rotation():
    global grid, n, m

    grid_copy = [_[:] for _ in grid]
    grid = [[0] * n for i in range(m)]

    for i in range(m):
        for j in range(n):
            grid[i][j] = grid_copy[j][m - i - 1]
    n, m = m, n

def zigzag():
    # 5번 연산:
    # 12 -> 41
    # 43    32
    grid_copy = [_[:] for _ in grid]

    for i in range(n // 2):
        for j in range(m // 2):
            grid[i][j] = grid_copy[i + n // 2][j]
    for i in range(n // 2, n):
        for j in range(m // 2):
            grid[i][j] = grid_copy[i][j + m // 2]
    for i in range(n // 2):
        for j in range(m // 2, m):
            grid[i][j] = grid_copy[i][j - m // 2]
    for i in range(n // 2, n):
        for j in range(m // 2, m):
            grid[i][j] = grid_copy[i - n // 2][j]

for order in order_list:
    if order == 1:
        updown()
    elif order == 2:
        leftright()
    elif order == 3:
        right_rotation()
    elif order == 4:
        left_rotation()
    elif order == 5:
        zigzag()
    elif order == 6:
        zigzag()
        zigzag()
        zigzag()

for row in grid:
    print(*row)
