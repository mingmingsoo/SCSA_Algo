'''
다익스트라 문제(미세먼지와 동일)
최단 가중치로 도착지까지 도달하기.

'''
T = int(input())
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]
for tc in range(T):
    import heapq

    n = int(input())

    grid = [list(map(int, input())) for i in range(n)]

    d = [[100001] * n for i in range(n)] # 큰값으로 채우기

    def dijk():
        q = [(grid[0][0], 0, 0)]
        d[0][0] = grid[0][0]

        while q:
            cost, r, c = heapq.heappop(q)

            if r == n-1 and c == n-1: # 더 탐색할 필요가 없음
                break

            if (cost > d[r][c]): # 너가 온 길은 아까 내가 온 길보다 늦어 ! 넘어가 !
                continue

            for k in range(4):
                nr = r + row[k]
                nc = c + col[k]
                if not (0 <= nr < n and 0 <= nc < n):
                    continue

                if (d[nr][nc] > cost + grid[nr][nc]): # 최소 경로 갱신
                    d[nr][nc] = cost + grid[nr][nc]
                    heapq.heappush(q, (d[nr][nc], nr, nc))


    dijk()
    print(f"#{tc+1} {d[n - 1][n - 1]}")
