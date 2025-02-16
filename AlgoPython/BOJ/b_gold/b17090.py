'''
문제 설명
    칸마다 이동경로를 따라 범위에 마주치면 이동 가능
구상
    state 2차원 배열을 생성하고
    0은 탐색해야할 곳
    1은 미로인곳
    2는 탈출가능한 곳
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(500000)

n, m = map(int, input().split())
grid = [list(input().rstrip()) for i in range(n)]
state = [[0]*m for i in range(n)]
visited = [[False]*m for i in range(n)]

row = [-1,0,1,0]
col = [0,1,0,-1]

def check(r,c,d):
    global miro

    visited[r][c] = True
    nr = r+row[d]
    nc = c+col[d]

    if(not(0<=nr<n and 0<=nc<m)):
        state[r][c] =2
        miro = True
        return
    elif(state[nr][nc]==2):
        state[r][c] = 2
        miro = True
        return
    elif(state[nr][nc]==1):
        state[r][c] = 1
        return
    elif(visited[nr][nc]):
        state[r][c] = 1
        return
    elif(state[nr][nc]==0):
        check(nr,nc,"URDL".index(grid[nr][nc]))
        if(miro):
            state[r][c] = 2
        else:
            state[r][c]=1



for i in range(n):
    for j in range(m):
        if state[i][j]==0:
            miro = False
            check(i,j,"URDL".index(grid[i][j]))
# for _ in state:
#     print(_)
ans = 0
for i in range(n):
    for j in range(m):
        if state[i][j]==2:
            ans+=1
print(ans)