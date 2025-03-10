'''
문제설명
    토마토처럼 퍼진다.
    N개중에 M개 고른다
    -1 검사 필요
'''
import itertools
from collections import deque
from itertools import combinations

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

arr = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            arr.append((i, j))
            grid[i][j] = 0

pick_list = itertools.combinations(arr, m)
ans = 50 * 50 + 1
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]
def isOk():
    for i in range(n):
        for j in range(n):
            if grid[i][j] ==0:
                return False
    return True
for _ in pick_list:
    origin_grid = [__[:] for __ in grid]
    q = deque()
    for r, c in _:
        grid[r][c] = 2
        q.append((r, c, 0))
    ele_ans = 0
    # visited 필요없다
    while q:
        r, c, time = q.popleft()
        ele_ans = time
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0<=nr<n and 0<=nc<n):
                continue
            if grid[nr][nc] == 0:
                grid[nr][nc] = 2
                q.append((nr,nc,time+1))
    if isOk():
        ans = min(ans,ele_ans)
    grid = origin_grid
if ans == 50 * 50 + 1:
    print(-1)
else:
    print(ans)