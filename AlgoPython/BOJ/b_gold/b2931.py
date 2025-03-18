'''
문제설명
    해커는 딱 1개만 지웠다.
    답은 딱 1가지다.
    M에서 시작해서 가다가 쭉쭉 가다가
    .을 만나면 경우수를 계산
    그다음에 dfs 연결 확인해줘야함



    아님 ! 그냥 ,, 방향에 따라 따져주면됨
    M과 Z는 중요하지 않음

'''
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
grid = [list(input()) for i in range(n)]
row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]
target_r, target_c, target_shape = -1, -1, ""

dirs = {"|": (0, 2), "-": (1, 3), "+": (0, 1, 2, 3), "1": (1, 2), "2": (0, 1), "3": (0, 3), "4": (2, 3)}
dirs_reverse = {(0, 2): "|", (1, 3): "-", (0, 1, 2, 3): "+", (1, 2): "1", (0, 1): "2", (0, 3): "3", (2, 3): "4"}
connect = {0: ("|", "+", "1", "4"), 1: ("-", "+", "3", "4"), 2: ("|", "+", "2", "3"), 3: ("-", "+", "1", "2")}
find = False
for i in range(n):
    for j in range(m):
        if grid[i][j] != ".":
            if grid[i][j] == "M" or grid[i][j] == "Z":
                continue
            for k in dirs[grid[i][j]]:
                nr = i + row[k]
                nc = j + col[k]
                if grid[nr][nc] == ".":
                    target_r, target_c = nr, nc
                    shape = []
                    for k in range(4):
                        ntr = target_r + row[k]
                        ntc = target_c + col[k]
                        if not (0 <= ntr < n and 0 <= ntc < m):
                            continue
                        if grid[ntr][ntc] in connect[k]:
                            shape.append(k)
                    target_shape = dirs_reverse[tuple(shape)]
                    find = True
                    break
        if find:
            break
    if find:
        break

print(target_r + 1, target_c + 1, target_shape)
