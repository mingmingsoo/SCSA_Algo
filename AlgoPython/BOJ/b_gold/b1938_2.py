'''
통나무 옮기기
다른 방법으로 풀기
'''
from collections import deque


def find(type):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == type:
                if j + 1 < n and grid[i][j + 1] == type:  # 가로면
                    return i, j + 1, 1
                elif i + 1 < n and grid[i + 1][j] == type:  # 세로면
                    return i + 1, j, 0


n = int(input())
grid = [list(input()) for i in range(n)]
r, c, dirs = find("B")  # 통나무 중심과 가로인지 세로인지 dirs 0: 세로 / dirs 1 : 가로
er, ec, edirs = find("E")

ans = 0
row = [-1, 1, 0, 0, 1, 1, -1, - 1]
col = [0, 0, 1, -1, 1, -1, 1, -1]


def is_range(r, c):
    # 8방 검사
    for k in range(8):
        nr = r + row[k]
        nc = c + col[k]
        if not (0 <= nr < n and 0 <= nc < n) or grid[nr][nc] == "1":
            return False
    return True


def not_one(r, c, dirs):
    if dirs == 1:  # 가로면
        if grid[r][c - 1] == "1" or grid[r][c] == "1" or grid[r][c + 1] == "1":
            return False
        return True
    elif dirs == 0:  # 세로면
        if grid[r - 1][c] == "1" or grid[r][c] == "1" or grid[r + 1][c] == "1":
            return False
        return True


def bfs(r, c, dirs):
    global ans
    visited = set([(r, c, dirs)])
    q = deque([(r, c, dirs, 0)])

    while q:
        r, c, dirs, cnt = q.popleft()
        if r == er and c == ec and dirs == edirs:
            return cnt
        if dirs == 1:  # 가로면
            # up
            if r > 0 and not_one(r - 1, c, dirs) and (r - 1, c, dirs) not in visited:
                visited.add((r - 1, c, dirs))
                q.append((r - 1, c, dirs, cnt + 1))
            # down
            if r < n - 1 and not_one(r + 1, c, dirs) and (r + 1, c, dirs) not in visited:
                visited.add((r + 1, c, dirs))
                q.append((r + 1, c, dirs, cnt + 1))
            # left
            if c - 1 > 0 and not_one(r, c - 1, dirs) and (r, c - 1, dirs) not in visited:
                visited.add((r, c - 1, dirs))
                q.append((r, c - 1, dirs, cnt + 1))
            # right
            if c + 1 < n - 1 and not_one(r, c + 1, dirs) and (r, c + 1, dirs) not in visited:
                visited.add((r, c + 1, dirs))
                q.append((r, c + 1, dirs, cnt + 1))
            # rotate
            if is_range(r, c) and (r, c, 1 - dirs) not in visited:
                visited.add((r, c, 1 - dirs))
                q.append((r, c, 1 - dirs, cnt + 1))
        elif dirs == 0:  # 세로면
            # up
            if r - 1 > 0 and not_one(r - 1, c, dirs) and (r - 1, c, dirs) not in visited:
                visited.add((r - 1, c, dirs))
                q.append((r - 1, c, dirs, cnt + 1))
            # down
            if r + 1 < n - 1 and not_one(r + 1, c, dirs) and (r + 1, c, dirs) not in visited:
                visited.add((r + 1, c, dirs))
                q.append((r + 1, c, dirs, cnt + 1))
            # left
            if c > 0 and not_one(r, c - 1, dirs) and (r, c - 1, dirs) not in visited:
                visited.add((r, c - 1, dirs))
                q.append((r, c - 1, dirs, cnt + 1))
            # right
            if c < n - 1 and not_one(r, c + 1, dirs) and (r, c + 1, dirs) not in visited:
                visited.add((r, c + 1, dirs))
                q.append((r, c + 1, dirs, cnt + 1))
            # rotate
            if is_range(r, c) and (r, c, 1 - dirs) not in visited:
                visited.add((r, c, 1 - dirs))
                q.append((r, c, 1 - dirs, cnt + 1))
    return 0


print(bfs(r, c, dirs))
