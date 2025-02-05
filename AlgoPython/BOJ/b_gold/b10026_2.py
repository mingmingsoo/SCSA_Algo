'''
풀었던 문제

정상인이 보는 군집의 갯수와
색약이 보는 군집의 갯수 출력

해결 방법
색약이 보는 2차원 배열을 새로 생성해서 bfs로 돌리거나
bfs에서 q에 넣어주는 조건을 r or g로 하면 된다.

'''
from collections import deque
def count(grid):
    colors = 0
    visited = [[False] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if(not visited[i][j]):
                bfs(i,j,grid[i][j],grid,visited)
                colors+=1
    return colors

def bfs(i, j, color, grid,visited):
    q = deque([(i, j)])
    visited[i][j] = True

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if (not (0 <= nr < n and 0 <= nc < n)):
                continue
            if (not visited[nr][nc] and grid[nr][nc]==color):
                q.append((nr,nc))
                visited[nr][nc] = True

n = int(input())
rgb = [list(input()) for i in range(n)]

rb = [[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        if(rgb[i][j]=="B"): # 파란색만 제대로 볼 수 있음
            rb[i][j] = "B"
        else:
            rb[i][j] = "G"

row = [-1,1,0,0]
col = [0,0,1,-1]



print(count(rgb),count(rb))
