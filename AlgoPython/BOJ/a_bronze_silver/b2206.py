'''
0: 이동가능
1: 이동 불가능
0,0 -> N-1, M-1로 이동
벽을 부술 수 있는 기회는 1번.

bfs로 풀고 불리언 데리고 다니기.

도착하지 못하면 -1 출력 : q가 안비면
'''
from collections import deque

n, m = map(int, input().split())

grid = [[0]*m for i in range(n)]
for i in range(n):
    string = input()
    for j in range(m):
        grid[i][j] = int(string[j])

# print(grid)


def bfs(startR, startC, endR, endC):
    row = [-1,1,0,0]
    col = [0,0,1,-1]
    q = deque([(startR,startC,0,True)])
    # print(q)
    visited = set([startR,startC,True]) # 벽 안부수고 이동.

    while q:
        r,c,sum,isBomb = q.popleft()
        if(r==endR and c == endC):
            return sum

        for k in range(4):
            nr = r+row[k]
            nc = c+col[k]

            if 0<=nr<=n-1 and 0<=nc<=m-1 and grid[nr][nc] == 1 and (nr,nc,False) not in visited and isBomb:
                visited.add((nr,nc,False))
                q.append((nr,nc,sum+1,False))
            if 0<=nr<=n-1 and 0<=nc<=m-1 and grid[nr][nc] == 0 and (nr,nc,isBomb) not in visited:
                visited.add((nr,nc,isBomb))
                q.append((nr,nc,sum+1,isBomb))


    return -1


ans = bfs(0,0,n-1,m-1)
if(ans == -1):
    print(-1)
else:
    print(ans+1)