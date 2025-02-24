'''
구상
카운트를 남겨서 진행
'''
from collections import deque

n,m = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
time = 0

def all_melting():
    for i in range(n):
        for j in range(m):
            if grid[i][j]==1:
                return False
    return True

row = [-1,1,0,0]
col = [0,0,1,-1]

def bfs(sr,sc):
    visited = [[False]*m for i in range(n)]
    visited[sr][sc] = True
    q = deque([(sr,sc)])
    counting_grid = [[0]*m for i in range(n)]

    while q:
        r, c = q.popleft()

        for k in range(4):
            nr = r+row[k]
            nc = c+col[k]
            if not(0<=nr<n and 0<=nc<m):
                continue
            if not visited[nr][nc] and grid[nr][nc]==0:
                q.append((nr,nc))
                visited[nr][nc] = True
            if grid[nr][nc]==1:
                counting_grid[nr][nc] +=1
    # print("--------------")
    # for _ in counting_grid:
    #     print(*_)

    # grid 가 1 이고 count_grid가 2이상인 애들은 녹임
    for i in range(n):
        for j in range(m):
            if grid[i][j]==1 and counting_grid[i][j]>=2:
                grid[i][j]=0
    # print("--------------")
    # for _ in grid:
    #     print(*_)

while True:
    if(all_melting()):
        break
    time+=1
    bfs(0,0)
print(time)