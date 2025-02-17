from collections import deque

grid = [[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]

n = len(grid) # 행
m = len(grid[0]) # 열

arr = [0]*m
visited = [[False]*m for i in range(n)]
row = [-1,1,0,0]
col = [0,0,1,-1]

def bfs(r,c):
    global eat, left,right
    q = deque([(r,c)])
    visited[r][c] = True

    while q:
        r,c = q.popleft()
        left = min(left,c)
        right = max(right,c)
        for k in range(4):
            nr = r+row[k]
            nc = c+col[k]
            if(not(0<=nr<n and 0<=nc<m)):
                continue
            if not visited[nr][nc] and grid[nr][nc]==1:
                visited[nr][nc] = True
                q.append((nr,nc))
                eat+=1

for i in range(n):
    for j in range(m):
        if not visited[i][j] and grid[i][j] ==1:
            left = j
            right = j
            eat = 1
            bfs(i,j)
            print(i,j,eat)
            for d in range(left, right+1):
                arr[d]+=eat
print(arr)
print(max(arr))