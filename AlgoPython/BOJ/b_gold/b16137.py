'''
절벽 고르는건 완탐
교차: 4가지 방향 탐색

오작교는 이처럼 매우 불안정하므로, 견우는 안전을 위해 두 번 연속으로 오작교를 건너지는 않기로 했다.

이게 최소 이동거리라 다익스트라로 풀었음

틀린이유 : 그냥 visited 써버림
그냥 bfs visited 갔던곳 또 못가서 안됨!!
시간만 짧으면 어디든지 갈 수 있음
갔던 곳이여도 시간 짧으면 갈 수 있음.

'''
import heapq


def is_range(r, c):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False


def bfs():
    global ans
    q = []
    heapq.heappush(q, (0, 0, 0))
    d = [[int(1e9)] * n for i in range(n)]
    d[0][0] = 0

    while q:
        time, r, c = heapq.heappop(q)
        if time > d[r][c]:
            continue
        if r == n - 1 and c == n - 1:
            ans = min(ans, time)
            return  # 다익스트라여서 return 가넝
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not is_range(nr, nc):
                continue
            if grid[r][c] > 1:  # 오작교에서는 탄탄한 땅으로밖에 못간다.
                if grid[nr][nc] == 1:
                    if d[nr][nc] > time + 1:
                        heapq.heappush(q, (time + 1, nr, nc))
                        d[nr][nc] = time + 1
            else:  # 땅에선 어디든지 갈 수 있다.
                if grid[nr][nc] == 1:
                    if d[nr][nc] > time + 1:
                        heapq.heappush(q, (time + 1, nr, nc))
                        d[nr][nc] = time + 1
                elif grid[nr][nc] > 1 and (time + 1) % grid[nr][nc] == 0:  # 타이밍 맞았으면 그냥 가!
                    if d[nr][nc] > time + 1:
                        heapq.heappush(q, (time + 1, nr, nc))
                        d[nr][nc] = time + 1
                # 안건너고 기다리는 경우
                elif grid[nr][nc] > 1 and (time + 1) % grid[nr][nc] != 0:  # 타이밍 안맞았으면 기다렸다 가!
                    if d[nr][nc] > time + (time // grid[nr][nc] + 1) * grid[nr][nc] - time:
                        heapq.heappush(q, (time + (time // grid[nr][nc] + 1) * grid[nr][nc] - time, nr, nc))
                        d[nr][nc] = time + (time // grid[nr][nc] + 1) * grid[nr][nc] - time
                        # 지금까지의 시간 + 얼마나 기다려야하는지
                        # 만약 내가 14고 다리가 3 이면 14//3 = 4 -> (4+1)*3 - 14 만큼 기다려야함.


def btk(idx):
    if idx == len(plus):
        return

    # 다리 놓는다.
    r, c = plus[idx]
    grid[r][c] = my_time
    bfs()
    grid[r][c] = 0
    btk(idx + 1)


n, my_time = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

plus = []
row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]
for i in range(n):
    for j in range(n):
        if grid[i][j] == 0:
            isOk = True
            if is_range(i + row[0], j + col[0]) and is_range(i + row[1], j + col[1]) \
                    and grid[i + row[0]][j + col[0]] == grid[i + row[1]][j + col[1]] == 0:
                isOk = False
                continue
            if is_range(i + row[1], j + col[1]) and is_range(i + row[2], j + col[2]) \
                    and grid[i + row[1]][j + col[1]] == grid[i + row[2]][j + col[2]] == 0:
                isOk = False
                continue
            if is_range(i + row[2], j + col[2]) and is_range(i + row[3], j + col[3]) \
                    and grid[i + row[2]][j + col[2]] == grid[i + row[3]][j + col[3]] == 0:
                isOk = False
                continue
            if is_range(i + row[3], j + col[3]) and is_range(i + row[0], j + col[0]) \
                    and grid[i + row[3]][j + col[3]] == grid[i + row[0]][j + col[0]] == 0:
                isOk = False
                continue
            if isOk:
                plus.append((i, j))

ans = int(1e9)
btk(0)
print(ans)
