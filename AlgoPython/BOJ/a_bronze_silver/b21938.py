import  sys
sys.setrecursionlimit(10**6)
'''
r,g,b 를 0~255
색을 평균네어 T보타 크면 255로 작으면 0으로 바꿈
255인 군집이 몇개 있는가?
'''

n, m = map(int, input().split())

grid = [[0]* m for i in range(n)]

colorList = [list(map(int,input().split())) for i in range(n)]
T = int(input())
for i in range(n):
    for j in range(0,3*m,3):
        total = colorList[i][j]+ colorList[i][j+1]+\
                 colorList[i][j+2]
        avg = total/3
        if(avg<T):
            avg = 0
        else:
            avg = 255
        grid[i][j//3] = avg

visited = [[False]* m for i in range(n)]

ans = 0
row = [-1,1,0,0]
col = [0,0,1,-1]

def dfs(r, c):
    visited[r][c] = True
    for k in range(4):
        nr = r+row[k]
        nc = c+col[k]
        if(0<=nr<n and 0<=nc<m and not visited[nr][nc] and grid[nr][nc]==255):
            dfs(nr,nc)


for i in range(n):
    for j in range(m):
        if(not visited[i][j] and grid[i][j]==255):
            ans +=1
            dfs(i,j)
print(ans)