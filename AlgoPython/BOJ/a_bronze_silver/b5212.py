n, m = map(int, input().split())

grid = [list(input()) for i in  range(n)]


isGroud = [[0] * m for i in range(n)]
row = [-1,1,0,0]
col = [0,0,1,-1]
for i in range(n):
    for j in range(m):
        if(grid[i][j]=='X'):
            cnt = 0
            for k in range(4):
                nr = i+row[k]
                nc = j+col[k]
                if(0<=nr<n and 0<=nc<m and grid[nr][nc]=='.'):
                    cnt+=1
                if(nr<0 or nr>=n or nc<0 or nc>=m):
                    cnt+=1
            if(cnt >=3):
                isGroud[i][j] = 1
for i in range(n):
    for j in range(m):
        if(isGroud[i][j]==1):
            grid[i][j]='.'
# print(grid)
minR = 11
maxR = -1
minC = 11
maxC = -1

for i in range(n):
    for j in range(m):
        if(grid[i][j]=='X'):
            minR = min(minR, i)
            maxR = max(maxR, i)
            minC = min(minC, j)
            maxC = max(maxC, j)
for i in range(minR, maxR+1):
    for j in range(minC, maxC+1):
        print(grid[i][j], end = "")
    print()