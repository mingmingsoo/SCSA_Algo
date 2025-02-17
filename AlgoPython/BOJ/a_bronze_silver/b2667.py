'''
구상
    bfs로 집 갯수 센다.
    그리고 담는다.
출력
    총 단지수와 각 단지마다 집 갯수
'''
from collections import deque

n = int(input())
grid = [list(map(int, input())) for i in range(n)]
visited = [[False] * n for i in range(n)]

ans = []
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]


def bfs(r, c):
    visited[r][c] = True
    q = deque([(r, c)])
    ele = 0
    while q:
        r, c = q.popleft()
        ele += 1
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if (not (0 <= nr < n and 0 <= nc < n)):
                continue
            if not visited[nr][nc] and grid[nr][nc] == 1:
                visited[nr][nc] = True
                q.append((nr, nc))
    return ele


for i in range(n):
    for j in range(n):
        if not visited[i][j] and grid[i][j] == 1:
            ele = bfs(i, j)
            ans.append(ele)
ans.sort() # 이거빼먹어서 1회틀림
print(len(ans))
for num in ans:
    print(num)