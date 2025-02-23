'''
문제설명
    mod를 사용해라
    bfs 갯수 구하기
'''
from collections import deque

n,m = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

visited = [[False]*m for i in range(n)]
ans = 0
row = [-1,1,0,0]
col = [0,0,1,-1]
def bfs(r,c):
    q = deque([(r,c)])
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = (r+row[k]+n)%n
            nc = (c+col[k]+m)%m

            if not visited[nr][nc] and grid[nr][nc]==0:
                visited[nr][nc] = True
                q.append((nr,nc))


for i in range(n):
    for j in range(m):
        if grid[i][j]==0 and not visited[i][j]:
            # print(i,j)
            visited[i][j]= True
            bfs(i,j)
            ans +=1
print(ans)
