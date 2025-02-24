'''
b2665
흠냐 백트래킹인가.
근데 맵이 큰데..
다익스트라 응용

구상
    1인애들은 그냥지나가고 0을 d에 기록
'''
import heapq

n = int(input())
grid = [list(map(int, input())) for i in range(n)]

d = [[2501] * n for i in range(n)]
d[0][0] = 0

def dijk(sr,sc,er,ec):
    row = [-1,1,0,0]
    col = [0,0,1,-1]
    q = []
    heapq.heappush(q,(0,sr,sc))

    while q:
        dist, r, c = heapq.heappop(q)
        if(r==er and c == ec):
            break

        if(dist > d[r][c]):
            continue
        for k in range(4):
            nr = r+row[k]
            nc = c+col[k]
            if not(0<=nr<n and 0<=nc<n):
                continue

            if grid[nr][nc] ==1 and d[nr][nc]==2501:
                d[nr][nc] = d[r][c]
                heapq.heappush(q,(dist,nr,nc))
            elif grid[nr][nc]==0:
                if d[nr][nc] > dist+1:
                    d[nr][nc] = dist+1
                    heapq.heappush(q,(dist+1,nr,nc))

dijk(0,0,n-1,n-1)

print(d[n-1][n-1])