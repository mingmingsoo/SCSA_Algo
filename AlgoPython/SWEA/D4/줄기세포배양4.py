'''
코드리팩토링 q로 한번만 관리,
범위검사 X
'''
from collections import deque


def myprint():
    print("-------------------")
    for i in range(N):
        for j in range(N):
            if grid[i][j] == -1:
                print("X", end=" ")
            else:
                print(grid[i][j], end=" ")
        print()


T = int(input())
for tc in range(T):

    n, m, time = map(int, input().split())
    tmp = [list(map(int, input().split())) for i in range(n)]
    N = 700
    grid = [[0] * N for i in range(N)]
    q = []
    for i in range(n):
        for j in range(m):
            if tmp[i][j]:
                grid[i + N // 2][j + N // 2] = tmp[i][j]
                q.append((i + N // 2, j + N // 2, tmp[i][j], 0))  # 좌표, 생명력, 현재 진행 시간

    row = [-1, 1, 0, 0]
    col = [0, 0, 1, -1]

    die_q = []

    for i in range(time + 1):
        q.sort(key=lambda x: x[2], reverse=True)  # 생명력 순 내림차순
        for qs in range(len(q)):
            r, c, power, cur = q.pop(0)
            if cur == power + 1:  # 번식 가능
                die_q.append((r, c, power, 1))  # 대신 죽을 예정
                for k in range(4):
                    nr = r + row[k]
                    nc = c + col[k]
                    if grid[nr][nc] == 0:
                        grid[nr][nc] = power
                        q.append((nr, nc, power, 1))
            else:
                q.append((r, c, power, cur + 1))  # 아니믄 기다려
        if die_q:
            # 죽을 애들 있다?
            for dqs in range(len(die_q)):
                r, c, power, cur = die_q.pop(0)
                if cur == power:  # 쥬거@
                    grid[r][c] = -1
                else:
                    die_q.append((r, c, power, cur + 1))  # 아니믄 기다려
        # myprint()
    ans = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] > 0:
                ans += 1

    print(f"#{tc + 1} {ans}")