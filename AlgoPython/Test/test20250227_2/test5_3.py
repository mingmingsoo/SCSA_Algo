import heapq

T = int(input())
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

for tc in range(1, T + 1):
    N = int(input())
    s_y, s_x, e_y, e_x = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]
    d = [[100000] * N for _ in range(N)]
    if arr[s_y][s_x] == 0:
        start = 0
    else:
        start = 1
    d[s_y][s_x] = start
    pq = [(start, s_y, s_x)]
    heapq.heapify(pq)

    while pq:
        cur, y, x = heapq.heappop(pq)
        if d[y][x] < cur:
            continue

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < N and 0 <= nx < N and d[ny][nx] > d[y][x] + arr[ny][nx]:
                d[ny][nx] = d[y][x] + arr[ny][nx]
                heapq.heappush(pq, (d[ny][nx], ny, nx))

    print(f'#{tc} {d[e_y][e_x]}')