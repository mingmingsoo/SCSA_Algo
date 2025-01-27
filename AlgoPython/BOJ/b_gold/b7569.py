'''
하루마다 토마토들은 상하좌우, 위아래로 익어감
1: 익은 토마토 - 얘를 기준으로 퍼져감
0: 익지 않은 토마토
-1: 토마토 없음

토마토가 모두 익지 못하면 -1 출력

필요한 과정
1. 익은 토마트들의 좌표를 q에 넣어줌
2. bfs 시작. row col hei 을 사용해서 이동
3. bfs 끝나고 grid가 0인데 vistied가 fasle이면 모두 익지 못한 상태 -1 출력

'''
from collections import deque

M,N,H = map(int, input().split())
# 3차원 배열 생성
grid = [[list(map(int, input().split())) for n in range(N)] for h in range(H)]

# for height in range(H):
#     print(grid[height])
q = deque()
visited = set()
for h in range(H):
    for i in range(N):
        for j in range(M):
            if grid[h][i][j] == 1:
                q.append((h,i,j))
                visited.add((h,i,j))
# print(q)
# print(visited)

hei = [1,-1,0,0,0,0]
row = [0,0,1,-1,0,0]
col = [0,0,0,0,1,-1]


def isRange(dh, dr, dc):
    if(0<=dh<H and 0<=dr<N and 0<=dc<M):
        return True
    return False

ans = 0
while q:
    size = len(q)
    for i in range(size):
        h,r,c = q.popleft()
        for d in range(6):
            dh = h+hei[d]
            dr = r+row[d]
            dc = c+col[d]

            if(isRange(dh,dr,dc) and grid[dh][dr][dc]==0 and (dh,dr,dc) not in visited):
                q.append((dh,dr,dc))
                visited.add((dh,dr,dc))
    ans += 1
isTomato = True
for h in range(H):
    for i in range(N):
        for j in range(M):
            if(grid[h][i][j] == 0 and (h,i,j) not in visited):
                isTomato = False
if(isTomato == False):
    print(-1)
else:
    print(ans-1)
