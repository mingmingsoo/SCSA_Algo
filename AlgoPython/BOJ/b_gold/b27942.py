n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]
eat = 0
path = []

r = c = n // 2 - 1  # 중심점
x = y = 2  # 가로, 세로 길이
while True:
    priority_list = []
    up = 0
    if r - 1 >= 0:
        for j in range(c, c + y):
            up += grid[r - 1][j]
        if up > 0:
            priority_list.append((up, 0))
    down = 0
    if r + x < n:
        for j in range(c, c + y):
            down += grid[r + x][j]
        if down > 0:
            priority_list.append((down, 1))
    left = 0
    if c - 1 >= 0:
        for i in range(r, r + x):
            left += grid[i][c - 1]
        if left > 0:
            priority_list.append((left, 2))
    right = 0
    if c + y < n:
        for i in range(r, r + x):
            right += grid[i][c + y]
        if right > 0:
            priority_list.append((right, 3))
    if not priority_list:
        break
    priority_list.sort(key=lambda x: (-x[0], x[1]))
    ele_eat, d = priority_list[0]
    eat += ele_eat
    path.append("UDLR"[d])
    if d == 0:  # up이였냐?
        for j in range(c, c + y):
            grid[r - 1][j] = 0
        r -= 1
        x += 1
    elif d == 1:  # down
        for j in range(c, c + y):
            grid[r + x][j] = 0
        x += 1
    elif d == 2:  # left
        for i in range(r, r + x):
            grid[i][c - 1] = 0
        c -= 1
        y += 1
    else:
        for i in range(r, r + x):
            grid[i][c + y] = 0
        y += 1
print(eat)
print("".join(path))

