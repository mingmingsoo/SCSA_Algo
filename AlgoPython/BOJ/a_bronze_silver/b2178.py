'''
1 이동 가능 0 불가능
시작점, 도착점 최소 거리 계산
항상 도착할 수 있다고함
'''
from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input())) for i in range(n)]

def bfs(startR, startC, endR, endC):
    row = [-1,1,0,0]
    col = [0,0,-1,1]
    q = deque([(startR,startC,0)])
    visited = [[False] * m for i in range(n)]
    visited[startR][startC] = True
    while q:
        r,c,cnt = q.popleft()
        if(r==endR and c == endC):
            print(cnt+1)
            return

        for k in range(4):
            nr = r+row[k]
            nc = c+col[k]
            if(0<=nr<n and 0<=nc<m and not visited[nr][nc] and grid[nr][nc]==1):
                q.append((nr,nc,cnt+1))
                visited[nr][nc] = True


bfs(0,0,n-1,m-1)