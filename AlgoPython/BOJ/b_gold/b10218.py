from collections import deque


def find():
    global er, ec
    lst = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == ".":
                lst.append((i, j))
            elif grid[i][j] == "O":
                er, ec = i, j
    return lst


def bfs(start_balls):
    global ans
    q = deque([(start_balls, 0, "")])
    visited = set()
    visited.add(tuple(start_balls))
    while q:
        balls, time, path = q.popleft()
        if time > 10:
            ans = "XHAE"
            return
        is_end = True
        for r, c in balls:
            if not (r == er and c == ec):
                is_end = False
                break
        if is_end:
            ans = path
            return
        for k in range(4):
            new_balls = []
            for origin_r, origin_c in balls:
                r, c = origin_r, origin_c
                while True:
                    nr = r + row[k]
                    nc = c + col[k]
                    if not (0 <= nr < n and 0 <= nc < m) or grid[nr][nc] == "#":
                        break
                    r = nr
                    c = nc
                    if r == er and c == ec:
                        break
                new_balls.append((r, c))
            if tuple(new_balls) not in visited:
                visited.add(tuple(new_balls))
                q.append((new_balls, time + 1, path + "UDRL"[k]))


row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]
T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    grid = [list(input()) for i in range(n)]
    er = ec = -1
    balls = find()

    ans = "XHAE"
    # 모둔 balls에서 bfs 실행
    bfs(balls)
    print(ans)
