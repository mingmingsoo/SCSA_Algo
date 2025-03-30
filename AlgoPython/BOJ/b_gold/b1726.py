'''
이거 약간 구슬탈출 처럼..
'''
from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

sr, sc, sd = map(lambda x: int(x) - 1, input().split())
er, ec, ed = map(lambda x: int(x) - 1, input().split())

ans = 0
row = [0, 0, 1, -1]
col = [1, -1, 0, 0]

rotation_dict = {0: (2, 3), 1: (2, 3), 2: (0, 1), 3: (0, 1)}


def bfs(sr, sc, sd):
    global ans
    visited = [[[False] * 4 for i in range(m)] for i in range(n)]
    visited[sr][sc][sd] = True
    q = deque([(sr, sc, sd, 0)])

    while q:
        r, c, d, cnt = q.popleft()
        if (r, c, d) == (er, ec, ed):
            ans = cnt
            return
        for l in range(1, 4):
            nr = r + row[d] * l
            nc = c + col[d] * l
            if not (0 <= nr < n and 0 <= nc < m) or grid[nr][nc]:
                break
            if not visited[nr][nc][d]:
                visited[nr][nc][d] = True
                q.append((nr, nc, d, cnt + 1))
        for ro_d in rotation_dict[d]:
            if not visited[r][c][ro_d]:
                visited[r][c][ro_d] = True
                q.append((r, c, ro_d, cnt + 1))


bfs(sr, sc, sd)
print(ans)
