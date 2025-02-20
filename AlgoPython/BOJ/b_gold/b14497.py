'''
문제 설명
    주난이의 점프로 친구들을 넘어뜨릴때까지 퍼져나간다.
    한번의 짬푸는 한 겹의 친구들을 쓰러뜨린다.
    즉 한번의 짬뿌는 네방향으로 친구를 만날때 까지 쓰러뜨린다.
'''
import heapq
from collections import deque

n, m = map(int, input().split())
r, c, er, ec = map(lambda x: int(x) - 1, input().split())
grid = [list(input()) for i in range(n)]

for i in range(n):
    for j in range(m):
        if grid[i][j] == "1":
            grid[i][j] = 1
        elif grid[i][j] == "0":
            grid[i][j] = 0
        elif grid[i][j] == "*":
            grid[i][j] = 0
        elif grid[i][j] == "#":
            grid[i][j] = 1

d = [[90001] * m for i in range(n)]


def bfs(r, c):
    global ans
    row = [-1, 1, 0, 0]
    col = [0, 0, 1, -1]
    q = [(0, r, c)]

    d[r][c] = 0

    while q:
        cnt, r, c = heapq.heappop(q)

        if (r == er and c == ec):
            break

        if d[r][c] > cnt:
            continue

        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < m):
                continue

            if d[nr][nc] > cnt + grid[nr][nc]:
                d[nr][nc] = cnt + grid[nr][nc]
                q.append((cnt + grid[nr][nc], nr, nc))


bfs(r, c)

print(d[er][ec])
