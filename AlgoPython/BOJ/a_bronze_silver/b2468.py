'''
풀었던 문제 ...

비가 오는 높이에 따라
비에 잠기지 않는 영역의 군집의 최대 갯수는?

비의 양은 배열의 최소-1~ 최대만 확인하면 되는데
최소로 하면 다 잠겨서 안전 영역 0
최소-1로 하면 다 안잠겨서 안전 영역 1

'''
from collections import deque

n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]

minH = 101
maxH = 0
for i in range(n):
    for j in range(n):
        if(grid[i][j]>maxH):
            maxH = grid[i][j]
        if(grid[i][j]<minH):
            minH = grid[i][j]

# print(maxH, minH)
ans = 1 # minH-1를 범위에 두지말고 ans = 1 로 하기.
row = [-1,1,0,0]
col = [0,0,1,-1]

def bfs(h, i, j):
    global total
    q = deque([(i,j,0)])
    visited[i][j] = True
    while q:
        r,c,d = q.popleft()
        for k in range(4):
            nr = r+row[k]
            nc = c+col[k]
            if(0<=nr<n and 0<=nc<n and not visited[nr][nc] and grid[nr][nc]>h):
                q.append((nr,nc,d+1))
                visited[nr][nc] = True
for h in range(minH, maxH): # 비의 범위  maxH + 1 이면 0이라 탐색 X
    visited = [[False] * n for i in range(n)]
    total = 0
    for i in range(n):
        for j in range(n):
            if (not visited[i][j] and grid[i][j] > h): # 안전 영역이면
                total+=1
                bfs(h,i,j)
    # for i in range(n):
    #     for j in range(n):
    #         if(not visited[i][j]): # 잠겼어
    #             print("X", end = " ")
    #         else:
    #             print("O", end=" ")
    #     print()
    ans = max(ans,total)
print(ans)

