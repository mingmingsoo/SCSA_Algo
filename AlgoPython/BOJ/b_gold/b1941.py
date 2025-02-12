'''
[문제 설명]
    칠공주의 규칙
    1. 7명의 여학생들로 구성
    2. 7명의 자리는 가로나 세로로 인접
    3. 이다솜파만 있어도 되는 것은 아니다.
    4. 7명 중 4명 이상은 이다솜파
    소문난 칠공주가 앉을 수 있는 모든 경우의 수 구하라

[입력]
    행렬은 모두 5*5
    이다솜파 S, 임도연파 Y
[출력]
    경우의 수
[구상]
    한 점에서 시작해서 모든 경로를 탐색해서
    depth가 7이고 S가 4개 이상인 경로를 모두 탐색한다.
'''


grid = [list(input()) for i in range(5)]
visited = [[False]* 5 for i in range(5)]
ans = 0

row = [-1,1,0,0]
col = [0,0,1,-1]
def dfs(r,c,cnt,long): # 위치, 이다솜파 숫자, 총 길이
    global ans
    if(long==7):
        if(cnt>=4):
            ans+=1
        return
    visited[r][c] = True
    for k in range(4):
        nr = r+row[k]
        nc = c+col[k]
        if(0<=nr<5 and 0<=nc<5 and not visited[nr][nc]):
            if(grid[nr][nc]=="S"):
                dfs(nr,nc,cnt+1,long+1)
            else:
                dfs(nr,nc,cnt,long+1)

    visited[r][c] = False
for i in range(5):
    for j in range(5):
        if(grid[i][j]=="S"):
            dfs(i,j,1,1)
print(ans)