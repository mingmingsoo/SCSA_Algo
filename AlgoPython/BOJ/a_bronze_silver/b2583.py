'''
0 인 군집들의 넓이 구하기 -> 리스트에 담기
군집 갯수 -> total
r,c 잘 확인하기
ans에 set으로 해서 중복되는 값이 안들어가서 틀렸음..ㅍ.ㅍㅍ퓨ㅠㅠ
set 잘 생각하고 쓰기 명심!
'''
import sys
sys.setrecursionlimit(10**5)

n, m, k = map(int, input().split())
grid = [[0] * m for i in range(n)]

for i in range(k):
    # c, r, 순서로 입력
    c1,r1,c2,r2 = map(int, input().split())
    r1,r2 = n-r1, n-r2
    for i in range(r2,r1):
        for j in range(c1,c2):
            grid[i][j] = 1

visited = [[False] * m for i in range(n)]

total = 0
ans = [] # set으로 해서 중복되는 값이 안들어가서 틀렸음ㅋㅋㅋㅋㅋ

row = [-1,1,0,0]
col = [0,0,1,-1]
def dfs(r, c):
    global  ele
    visited[r][c] = True
    ele +=1
    for k in range(4):
        nr = r+row[k]
        nc = c+col[k]
        if(0<=nr<n and 0<=nc<m and grid[nr][nc]==0 and not visited[nr][nc]):
            dfs(nr,nc)


for i in range(n):
    for j in range(m):
        if(grid[i][j]==0 and not visited[i][j]):
            total+=1
            ele = 0
            dfs(i,j)
            ans.append(ele)
ans.sort()
print(total)
print(*ans)
