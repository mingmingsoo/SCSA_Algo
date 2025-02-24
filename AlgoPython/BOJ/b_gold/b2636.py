'''
b2636

문제 설명
    공기와 맞닿은 곳만 없어진다.
    치즈가 모두 없어질 때 까지 걸리는 시간은?
입력
    맵
출력
    치즈가 모두 녹는 시간, 녹기 한 시간 전 남아있는 치즈갯수
구상.
    맵의 테두리는 모두 공기임!
    0,0도 공기이므로 공기부터 시작해서 공기를 q에 넣어주고
    치즈를 만나면 녹여주면 된다.
    -> 구멍치즈를 해결할 수 있음
'''
from collections import deque

n, m = map(int, input().split())

grid = [list(map(int, input().split())) for i in range(n)]

cheeze = []
row = [-1,1,0,0]
col = [0,0,1,-1]
time = 0

def bfs(sr,sc):
    visited = [[False]*m for i in range(n)]
    visited[sr][sc] = True
    q = deque([(sr,sc)])
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
            if not visited[nr][nc] and grid[nr][nc]==1:
                grid[nr][nc] =0
                visited[nr][nc] = True

def counting(grid):
    num = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j]==1:
                num+=1
    return num

while True:
    cheeze_num = counting(grid)
    if(cheeze_num==0):
        break
    cheeze.append(cheeze_num)
    bfs(0,0)
    # print("-------------------")
    # for _ in grid:
    #     print(*_)
    time+=1

print(time)
if not cheeze:
    print(0)
else:
    print(cheeze[-1])
