'''
수영장 다시
'''
from collections import deque

n,m = map(int, input().split())
grid= [list(map(int, input())) for i in range(n)]

total = 0
row = [-1,1,0,0]
col = [0,0,1,-1]
def bfs(i,j,h):
    global total
    # 나보다 작거나 같으면 담기.
    visited = set()
    visited.add((i,j,h))
    q = deque([(i,j,h)])
    minH = 10 # 채울 때 필요함

    while q:
        r,c,height = q.popleft()

        for k in range(4):
            nr = r+row[k]
            nc = c+col[k]

            if not(0<=nr<n and 0<=nc<m):
                return

            if grid[nr][nc]<=h and (nr,nc,grid[nr][nc]) not in visited:
                visited.add((nr,nc,grid[nr][nc]))
                q.append((nr,nc,grid[nr][nc]))
            if grid[nr][nc]>h:
                minH = min(minH,grid[nr][nc])
    for x,y,hh in visited:
        total += (minH-hh)
        grid[x][y] = minH

for i in range(1,n-1):
    for j in range(1,m-1):
        bfs(i,j,grid[i][j])
print(total)