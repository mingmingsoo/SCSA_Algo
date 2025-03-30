'''
# 두번쨰 풀이 class 사용

'''
import heapq
from collections import deque


class Monster:
    def __init__(self, r, c, dist):
        self.r = r
        self.c = c
        self.dist = dist

    def __lt__(self, other):
        # 이런 방법이!
        return (self.dist, self.r, self.c) < (other.dist, other.r, other.c)

    # def __lt__(self, other):
    #     if self.dist == other.dist:
    #         if self.r == other.r:
    #             return self.c < other.c
    #         return self.r < other.r
    #     return self.dist < other.dist


n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]

r, c, level, eat = -1, -1, 2, 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 9:
            grid[i][j] = 0
            r, c = i, j

time = 0
row = [-1, 0, 1, 0]
col = [0, -1, 0, 1]
while True:

    target_q = []

    q = deque([(r, c, 0)])
    visited = [[False] * n for i in range(n)]
    visited[r][c] = True
    while q:
        r, c, dist = q.popleft()

        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < n) or visited[nr][nc]:
                continue
            if grid[nr][nc] == 0 or grid[nr][nc] == level:
                visited[nr][nc] = True
                q.append((nr, nc, dist + 1))
            elif grid[nr][nc] < level:
                visited[nr][nc] = True
                heapq.heappush(target_q, Monster(nr, nc, dist + 1))

    if not target_q:
        break

    monster = heapq.heappop(target_q)
    grid[monster.r][monster.c] = 0  # 먹는다
    eat += 1
    r = monster.r
    c = monster.c
    time += monster.dist
    if eat == level:
        level += 1
        eat = 0

print(time)
