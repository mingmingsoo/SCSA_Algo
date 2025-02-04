# 풀이시간: 50분
# 제출횟수: 1회
# 시간: 176ms
# 메모리: 75,196kb

'''
문제 시작 09:10
문제 종료 10:00

문제 설명
가장 높은 봉우리에서 낮은 지형으로의 탐색
가장 긴 등산로를 찾아야함
딱 한번 k만큼 지형을 깎을 수 있음.

1. 가장 높은 곳을 찾음. 여러개라 list에 담아주기.
2. 높은 곳에서 dfs
3. 깎았는지를 여부를 데리고 와야함. 즉 visited 해제가 필요
4. 최대 갈 수 있는 거리이므로 다 깎으면 안되고 최소로 깎아야함

'''

T = int(input())
for tc in range(T):

    n, kk = map(int, input().split())  # 맵 크기와 깎을 수 있는 높이
    grid = [[] for i in range(n)]
    maxH = -1
    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(n):
            grid[i] = tmp
            if (grid[i][j] > maxH):
                maxH = grid[i][j]
    high_list = []
    for i in range(n):
        for j in range(n):
            if (grid[i][j] == maxH):
                high_list.append((i, j))

    # print(maxH, high_list)

    ans = 0
    row = [0, 1, -1, 0]
    col = [-1, 0, 0, 1]


    def dfs(r, c, h, bomb, dist): # 위치, 최대높이, 깎을 수 있는지 여부, 현재까지의 거리
        global ans
        ans = max(ans, dist)  # 최대거리 갱신

        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if (not (0 <= nr < n and 0 <= nc < n)):
                continue

            if (not visited[nr][nc] and grid[nr][nc] < h):  # 낮으면 조건 없이 갈 수 있음
                visited[nr][nc] = True
                dfs(nr, nc, grid[nr][nc], bomb, dist + 1)
                visited[nr][nc] = False # 방문체크 해제 필요 -> 다시 돌아와서 탐색해야 하므로
            elif (not visited[nr][nc] and grid[nr][nc] - kk < h and bomb):
		            # 깎아서 낮아질 수 있고 기회가 있다면
                visited[nr][nc] = True
                origin = grid[nr][nc] # 되돌려 줘야함
                grid[nr][nc] = grid[r][c] - 1  # 최소로만 깎기
                dfs(nr, nc, grid[nr][nc], False, dist + 1)
                 # 원상복구
                visited[nr][nc] = False
                grid[nr][nc] = origin


    for sr, sc in high_list:
        visited = [[False] * n for i in range(n)]  # 매 경우 탐색하므로 visited 매번 초기화 필요
        visited[sr][sc] = True
        dfs(sr, sc, maxH, True, 1)

    print(f"#{tc + 1} {ans}")


