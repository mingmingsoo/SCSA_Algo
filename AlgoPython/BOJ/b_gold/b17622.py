n, limit = map(int, input().split())
grid = [[9] + list(map(int, input().split())) + [9] for i in range(n)]  # 9로 패딩
m = n + 2
grid[n - 1][m - 1] = 5
ans = 0
row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]
dirs = {0: (0, 1, 4), 1: (1, 3, 5), 2: (2, 3, 4), 3: (0, 2, 5)}
possible_go = {0: (1, 2), 1: (2, 3), 2: (0, 1), 3: (0, 3), 4: (0, 2), 5: (1, 3), 9: (1, 5)}

def valid():
    global ans
    r, c, er, ec = 0, 0, n - 1, m - 1
    visited = [[False] * m for i in range(n)]
    visited[r][c] = True
    while True:
        ans += 1
        if (r, c) == (er, ec):
            return True
        possible = False
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < m) or (grid[nr][nc] == 9 and (nr, nc) != (er, ec)):
                continue
            if not visited[nr][nc] and grid[nr][nc] in dirs[k]:  # 이거면 갈 수 있음
                visited[nr][nc] = True
                r = nr
                c = nc
                possible = True
                break
        if not possible:
            break
    return False


if limit == 0:
    if (valid()):
        print(ans - 2)
    else:
        print(-1)
else:
