'''
문제 설명
    십자가가 가능한 모든 경우의 수 출력
'''

n,m =map(int, input().split())
grid = [list(input()) for i in range(n)]
visited = [[False]*m for i in range(n)]

ans = []
row = [1,-1,0,0]
col = [0,0,1,-1]

def jejus(r,c):
    l = 1
    while True:
        isOk = True
        for k in range(4):
            nr = r+row[k]*l
            nc = c+col[k]*l
            if not(0<=nr<n and 0<=nc<m):
                isOk = False
                break
            if grid[nr][nc] != "*":
                isOk = False
                break
        if(isOk):
            visited[r][c]=True
            for k in range(4):
                nr = r + row[k] * l
                nc = c + col[k] * l
                visited[nr][nc] = True
            ans.append((r + 1, c + 1, l))
            l+=1
        else:
            return

ans = []

for i in range(1,n-1):
    for j in range(1,m-1):
        if(grid[i][j]=="*"):
            jejus(i,j)

def valid():
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "*" and not visited[i][j]:
                print(-1)
                return True
    return False

if(valid()):
    pass
else:
    print(len(ans))
    for r, c, s in ans:
        print(r, c, s)


