T = int(input())
for tc in range(T):
    N, M, C = map(int, input().split())  # 맵크기, 좌표 갯수, 찾을 색깔

    grid = [[0] * N for i in range(N)]

    for m in range(M):
        r, c, rn, rc, color = map(int, input().split())
        for i in range(r, r + rn):
            for j in range(c, c + rc):
                grid[i][j] = color
    # for row in grid:
    #     print(row)

    ans = 0
    for i in range(N):
        for j in range(N):
            if (grid[i][j] == C):
                ans += 1
    print(f"#{tc+1} {ans}")