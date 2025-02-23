'''
문제설명
    0,0 ->n-1, m-1까~쥐
구상
    k개를 따로 관리
    visited 3차원으로 관리
'''
from collections import deque

limit = int(input())
m, n = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

ans = -1


def bfs(sr, sc, er, ec):
    global ans
    visited = [[[False] * (limit+1) for i in range(m)] for i in range(n)] # 일반으로 갔냐 그냥으로 갔냐
    visited[sr][sc][0] = True
    q = deque([(sr, sc, 0, 0)])
    row = [0, 0, -1, 1]
    col = [1, -1, 0, 0]
    jump_row = [2, 1, -1, -2, -2, -1, 1, 2]
    jump_col = [1, 2, 2, 1, -1, -2, -2, -1]

    while q:
        r,c,cnt,jump= q.popleft()
        if(r==er and c==ec):
            ans = cnt
            return
        # jump에 상관없이 4방으로 이동 가능.
        for k in range(4):
            nr = r+row[k]
            nc = c+col[k]

            if not(0<=nr<n and 0<= nc<m):
                continue
            if not visited[nr][nc][jump] and grid[nr][nc]!=1:
                visited[nr][nc][jump] = True
                q.append((nr,nc,cnt+1,jump))

        if(jump<limit):
            for k in range(8):
                nr = r + jump_row[k]
                nc = c + jump_col[k]
                if not (0 <= nr < n and 0 <= nc < m):
                    continue
                if not visited[nr][nc][jump+1] and grid[nr][nc]!=1:
                    visited[nr][nc][jump+1] = True
                    q.append((nr, nc, cnt + 1, jump+1))





bfs(0, 0, n - 1, m - 1)
print(ans)