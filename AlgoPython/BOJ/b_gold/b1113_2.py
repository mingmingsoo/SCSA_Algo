'''
9 13
1111111111111
1555555555551
1511111111151
1511199911151
1511192911151
1511199911151
1511111111151
1555555555551
1111111111111

안에 갇혀서 물이 고일 수 있는 1과 그 밖의 물이 고일 수 없는 1은 무슨 차이일까?

- 안에 고여있는 1은 본인과 같은 크기 혹은 작은애들을 q에 넣는다.
q에 값들이 잘 담긴채로 끝나면 물이 고일 수 있다.

- 물이 고일 수 없는 1은 본인과 같은 크기 혹은 작은 애들을 q에 넣는다
근데 혹시라도 범위 밖으로 나가면 물이 고일 수 없는 것이다.


1. 1,1 ~ n-1,m-1 만 탐색한다
2. visited를 하면... 안된다. 물이 고일 수 있는 애들한테도 영향받는다.
3. 그러면 물의 높이가 중복되는뎅.... set에 (i,j,높이) 넣고다니고
    물이 고일 수 있었다면 걔네들만 visited 해주장. 그리고 그 set으로 높이 계산하자
    -> 고일수 있는 높이 계산하는 로직도 필요.

'''
import copy
from collections import deque

n,m = map(int, input().split())

grid = [list(map(int, input())) for i in range(n)]

ans = 0


row = [-1,1,0,0]
col = [0,0,1,-1]
def bfs(i, j, height):
    global ans
    q = deque([(i,j,height)])
    visited = set([(i,j,height)])
    minH = 10
    while q:
        r,c,h = q.popleft()

        for k in range(4):
            nr = r+row[k]
            nc = c+col[k]
            if(not(0<=nr<n and 0<=nc<m)): # 물이 될 수 없는 애들임.
                return # 그냥 종료
            if((nr,nc,grid[nr][nc]) not in visited and grid[nr][nc]<=height): # 나보다 같거나 낮은 애들은 다 물이 흘러가유
                q.append((nr,nc,grid[nr][nc]))
                visited.add((nr,nc,grid[nr][nc]))
            if(grid[nr][nc]>height):
                minH = min(minH, grid[nr][nc])

    # 여기까지 왔으면 수영장 계산
    for r,c,h in visited:
        grid[r][c] = minH
        ans += (minH-h)

for i in range(1,n-1):
    for j in range(1,m-1):
        bfs(i,j,grid[i][j])
print(ans)