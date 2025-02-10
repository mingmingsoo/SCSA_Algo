'''
문제시작 14:57
중간중간 풀어서 시간을 못쟀슴다...

before after 다른게 있으면
before에 after 색깔을 주입해줌
근데 before after 행렬이 다르면 백신이 다른 것

그게 아니라면 백신이 맞는 것

'''

from collections import deque
def same(before, after):
    for i in range(n):
        for j in range(m):
            if(before[i][j]!=after[i][j]):
                return False
    return True


def bfs(i, j,bef,aft):
    q = deque([(i,j)])
    visited = [[False]*m for i in range(n)]
    visited[i][j] = True
    while q:
        r,c = q.pop()
        before[r][c] = aft # 색깔 주입! 사실 한번만 해줘도 됨
        for k in range(4):
            nr = r+row[k]
            nc = c+col[k]
            if(not(0<=nr<n and 0<=nc<m)):
                continue
            if(not visited[nr][nc] and before[nr][nc] == bef):
                q.append((nr,nc))
                visited[nr][nc] = True
                before[nr][nc] = aft # 색깔 주입!

def valid():
    global ans
    for i in range(n):
        for j in range(m):
            if(before[i][j] != after[i][j]):
                # 두 값이 다르면 before 색깔을 주입해줌
                bfs(i,j,before[i][j],after[i][j])
                if(not same(before,after)): # 근데 만약 두개가 다르면 백신이 아닌 것임
                    ans = "NO"
                    return

n,m = map(int, input().split())
before = [list(map(int, input().split())) for i in range(n)]
after = [list(map(int, input().split())) for i in range(n)]

ans = "YES"

row = [-1,1,0,0]
col = [0,0,1,-1]

if(same(before, after)): # 처음부터 행렬이 같으면 yes
    print(ans)
    exit()

valid() # 검증해서 아니면 no
print(ans)