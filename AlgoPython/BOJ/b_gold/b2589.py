'''
문제설명
    L 인 모든점에서 구함.
    다익스트라풀이
'''
import heapq

n, m = map(int, input().split())
grid = [list(input()) for i in range(n)]

visited = [[False]* m for i in range(n)]
ans = 0
row = [-1,1,0,0]
col = [0,0,1,-1]
def dijk(r,c):
    global ans
    d[r][c] = 0
    q = []
    heapq.heappush(q,(0,r,c))

    while q:
        dist, r,c = heapq.heappop(q)
        if dist > d[r][c]:
            continue

        for  k in range(4):
            nr = r+row[k]
            nc = c + col[k]

            if not(0<=nr<n and 0<=nc<m) or grid[nr][nc]=="W":
                continue

            if d[nr][nc] > dist+1:
                d[nr][nc] = dist+1
                heapq.heappush(q,(dist+1, nr,nc))

    for i in range(n):
        for j in range(m):
            if d[i][j] != 2501:
                ans = max(ans, d[i][j])

for i in range(n):
    for j in range(m):
        if grid[i][j] =="L":
            d = [[2501]*m for i in range(n)]
            dijk(i,j)
print(ans)