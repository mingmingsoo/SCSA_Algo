'''
문제설명
    각 행의 첫 점마다 별들을 가둘 수 있는지 검사해야함 (완탐필요)
구상
    가둔다는 것은 첫점으로 같은 방향으로 돌아왔다는 것이다.
'''

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

row = [0,1,0,-1]
col = [1,0,-1,0]

ans = []
def is_cycle(idx):
    r,c,d = idx,0,0
    visited[r][c][0] = True
    while True:
        num = grid[r][c] # 내가 얼마나 갈 수 있는지

        nr = r+row[d]*num
        nc = c+col[d]*num
        nd = (d+1)%4
        if not(0<=nr<n and 0<=nc<m):
            return False
        if not visited[nr][nc][nd]:
            visited[nr][nc][nd] = True
            r,c,d = nr,nc,nd
        elif visited[nr][nc][nd]:
            return True


for i in range(n):
    visited = [[[False]*4 for i in range(m)] for i in range(n)]
    if(is_cycle(i)):
        ans.append(i+1)

print(len(ans))
print(*ans)