'''
일단 수영장처럼 풀어보기
'''
from collections import deque

m,n = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

total = 0
row = [-1,1,0,0]
col = [0,0,1,-1]
def bfs(i,j,origin_h):
    global total
    visited = set([(i,j,origin_h)])
    q = deque([(i,j,origin_h)])
    minH = 1000000000
    while q:
        r,c,h = q.popleft()

        for k in range(4):
            nr = r+row[k]
            nc = c+col[k]

            if not(0<=nr<n and 0<=nc<m):
                return
            if (nr,nc,grid[nr][nc]) not in visited and grid[nr][nc]<=origin_h:
                q.append((nr,nc,grid[nr][nc]))
                visited.add((nr,nc,grid[nr][nc]))
            if grid[nr][nc] > origin_h:
                minH = min(minH, grid[nr][nc])

    for x,y,hh in visited:
        total += (minH - hh)
        grid[x][y] = minH

for i in range(1,n-1):
    for j in range(1,m-1):
            bfs(i,j,grid[i][j])
print(total)
