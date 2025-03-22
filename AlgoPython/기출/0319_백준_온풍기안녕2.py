'''
온풍기 안녕 쉽게쉽게 가자
머리 싹 지우고 다시 19:40~20:11
'''
from collections import deque


def valid():
    for r, c in valid_set:
        if grid[r][c] < limit:
            return False
    return True


def edge():
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                if grid[i][j] > 0:
                    grid[i][j] -= 1


def control():
    plus_grid = [[0] * m for i in range(n)]

    for i in range(n):
        for j in range(m):
            total_minus = 0
            for k in range(4):
                nr = i + row[k]
                nc = j + col[k]
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] < grid[i][j] and block[i][j][k]:
                    minus = grid[i][j] - grid[nr][nc]
                    plus_grid[nr][nc] += minus // 4
                    total_minus += minus // 4
            plus_grid[i][j] -= total_minus

    for i in range(n):
        for j in range(m):
            grid[i][j] += plus_grid[i][j]


def warm():
    # new_grid 만들어서 한번에 합쳐주기
    for r, c, d in robot_set:
        new_grid = [[0] * m for i in range(n)]
        nr = r + row[d]
        nc = c + col[d]  # 여긴 무조건 5가 될 수 있음
        new_grid[nr][nc] = 5

        q = deque([(nr, nc, 4)])
        while q:
            r, c, power = q.popleft()
            if power == 0:
                break
            # 5 바로 밑에
            nr = r + row[d]
            nc = c + col[d]
            if 0 <= nr < n and 0 <= nc < m and block[r][c][d]:
                new_grid[nr][nc] = power
                q.append((nr, nc, power - 1))

            for side_d in dir_dict[d]:

                nr1 = r + row[side_d]  # 4를 가기 위해서 가야하는 사이드
                nc1 = c + col[side_d]

                nr2 = nr1 + row[d]  # 진짜 그 4
                nc2 = nc1 + col[d]

                if 0 <= nr2 < n and 0 <= nc2 < m and block[r][c][side_d] and block[nr1][nc1][d]:
                    new_grid[nr2][nc2] = power
                    q.append((nr2, nc2, power - 1))

        for i in range(n):
            for j in range(m):
                grid[i][j] += new_grid[i][j]


n, m, limit = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
block = [[[True] * 4 for i in range(m)] for i in range(n)]
block_num = int(input())
row = [0, 0, -1, 1]
col = [1, -1, 0, 0]
# 0  1   2  3
# 우 좌 위 아래
for b in range(block_num):
    r, c, d = map(int, input().split())
    r -= 1
    c -= 1
    if d == 0:
        block[r][c][2] = False  # r,c에선 위로 못감
        block[r - 1][c][3] = False  # r-1,c에선 아래로 못감
    else:
        block[r][c][0] = False  # r,c 에선 오른쪽으로 못감
        block[r][c + 1][1] = False  # r,c+1에선 왼쪽으로 못감

valid_set = set()
robot_set = set()
dir_dict = {0: (2, 3), 1: (2, 3), 2: (1, 0), 3: (1, 0)}

for i in range(n):
    for j in range(m):
        if grid[i][j] == 5:
            valid_set.add((i, j))
            grid[i][j] = 0
        elif 0 < grid[i][j] < 5:
            robot_set.add((i, j, grid[i][j] - 1))
            grid[i][j] = 0
ans = 101

for choco in range(1, 101):

    warm()  # 퍼져나가
    control()  # 온도 조절
    edge()  # 바깥쪽 온도 감소
    if valid():  # 검증
        ans = choco
        break
print(ans)
