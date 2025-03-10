'''
문제설명
    핀을 움직여서 인접한 핀을 최대한 많이 없애라!
문제 구상
    동시 다발이아니라 bfs가 아님
    btk
    원래 맵 기록해줘야하는듯..
'''
def btk(dist):
    global ans
    find = False

    for i in range(n):
        for j in range(m):
            if grid[i][j] == "o":
                for k in range(4):
                    nr = i + row[k]
                    nc = j + col[k]
                    if not (0 <= nr < n and 0 <= nc < m) or not (0 <= nr + row[k] < n and 0 <= nc + col[k] < m):
                        continue

                    if grid[nr][nc] == "o" and grid[nr + row[k]][nc + col[k]] == ".":
                        find = True
                        grid[nr][nc] = "."
                        grid[i][j] = "."
                        grid[nr + row[k]][nc + col[k]] = "o"
                        btk(dist + 1)
                        grid[nr][nc] = "o"
                        grid[i][j] = "o"
                        grid[nr + row[k]][nc + col[k]] = "."
    if not find:
        ans = max(ans, dist)
        return

output = []
T = int(input())
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]
for tc in range(T):
    n, m = 5, 9
    grid = [list(input()) for i in range(n)]
    if tc < T - 1:
        input()

    # 원래 갯수 - 먹은 갯수
    # 최대한 많이 먹어야하고
    # 이동 횟수도 기록

    total = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == "o":
                total += 1
    ans = 0

    btk(0)
    output.append((total-ans, ans))
for eat, dist in output:
    print(eat, dist)