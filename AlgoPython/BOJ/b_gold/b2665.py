'''
# 제출 횟수 : 1회
# 메모리 : 112044KB
# 실행 시간 : 140ms

b2665
백트래킹인가.
근데 맵이 큰데..
다익스트라 응용으로 풀겠음

구상
    1인애들은 그냥지나가고 0을 d에 기록
'''
import heapq

n = int(input())
grid = [list(map(int, input())) for i in range(n)]

d = [[2501] * n for i in range(n)] # 큰 값으로 채우기
d[0][0] = 0 # 시작점

def dijk(sr,sc,er,ec):
    row = [-1,1,0,0]
    col = [0,0,1,-1]
    q = []
    heapq.heappush(q,(0,sr,sc))

    while q:
        dist, r, c = heapq.heappop(q)
        if(r==er and c == ec):
            break

        if(dist > d[r][c]): # 내가 온 길이 돌아온 길이면 continue
            continue
        for k in range(4):
            nr = r+row[k]
            nc = c+col[k]
            if not(0<=nr<n and 0<=nc<n):
                continue

            if d[nr][nc] > dist+(1-grid[nr][nc]):
                d[nr][nc] = dist+(1-grid[nr][nc])
                heapq.heappush(q,(d[nr][nc],nr,nc))

dijk(0,0,n-1,n-1)

print(d[n-1][n-1])