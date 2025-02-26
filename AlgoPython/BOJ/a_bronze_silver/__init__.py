'''
문제설명
    빨, 초 뿌릴 수 있는 영역의 조.합
입력
    맵크기. 용액 갯수
    맵
출력
    최대 꽃 갯수

구상
    조합이 아니라 순열
'''
from collections import deque

n,m,green,red = map(int, input().split())

grid = [list(map(int, input().split())) for i in range(n)]

sel = [0]*(green+red)
arr = []

for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            arr.append((i,j))
# print(arr)
flower = 0

color_arr = []
for i in range(green):
    color_arr.append("G")
for i in range(red):
    color_arr.append("R")

# print(color_arr)
row = [-1,1,0,0]
col = [0,0,1,-1]

def bfs(sel, color_sel):
    ele_flower = 0
    q = deque()
    time_grid = [[0] * m for i in range(n)]
    color_grid = [[0] * m for i in range(n)]
    for i in range(len(sel)):
        r,c = sel[i]
        color = color_sel[i]
        color_grid[r][c] = color
        q.append((r,c,color,1)) # 위치 , 컬러, 시간
    while q:
        r, c, color, time = q.popleft()

        for k in range(4):
            nr = r+row[k]
            nc = c+col[k]
            if not(0<=nr<n and 0<=nc<m) or grid[nr][nc]==0:
                continue

            if color_grid[nr][nc] != color and time_grid[nr][nc] == time  and  color_grid[nr][nc] != "X":
                color_grid[nr][nc] = "X"
                ele_flower+=1
            elif color_grid[nr][nc] == color or color_grid[nr][nc] == "X":
                continue
            elif color_grid[nr][nc] == 0:
                color_grid[nr][nc] = color
                time_grid[nr][nc] = time
                q.append((nr,nc,color, time+1))


    return ele_flower
def perm(cidx,color_sel,visited):
    global flower
    if cidx == green+red:
        # print(sel)
        # print(color_sel)

        # 여기서 bfs
        ele_flower = bfs(sel,color_sel)
        # if ele_flower ==6:
        #     print(sel, color_sel)
        flower = max(ele_flower, flower)

        return

    for i in range(len(color_arr)):
        if not visited[i]:
            color_sel[cidx] = color_arr[i]
            visited[i] = True
            perm(cidx+1, color_sel, visited)
            visited[i] = False

def combi(sidx, idx):
    global flower
    if sidx == green+red:
        # print(sel) # 얘가 선택할 땅들

        color_sel = [0]*(green+red) # 얘가 순열...
        visited = [False] * len(arr)
        perm(0,color_sel,visited)

        return

    if idx == len(arr):
        return

    sel[sidx] = arr[idx]
    combi(sidx+1, idx+1)
    combi(sidx, idx+1)



combi(0,0)
print(flower)