'''
문제설명
    마법 지팡이 1번만 사용해서 벽 허물음
    최단경로
    벽부수고 이동하기랑 동일한 문제
설마 홍익이 위치가 0이진 않겠지...
'''
from collections import deque

n,m = map(int, input().split())
sr,sc = map(lambda x:int(x)-1, input().split())
er,ec = map(lambda x:int(x)-1, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
row = [-1,1,0,0]
col = [0,0,1,-1]

visited = [[[False]*2 for i in range(m)] for i in range(n)]
q = deque([(sr,sc,0,True)])
visited[sr][sc][0] = True
visited[sr][sc][1] = True
ans = 1000 * 1000 + 1
while q:
    r,c,dist,bomb = q.popleft()
    if r == er and c == ec:
        ans = dist
        break
    for k in range(4):
        nr = r+row[k]
        nc = c+col[k]
        if not(0<=nr<n and 0<=nc<m):
            continue
        if grid[nr][nc] == 0 and not visited[nr][nc][bomb]:
            visited[nr][nc][bomb] = True
            q.append((nr,nc,dist+1,bomb))
        elif grid[nr][nc] == 1 and not visited[nr][nc][1] and bomb:
            visited[nr][nc][1] = True
            q.append((nr,nc,dist+1,False))
if ans ==1000 * 1000 + 1:
    print(-1)
else:
    print(ans)