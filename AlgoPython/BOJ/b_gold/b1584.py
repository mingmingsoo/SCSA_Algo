'''
다익스트라 연습

[문제설명]
    0,0 -> 500,500 으로 가야함
    4방으로 움직일 수 있음
    도착지까지 갈 때 생명을 잃는 최솟값을 구해라
    위험, 죽음이 겹칠 수 있음 이때는 죽음이 더 강하다.
[입력]
    위험한 구역수 N
    위험한 구역의 좌표
    죽음의 구역수 M
    죽음의 구역수 좌표
[구상]
    0 -> 안전구역
    1 -> 위험구역
    2-> 죽음구역
    죽음구역은 갈 수 없고 -> q에서 조건으로 거른다.
    위험구역 합이 최소로 되게끔 경로를 설정한다.
'''
import heapq
size = 500
# 초기 설정
grid = [[0] * (size+1) for i in range(size+1)]
danger_num = int(input())
for i in range(danger_num):
    danger_x1, danger_y1, danger_x2, danger_y2 = map(int, input().split())
    if danger_x2 < danger_x1:
        danger_x1, danger_x2 = danger_x2, danger_x1
    if danger_y2 < danger_y1:
        danger_y1, danger_y2 = danger_y2, danger_y1
    for i in range(danger_x1, danger_x2 + 1):
        for j in range(danger_y1, danger_y2 + 1):
            grid[i][j] = 1
die_num = int(input())
for i in range(die_num):
    die_x1, die_y1, die_x2, die_y2 = map(int, input().split())
    if die_x2 < die_x1:
        die_x1, die_x2 = die_x2, die_x1
    if die_y2 < die_y1:
        die_y1, die_y2 = die_y2, die_y1
    for i in range(die_x1, die_x2 + 1):
        for j in range(die_y1, die_y2 + 1):
            grid[i][j] = 2

d = [[size*size*50+1] * (size+1) for i in range(size+1)] # 큰값
d[0][0] = 0 # 시작점

def dijk(start,sr,sc):
    row = [-1,1,0,0]
    col = [0,0,1,-1]
    q = []
    heapq.heappush(q, (start,sr,sc))

    while q:
        dist, r, c = heapq.heappop(q)

        if dist > d[r][c]: # 너가 온 길은 아까 내가 더 빨리 온 길이야 넘어가
            continue

        for k in range(4):
            nr = r+row[k]
            nc = c+col[k]
            if(not(0<=nr<size+1 and 0<=nc<size+1)):
                continue
            if(grid[nr][nc]==2): # 죽음의 구역이면 넘어가.
                continue
            if(d[nr][nc] > dist + grid[nr][nc]):
                d[nr][nc] = dist+grid[nr][nc]
                q.append((d[nr][nc], nr,nc))
dijk(d[0][0],0,0)
if(d[size][size] == 12500001):
    print(-1)
else:
    print(d[size][size])
