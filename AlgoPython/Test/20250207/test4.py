'''
기본 bfs
틀린이유: maxNum = -1로 초기화했는데
그림이 없을 때 도있음 ㅠㅠ
그러면 -1을 출력해서 틀렸을 것이다 ㅠㅠ
초기화 너무 대충하는 것 같다... 잘 보고하자
'''

from collections import deque

n,m = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

visited = [[False] * m for i in range(n)]
total = 0
maxNum = 0

row = [-1,1,0,0]
col = [0,0,1,-1]

def bfs(i, j):
    global maxNum
    q = deque([(i,j)])
    cnt = 1
    while q:
        r,c = q.popleft()
        maxNum = max(cnt, maxNum)
        for k in range(4):
            nr = r+row[k]
            nc = c+col[k]
            if(not(0<=nr<n and 0<=nc<m)):
                continue

            if(not visited[nr][nc] and grid[nr][nc]==1):
                q.append((nr,nc))
                cnt+=1
                visited[nr][nc] = True
    maxNum = max(maxNum,cnt)

for i in range(n):
    for j in range(m):
        if(not visited[i][j] and grid[i][j]==1):
            # print(i,j)
            visited[i][j]= True
            bfs(i,j)
            total +=1
print(total)
print(maxNum)
