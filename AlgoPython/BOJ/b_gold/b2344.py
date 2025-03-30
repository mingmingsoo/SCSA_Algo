n, m = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]

location = {}
dirs = {}
change = {1: 0, 0: 1, 2: 3, 3: 2}
num = 1
for i in range(n):
    j = -1
    location[(i, j)] = num
    dirs[(i, j)] = 1
    num += 1

for j in range(m):
    i = n
    location[(i, j)] = num
    dirs[(i, j)] = 0
    num += 1

for i in range(n - 1, -1, -1):
    j = m
    location[(i, j)] = num
    dirs[(i, j)] = 3
    num += 1

for j in range(m - 1, -1, -1):
    i = -1
    location[(i, j)] = num
    dirs[(i, j)] = 2
    num += 1

for key, value in location.items():
    d = dirs[key]
    r, c = key
    while True:
        nr = r + row[d]
        nc = c + col[d]

        if not (0 <= nr < n and 0 <= nc < m):
            print(location[(nr, nc)], end=" ")
            break
        if grid[nr][nc] == 1:
            d = change[d]

        r = nr
        c = nc
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]

location = {}
dirs = {}
change = {1: 0, 0: 1, 2: 3, 3: 2}
num = 1
for i in range(n):
    j = -1
    location[(i, j)] = num
    dirs[(i, j)] = 1
    num += 1

for j in range(m):
    i = n
    location[(i, j)] = num
    dirs[(i, j)] = 0
    num += 1

for i in range(n - 1, -1, -1):
    j = m
    location[(i, j)] = num
    dirs[(i, j)] = 3
    num += 1

for j in range(m - 1, -1, -1):
    i = -1
    location[(i, j)] = num
    dirs[(i, j)] = 2
    num += 1

for key, value in location.items():
    d = dirs[key]
    r, c = key
    while True:
        nr = r + row[d]
        nc = c + col[d]

        if not (0 <= nr < n and 0 <= nc < m):
            print(location[(nr, nc)], end=" ")
            break
        if grid[nr][nc] == 1:
            d = change[d]

        r = nr
        c = nc
