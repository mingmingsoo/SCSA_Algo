'''
코드 리팩토링
'''
from collections import deque
def out(r, c, er, ec):
    visited = [[False] * n for i in range(n)]
    visited[r][c] = True
    q = deque([(r, c, 0)])
    while q:
        r, c, dist = q.popleft()
        if r == er and c == ec:
            return dist
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < n) or visited[nr][nc] or grid[nr][nc] == -1:
                continue
            visited[nr][nc] = True
            q.append((nr, nc, dist + 1))
    return -1


def find(r, c):
    user = []
    visited = [[False] * n for i in range(n)]
    visited[r][c] = True
    q = deque([(r, c, 0)])
    while q:
        q_size = len(q)
        for qs in range(q_size):
            r, c, dist = q.popleft()
            for k in range(4):
                nr = r + row[k]
                nc = c + col[k]
                if not (0 <= nr < n and 0 <= nc < n) or visited[nr][nc] or grid[nr][nc] == -1:
                    continue
                if grid[nr][nc] == 0:
                    visited[nr][nc] = True
                    q.append((nr, nc, dist + 1))
                elif grid[nr][nc] != 0:
                    visited[nr][nc] = True
                    q.append((nr, nc, dist + 1))
                    user.append((dist + 1, nr, nc, grid[nr][nc]))
        if user:
            user.sort()
            return user[0]
    return -1, -1, -1, -1


n, m, power = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            grid[i][j] = -1
r, c = map(lambda x: int(x) - 1, input().split())
end_info = {}
for mm in range(m):
    sr, sc, er, ec = map(lambda x: int(x) - 1, input().split())
    end_info[mm + 1] = (er, ec)
    grid[sr][sc] = mm + 1

row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]

for mm in range(m):
    used_power = next_r = next_c = next_numbering = -1
    if grid[r][c] != 0 and grid[r][c] != -1:
        used_power, next_r, next_c, next_numbering = 0, r, c, grid[r][c]
    else:
        used_power, next_r, next_c, next_numbering = find(r, c)
    if next_r == -1 or used_power > power:
        power = -1
        break
    grid[next_r][next_c] = 0
    power -= used_power
    r, c = next_r, next_c
    er, ec = end_info[next_numbering]
    used_power = out(r, c, er, ec)
    if used_power > power or used_power == -1:
        power = -1
        break
    power -= used_power
    power += used_power * 2
    r, c = er, ec
print(power)
