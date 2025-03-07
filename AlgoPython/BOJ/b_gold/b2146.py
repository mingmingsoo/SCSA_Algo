'''
문제설명
    여러개의 섬들 중
    딱 두개만 연결하면 되는데
    그 거리가 최소가 되게끔 해라...
구상
    일단 섬에 넘버링 한다.
    넘버링 하고나서는
    뭘 연결할지는 조합으로 2개 뽑아야할듯
    최단거리는 어떻게 구할까요
    모든 점을 q에 넣고
    퍼져나가다가 다음 섬 만나면 끝

필요한 메서드
bfs() # 넘버링 필요
bfs() # 거리 계산.
'''
from collections import deque

n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]
visited = [[0]*n for i in range(n)]
num = 1
row = [-1,1,0,0]
col = [0,0,1,-1]
def bfs(r,c,num):
    q = deque([(r,c)])
    while q:
        r,c = q.popleft()
        for k in range(4):
            nr = r+row[k]
            nc = c+col[k]
            if not(0<=nr<n and 0<=nc<n) or visited[nr][nc] or grid[nr][nc] != 1:
                continue
            visited[nr][nc] = num
            q.append((nr,nc))

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and visited[i][j] ==0:
            visited[i][j] = num
            bfs(i,j,num)
            num +=1

v = [[False]*n for i in range(n)]
ans = 100*100+1

def bfs2(r,c,num):
    global ans
    q = deque([(r,c,0)])
    while q:
        r,c,cnt = q.popleft()
        for k in range(4):
            nr = r+row[k]
            nc = c+col[k]
            if not(0<=nr<n and 0<=nc<n):
                continue
            if visited[nr][nc] ==0:
                q.append((nr, nc, cnt+1))
            elif visited[nr][nc] != num:
                ans = min(ans,cnt)
                return

for i in range(n):
    for j in range(n):
        if visited[i][j] != 0:
            bfs2(i,j,visited[i][j])

print(ans)