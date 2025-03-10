'''
원숭이는 K번만큼만 뛸 수 있음.
'''
from collections import deque

limit = int(input())
m, n = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
ans = -1

row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]

row2 = [-2, -1, 1, 2, 2, 1, -1, -2]
col2 = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs():
    global ans
    visited = [[-1] * m for i in range(n)]
    visited[0][0] = 0  # 안뛰었다.
    q = deque([(0, 0, 0, 0)])  # 좌표와 동작수, 뛴 횟수
    while q:
        r, c, cnt, jump = q.popleft()
        if r == n - 1 and c == m - 1:
            ans = cnt
            return
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < m) or grid[nr][nc] == 1:
                continue
            if visited[nr][nc] != -1 or visited[nr][nc] < jump:
                visited[nr][nc] = jump
                q.append((nr, nc, cnt + 1, jump))
        if jump < limit:
            for k in range(8):
                nr = r + row2[k]
                nc = c + col2[k]
                if not (0 <= nr < n and 0 <= nc < m) or grid[nr][nc] == 1:
                    continue
                if visited[nr][nc] == -1 or visited[nr][nc] > jump:
                    visited[nr][nc] = jump + 1
                q.append((nr, nc, cnt + 1, jump + 1))


bfs()
print(ans)
