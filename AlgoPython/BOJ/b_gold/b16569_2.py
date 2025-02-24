'''
풀이시간 1시간4분

문제 설명
    화산은 인접한 곳으로 덮힌다.
    가장 높은곳으로 되도록 가장 빨리 -> ans배열 만들기
    우선순위가 가장 높은 고도임 -> return 치면 안되고 가능한 경우를 구해야함
    재상이는 화산이 있는 위치와 화산쇄설류가 뒤덮인 곳은 갈 수 없다.
    -> 즉 화산먼저 폭발한다.
입력
    좌표 -1 씩 필요
구상
필요한 변수
    1. fire_grid : 못가는 곳 기록
    2. fire_grid_cur_time : 그 화산이 지금 시간이 얼마나 흘렀는지 기록
필요한 메서드
    1. bfs
    2. fire
헷갈렸던 점
    fire_grid_cur_time = [[1] * m for i in range(n)] # 화산 진행 시간 만들때
    처음엔 0으로 채웠는데
    1초가 되자마자 근방 가까운 1인 곳이 터졌음
    나는 1초 지나고 될 줄 알았음
'''

import heapq
from collections import deque
import sys

input = sys.stdin.readline


def my_print(cur_time):
    print("========", cur_time, "========")
    for i in range(n):
        for j in range(m):
            if fire_grid[i][j] == -2:
                print("O", end=" ")
            elif fire_grid[i][j] == -1:
                print("X", end=" ")
            else:
                print(fire_grid[i][j], end=" ")
        print()


def fire(r, c, cur_time):
    # 폭발 시작해야되는데..
    ing = cur_time - fire_grid[r][c] + 1
    sx, ex, sy, ey = max(0, r - ing), min(n, r + ing), max(0, c - ing), min(m, c + ing)
    for i in range(sx,ex):
        for j in range(sy,ey):
            if ing >= abs(i - r) + abs(j - c):  # 인접한 곳으로 화산흐름
                if (i == r and j == c):  # 내 위치는 빼고
                    continue
                else:
                    if (fire_grid[i][j] == -2):  # 이게 필요한 이유가 이거 없으면 다른 분출구도 -1로 만들어버림..
                        fire_grid[i][j] = -1


n, m, tnum = map(int, input().split())
sr, sc = map(lambda x: int(x) - 1, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

fire_grid = [[-2] * m for i in range(n)]  # -2인 곳은 갈 수 있음
visited = [[False] * m for i in range(n)]
fire_list = []
for i in range(tnum):
    x, y, t = map(int, input().split())
    x -= 1
    y -= 1
    fire_grid[x][y] = t  # 분출구 기록 t초부터 분출한다.
    fire_list.append((x,y,t))
ans = []  # 높이와 거리를 담을 배열


def bfs(sr, sc):
    row = [-1, 1, 0, 0]
    col = [0, 0, 1, -1]
    q = deque([(sr, sc, 0)])
    visited[sr][sc] = True
    cur_time = 0
    while q:
        # 화산 폭발
        for x,y,t in fire_list:
            if t <= cur_time:
                fire(x,y,cur_time)

        qsize = len(q)
        for size in range(qsize):
            # 재상이 이동
            r, c, cnt = q.popleft()
            heapq.heappush(ans, (-grid[r][c], cnt))  # 높이, 시간 기록

            for k in range(4):
                nr = r + row[k]
                nc = c + col[k]

                if not (0 <= nr < n and 0 <= nc < m):
                    continue
                if not visited[nr][nc] and fire_grid[nr][nc] == -2:  # 화산이 아닌곳만 갈 수 있음
                    visited[nr][nc] = True
                    q.append((nr, nc, cnt + 1))
        cur_time += 1


bfs(sr, sc)
h, t = heapq.heappop(ans)
print(-h, t)
