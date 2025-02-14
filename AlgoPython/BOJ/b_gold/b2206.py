'''
풀었던 문제

0이면 이동 가능
1이면 불가능

최단경로로 이동할 건데
벽을 부수는 기회가 1번 있음.

풀이
bfs로 풀되 방문처리는 3차원 배열로. 한번 부숴진데는 다시 못부수게 하겠음
'''
from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input())) for i in range(n)]
ans = -1

def bfs():
    q = deque([(0,0,1,True)]) # 위치와 거리, 벽 부실수 있는지
    visited = [[[False]*m for i in range(n)] for i in range(2)]
    visited[0][0][0] = True # 처음 온 곳은
    visited[1][0][0] = True # 벽이 있지도 않지만 일단 방문 처뤼~

    row = [-1,1,0,0]
    col = [0,0,1,-1]

    while q:
        global ans
        r,c,cnt,bomb = q.popleft()
        if(r == n-1 and c== m-1):
            ans = cnt
            return

        for k in range(4):
            nr = r+row[k]
            nc = c+col[k]
            if(not(0<=nr<n and 0<=nc<m)):
                continue
            # 갈 수 있으면 그냥가
            if(grid[nr][nc]==0 and not visited[bomb][nr][nc]):
                visited[bomb][nr][nc] = True
                q.append((nr,nc,cnt+1,bomb))
            elif(grid[nr][nc]==1 and not visited[1][nr][nc] and bomb):
                visited[1][nr][nc] = True
                q.append((nr,nc,cnt+1,False))

bfs()
print(ans)