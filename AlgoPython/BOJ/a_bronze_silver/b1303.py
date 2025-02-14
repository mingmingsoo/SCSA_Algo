'''
문제 설명
    뭉쳐있으면 제곱만큼 힘을냄
'''
from collections import deque

m,n = map(int, input().split())

grid = [list(input()) for i in range(n)]

w = 0
b = 0

visited = [[False] * m for i in range(n)]

def bfs(r,c,team):
    row = [-1,1,0,0]
    col = [0,0,1,-1]
    q = deque([(r,c)])
    visited[r][c] = True
    cnt = 0
    while q:
        r, c = q.popleft()
        cnt+=1

        for k in range(4):
            nr = r+row[k]
            nc = c+col[k]
            if(not (0<=nr<n and 0<=nc<m)):
                continue
            if not visited[nr][nc] and grid[nr][nc] == team:
                visited[nr][nc] =True
                q.append((nr,nc))
    return cnt

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            group = bfs(i,j,grid[i][j])
            if(grid[i][j]=="W"):
                w += group**2
            else:
                b+=group**2

print(w,b)