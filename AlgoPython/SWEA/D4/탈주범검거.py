'''
# 두번째 풀이 dict 사용
visited True 갯수를 세라
bfs
'''
from collections import deque

row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]
T = int(input())
connect = {0: (1, 2, 5, 6), 1: (1, 3, 6, 7), 2: (1, 2, 4, 7), 3: (1, 3, 4, 5)}
next = {1: (0, 1, 2, 3), 2: (0, 2), 3: (1, 3), 4: (0, 1), 5: (1, 2), 6: (2, 3), 7: (0, 3)}

for tc in range(T):

    n, m, r, c, time = map(int, input().split())
    grid = [list(map(int, input().split())) for i in range(n)]

    visited = [[False] * m for i in range(n)]
    visited[r][c] = True


    def bfs(sr, sc):
        q = deque([(sr, sc, 1)])

        while q:
            r, c, t = q.popleft()
            if t >= time:
                return

            for k in next[grid[r][c]]:
                nr = r + row[k]
                nc = c + col[k]
                if not (0 <= nr < n and 0 <= nc < m) or grid[nr][nc] == 0 or visited[nr][nc]:
                    continue
                if (grid[nr][nc] in connect[k]):
                    q.append((nr, nc, t + 1))
                    visited[nr][nc] = True


    bfs(r, c)
    ans = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                ans += 1
    print(f"#{tc + 1} {ans}")
