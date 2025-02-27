'''
문제설명
    빨, 초 뿌릴 수 있는 영역의 조.합
입력
    맵크기. 용액 갯수
    맵
출력
    최대 꽃 갯수

구상
    땅 선택은 조합
    색깔 선택은 순열 -> set에 담아서 중복 없게끔
    퍼지는 건 bfs
필요한 메서드
    combi - 땅 선택
    perm - 색깔 순서 정함 -> set으로 관리
    bfs - 배양액 퍼뜨림
'''
from collections import deque

def perm(idx):
    global flower
    if idx == flower_n:
        color_set.add(tuple(color_sel[:])) # 색깔 순서 set에 담아주기
        return

    for i in range(len(color_arr)):
        if not visited[i]:
            color_sel[idx] = color_arr[i]
            visited[i] = True
            perm(idx+1)
            visited[i] = False

def combi(sidx, idx):# 위치 조합
    global flower
    if sidx == flower_n:

        # 위치에 따른 모든 색깔 순열을 계산해줌.
        for color_list in color_set:
            ele_flower = bfs(location_sel, color_list)
            flower = max(ele_flower, flower)
        return

    if idx == len(location_arr):
        return

    location_sel[sidx] = location_arr[idx]
    combi(sidx+1, idx+1)
    combi(sidx, idx+1)

def bfs(location_sel, color_list): # 배양엑 뿌리는 bfs
    ele_flower = 0

    q = deque()
    time_grid = [[0] * m for i in range(n)] # 시간을 기록
    color_grid = [[0] * m for i in range(n)] # 방문배열, 꽃개화 체크

    for i in range(len(location_sel)):
        r,c = location_sel[i]
        color = color_list[i]
        color_grid[r][c] = color # 방문체크
        q.append((r,c,color,1)) # 위치 , 컬러, 시간
    while q:
        r, c, color, time = q.popleft()
        if color_grid[r][c] =="X": # 꽃이 됐으면 넘어가!
            continue

        for k in range(4):
            nr = r+row[k]
            nc = c+col[k]
            if not(0<=nr<n and 0<=nc<m) or grid[nr][nc]==0:
                continue

            # 나랑 다른색이고, 같은 시간이고, 꽃이 아니면!
            if color_grid[nr][nc] != color and time_grid[nr][nc] == time  and color_grid[nr][nc] != "X":
                color_grid[nr][nc] = "X" # 꽃 탄생
                ele_flower+=1

            # 나랑 같은 색이거나 꽃이면 배양액 못뿌려 넘어가
            elif color_grid[nr][nc] == color or color_grid[nr][nc] == "X":
                continue

            # 그게 아니라면 배양액을 뿌릴 수 있음
            elif color_grid[nr][nc] == 0:
                color_grid[nr][nc] = color
                time_grid[nr][nc] = time
                q.append((nr,nc,color, time+1))

    return ele_flower


n,m,green,red = map(int, input().split())

grid = [list(map(int, input().split())) for i in range(n)]
row = [-1,1,0,0]
col = [0,0,1,-1]

flower_n = green+red

location_arr = []
location_sel = [0]*flower_n

for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            location_arr.append((i,j))

color_arr = []
for i in range(green):
    color_arr.append("G")
for i in range(red):
    color_arr.append("R")

color_set = set() # 색깔 순열 중복없이.
color_sel=[0]*(flower_n)
visited = [False]*(flower_n)

flower = 0
perm(0) # 색깔 순열
combi(0,0) # 위치 조합
print(flower)