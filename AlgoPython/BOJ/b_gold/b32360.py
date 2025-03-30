from collections import deque

n, m = map(int, input().split())
inner, outer = map(int, input().split())

grid = [list(input()) for i in range(n)]

sr = sc = er = ec = -1

for i in range(n):
    for j in range(m):
        if grid[i][j] == "S":
            sr, sc = i, j
        elif grid[i][j] == "E":
            er, ec = i, j

row = [0, -1, 1, 0, 0]
col = [0, 0, 0, 1, -1]
ans = -1


def bfs(sr, sc, er, ec):
    global ans
    visited = [[[False] * 101 for i in range(m)] for i in range(n)]
    visited[sr][sc][0] = True
    q = deque([(sr, sc, 0, 0)])
    while q:
        r, c, bad, cnt = q.popleft()
        # print(r, c, bad, cnt)
        if (r == er and c == ec):
            ans = cnt
            return

        for k in range(5):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < m) or grid[nr][nc] == "#":
                continue
            if grid[nr][nc] in ("S", "H"):
                next_bad = max(0, bad - inner)
                if not visited[nr][nc][next_bad]:
                    visited[nr][nc][next_bad] = True
                    q.append((nr, nc, next_bad, cnt + 1))
            elif grid[nr][nc] in (".", "E"):
                next_bad = min(100, bad + outer)
                if next_bad >= 100:
                    continue
                if not visited[nr][nc][next_bad]:
                    visited[nr][nc][next_bad] = True
                    q.append((nr, nc, next_bad, cnt + 1))


bfs(sr, sc, er, ec)
print(ans)
