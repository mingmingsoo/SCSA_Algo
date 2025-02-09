'''
시뮬레이션 +bfs
녹이는 시뮬레이션
두 덩어리 이상이 되는지 검사할 때 bfs사용
'''
from collections import deque
import sys
input = sys.stdin.readline
# 덩어리가 몇개인지 검사
def valid():
    total = 0
    for i in range(n):
        for j in range(m):
            if(not visited[i][j] and grid[i][j]!=0):
                bfs(i,j)
                total +=1
    return total
# 덩어리인애들을 visited 해준다.
def bfs(i, j):
    visited[i][j] = True
    q = deque([(i,j)])
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r+row[k]
            nc = c+col[k]
            if(not(0<=nr<n and 0<=nc<m)):
                continue
            if(not visited[nr][nc] and grid[nr][nc]!=0):
                q.append((nr,nc))
                visited[nr][nc] = True
# 녹이는 과정.
# copy를 하지 않으면 녹으면서 위나 옆 즉 근방에서 녹은애들의 영향을 받을 수 있어서
# copy로 딱 녹는 만큼만 녹여줘야한다.
def hot():
    global grid
    grid_copy = [x[:] for x in grid]
    for i in range(n):
        for j in range(m):
            if(grid[i][j]!=0):
                cnt = 0 # 몇면이 닿아있는지 확인
                for k in range(4):
                    nr = i+row[k]
                    nc = j+col[k]
                    if (not (0 <= nr < n and 0 <= nc < m)):
                        continue
                    if(grid[nr][nc]==0):
                        cnt+=1
                grid_copy[i][j] -= cnt # copy 에서 빼줘야 다른 빙산들이 영향을 안받는다.
                if(grid_copy[i][j]<0): # 음수값  처리.
                    grid_copy[i][j] = 0
    grid = [x[:] for x in grid_copy]

n, m = map(int, input().split())
grid = [list(map(int,input().split())) for i in range(n)]
ans = 0
time = 0
row = [-1,1,0,0]
col = [0,0,1,-1]

while True:
    # 현재 덩어리 갯수 센다. (bfs)
    # 덩어리 0개면 ans = 0
    # 덩어리가 2개 이상이면 ans = time
    # 덩어리가 2개보다 작으면 녹인다.
    visited = [[False] * m for i in range(n)]
    area = valid()
    if(area ==0): # 다 녹아서 검사할 필요가 없음
        break
    elif(area>=2): # 목표 달성
        ans = time
        break
    # elif(area ==1): # 빙산이 하나면 녹여줘야함
    time +=1
    hot()

    # print("-----")
    # for _ in grid:
    #     print(*_)

print(ans)