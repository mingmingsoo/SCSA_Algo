'''
조건
0: 이동가능
1: 이동불가능
2: 목표지점

출력
1. 최단거리 출력
2. 도달 불가능시 -1 출력
'''
from collections import deque

n,m = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

endR = -1
endC = -1
found = False
for i in range(n):
    for j in range(m):
        if(grid[i][j]==2):
            endR = i
            endC = j
            found = True
            break
    if(found):
        break
bfsGrid = [[0] * m for i in range(n)]
row = [-1,1,0,0]
col = [0,0,1,-1]

def bfs(i, j):
    q = deque([(i,j,0)])
    visited = set([(i,j)])

    while q:
        r,c,cnt = q.popleft()
        bfsGrid[r][c] = cnt
        for k in range(4):
            nr = r+row[k]
            nc = c+col[k]
            if(0<=nr<n and 0<=nc<m
                    and (nr, nc) not in visited
                    and grid[nr][nc]!=0):
                q.append((nr,nc,cnt+1))
                visited.add((nr,nc))
    return

bfs(endR,endC)
for i in range(0,n):
    for j in range(0,m):
        if(grid[i][j]==1 and bfsGrid[i][j]==0):
            bfsGrid[i][j] = -1

for row in bfsGrid:
    for ele in row:
        print(ele, end = " ")
    print()