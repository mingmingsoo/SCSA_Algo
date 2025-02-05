'''
풀었던 문제

행, 열 거꾸로 들어옴
1 익은토마토
0 안익은토마토
-1 벽

해결방법
1. 토마토 위치들을 q에 한번에 담아줌
    1-1. 토마토가 아예 없으면 0 출력하고 끝
2. 익힘 표시를 visited로 하기, 일수는 dist로 파악
3. bfs가 끝나고 토마토인데 visited가 False 인 애들을 카운트 해줌

틀린 이유
처음 배열 받을 때 1인 좌표가 없으면 0 출력하고 끝이라고 생각했는데
-> 0 이 아니라 -1 이였음

추가로 넣어본 테케
2 2
1 1
1 1

2 2
-1 -1
-1 -1

'''
from collections import deque

m, n = map(int, input().split())

grid = [list(map(int, input().split())) for i in range(n)]
visited = [[False]* m for i in range(n)]

q = deque()
# 익은 토마토 찾기
for i in range(n):
    for j in range(m):
        if(grid[i][j]== 1):
            q.append((i,j))
            visited[i][j]= True

if(not q): # 익은 토마토 없으면 0 출력하고 끝 -> 0 이 아니라 -1 이였음
    print(-1)
    exit()

row = [-1,1,0,0]
col = [0,0,1,-1]


def bfs():
    day = 0
    while q:
        size = len(q)
        for s in range(size):
            r, c= q.popleft()
            for k in range(4):
                nr = r + row[k]
                nc = c + col[k]
                if (not (0 <= nr < n and 0 <= nc < m)):
                    continue
                if (not visited[nr][nc] and grid[nr][nc] == 0):  # 안익은 토마토면 익힐거임
                    visited[nr][nc] = True
                    grid[nr][nc] = 1
                    q.append((nr, nc))
        day+=1
    return day

days = bfs()-1

def all_order_tomato():
    global days
    # 못 익힌 토마토가 있으면?
    for i in range(n):
        for j in range(m):
            if (grid[i][j] == 0):
                days = -1
                return

all_order_tomato()

print(days)