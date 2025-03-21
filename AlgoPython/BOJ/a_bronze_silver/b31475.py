'''
아래로 하나 만들어서 회전.
'''
n, m = map(int, input().split())
dirs = input()
if dirs == "R" or dirs == "L":
    n, m = m, n

visited = [[False] * m for i in range(n)]
for i in range(n):
    for j in range(m // 2 + 1, m):
        visited[i][j] = True

grid = [[0] * m for i in range(n)]

# 0,m//2~ n//2,m//4 달팽이 만들기
r, c = 0, m // 2
d = 0
num = 1
grid[r][c] = num
row = [1, 0, -1, 0]
col = [0, -1, 0, 1]
while num < n * (m // 2 + 1):
    num += 1
    if not (0 <= r + row[d] < n and 0 <= c + col[d] < m // 2 + 1) or visited[r + row[d]][c + col[d]] or \
            grid[r + row[d]][c + col[d]]:
        d = (d + 1) % 4

    r = r + row[d]
    c = c + col[d]
    grid[r][c] = num

# 잉제 복사

for j in range(m // 2 + 1, m):
    for i in range(n):
        grid[i][j] = grid[i][m - j - 1]

# 잉제 회전
rotation_dict = {"U": 0, "L": 3, "D": 2, "R": 1}  # 회전 시킬 횟수


def rotation():
    global n, m, grid
    new_grid = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            new_grid[i][j] = grid[n - j - 1][i]

    n, m = m, n
    grid = new_grid


for ro in range(rotation_dict[dirs]):
    rotation()
for _ in grid:
    print(*_)
