'''
 굳이 레버기 있는 이유가 뭐지,,,
 다익스트라 풀이
 아 레버를 당겨야만 가능.ㅋㅋ
'''
import heapq

maps =["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]

n = len(maps)
m = len(maps[0])
d = [[10001]*m for i in range(n)]

sr,sc,lr,lc,er,ec = -1,-1,-1,-1,-1,-1
ans1= 0
ans2 = 0
for i in range(n):
    for j in range(m):
        if maps[i][j] =="S":
            sr , sc = i,j
        elif maps[i][j] =="E":
            er,ec = i,j
        elif maps[i][j] =="L":
            lr,lc = i,j
d[sr][sc] = 0
row = [-1,1,0,0]
col = [0,0,1,-1]
def dijk(sr,sc,er,ec,start):
    q = []
    heapq.heappush(q, (start,sr,sc))

    while q:
        dist, r, c =heapq.heappop(q)
        if r== er and c == ec:
            break
        if d[r][c] > dist:
            continue

        for k in range(4):
            nr = r+row[k]
            nc = c+col[k]

            if not(0<=nr<n and 0<=nc<m):
                continue
            if maps[nr][nc] =="X":
                continue
            if d[nr][nc] > dist+1:
                d[nr][nc] = dist+1
                heapq.heappush(q,(dist+1,nr,nc))

dijk(sr,sc,lr,lc,0)
ans1 = d[lr][lc]
if(d[lr][lc]==10001):
    print(-1)
else:
    d = [[10001] * m for i in range(n)]
    d[lr][lc] = 0
    dijk(lr,lc,er,ec,d[lr][lc])
    ans2 = d[er][ec]
    ans = ans1+ans2
    if(ans>=10001):
        print(-1)
    else:
        print(ans)