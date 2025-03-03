'''
문제 설명
    젤리는 오른쪽, 아래로만 가능
    n,m 도착시 승리
    짬푸는 그 맵의 숫자만큼 가능
구상
    bfs 인데 가는 만큼의 숫자를 조절
    visited가 좀 어려운데..
    너가 전에서 어디서왔냐를 기록
'''
from collections import deque

n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]
ans = "Hing"


def bfs():
    global ans
    visited = set()
    q = deque([(0, 0, grid[0][0])])
    row = [-1, 1, 0, 0]
    col = [0, 0, 1, -1]
    while q:
        r, c, jump = q.popleft()
        if r == n - 1 and c == n - 1:
            ans = "HaruHaru"
            return
        for k in range(4):
            nr = r + row[k] * jump
            nc = c + col[k] * jump
            if not (0 <= nr < n and 0 <= nc < n):
                continue
            if (r, c, nr, nc) not in visited:
                q.append((nr, nc, grid[nr][nc]))
                visited.add((r, c, nr, nc))


bfs()
print(ans)
