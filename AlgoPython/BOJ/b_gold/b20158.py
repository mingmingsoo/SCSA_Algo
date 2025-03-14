'''
4
0 1 0 0
0 0 0 0
0 0 0 0
2 0 0 0

4
0 0 0 2
1 2 1 0
2 1 1 0
1 1 1 0

맵이 100이라
속도 가속도 붙어도 14까지밖에 안댐

'''
import heapq

n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]
d = [[[[int(1e9)] * 15 for i in range(4)] for i in range(n)] for i in range(n)]
# 속도 14까지, 방향, 좌표
ans = "Fired"
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]

q = []
heapq.heappush(q, (0, 0, 0, -1, 1))  # 시간, 위치, 방향, 속도

while q:
    time, r, c, before_d, s = heapq.heappop(q)
    if time > 0 and d[r][c][before_d][s] > time:
        continue
    if r == c == n - 1:
        ans = time
        break
    for k in range(4):
        if k == before_d:
            nr = r + row[k] * (s + 1)
            nc = c + col[k] * (s + 1)
        else:
            nr = r + row[k]
            nc = c + col[k]
        if not (0 <= nr < n and 0 <= nc < n) or (grid[nr][nc] != 0 and time + 1 >= grid[nr][nc]):
            continue
        possible = True
        for rr in range(r, nr):
            if grid[rr][nc] != 0 and time + 1 > grid[rr][nc]:
                possible = False
                break
        for cc in range(c, nc):
            if grid[nr][cc] != 0 and time + 1 > grid[nr][cc]:
                possible = False
                break
        if not possible:
            continue
        if k == before_d:
            if d[nr][nc][k][s + 1] > time + 1:
                d[nr][nc][k][s + 1] = time + 1
                heapq.heappush(q, (time + 1, nr, nc, k, s + 1))
        else:
            if d[nr][nc][k][1] > time + 1:
                d[nr][nc][k][1] = time + 1
                heapq.heappush(q, (time + 1, nr, nc, k, 1))

print(ans)
