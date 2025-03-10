'''
궁수 3명
공격은 D이하에서 가장 가까운, 왼쪽
적은 아래로 한 칸이동
모든 적이 격자판에서 제외되면 게잉ㅁ끝
입력
적 1

구상 n 중에 3개를 골름(조합)
궁수를 위치시키고 시뮬레이션 진행
적을 많이 제거해야함
# 패딩 굳이 안주겠다
'''
import heapq

n,m,limit = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
sel = [0]*3
total_enemy = 0
for _ in grid:
    total_enemy += _.count(1)
ans = 0
def combi(sidx,idx):
    global ans, grid
    if sidx == 3:
        origin_grid = [_[:] for _ in grid]
        cur_enemy = total_enemy
        kill = 0
        while True:
            # 궁수들이 각 후보를 고름
            enemy_list = []
            for lo in sel:
                ele_enemy = []
                for i in range(n):
                    for j in range(m):
                        if grid[i][j] == 1:
                            if (n-i)+abs(lo-j) <= limit:
                                heapq.heappush(ele_enemy,((n-i)+abs(lo-j),j,i))
                if ele_enemy:
                    dist,c,r = heapq.heappop(ele_enemy)
                    enemy_list.append((r,c))

            # 후보 킬 -> 1에서 0 이됐으면 score+1
            for r, c in enemy_list:
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    kill +=1
                    cur_enemy -=1
            # 궁수들 당기는데
            # 맨 밑에애들은 die
            for j in range(m):
                if grid[n-1][j] == 1:
                    grid[n-1][j] = 0
                    cur_enemy -=1

            for i in range(n-1,0,-1):
                for j in range(m):
                    if grid[i-1][j] == 1:
                        grid[i][j],grid[i-1][j] = grid[i-1][j] ,grid[i][j]
            # 적이 0명이면 끝
            if cur_enemy == 0:
                ans = max(ans, kill)
                grid = [_[:] for _ in origin_grid]
                return

    if idx == m:
        return

    sel[sidx] = idx
    combi(sidx+1, idx+1)
    combi(sidx, idx+1)


combi(0,0)
print(ans)