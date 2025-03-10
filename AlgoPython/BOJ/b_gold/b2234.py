from collections import deque

'''
반례
2 1
15 15
답 2

틀린이유: 넘버링해준걸로 벽부스는거 확인해야하는데 방크기합해준 배열로 확인했음
'''
m, n = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

maxi = 0
num = 0
visited = [[0] * m for i in range(n)]
numbering = [[0] * m for i in range(n)]
row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]

info = {0: (0, 1, 2, 3), 1: (0, 1, 2), 2: (1, 2, 3), 3: (1, 2), 4: (0, 2, 3), 5: (0, 2),
        6: (2, 3), 7: (2,), 8: (0, 1, 3), 9: (0, 1), 10: (1, 3),
        11: (1,), 12: (0, 3), 13: (0,), 14: (3,), 15: ()}


def bfs(r, c):
    global maxi
    q = deque([(r, c)])
    ele_room = 0
    same_room = []
    while q:
        r, c = q.popleft()
        same_room.append((r, c))
        ele_room += 1
        for k in info[grid[r][c]]:
            nr = r + row[k]
            nc = c + col[k]
            if visited[nr][nc] == 0:
                visited[nr][nc] = num
                q.append((nr, nc))
    maxi = max(maxi, ele_room)
    for r, c in same_room:
        numbering[r][c] = ele_room


for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            num += 1
            visited[i][j] = num
            bfs(i, j)

ans = 0

for i in range(n):
    for j in range(m):
        my_room = visited[i][j]
        for k in range(4):
            nr = i + row[k]
            nc = j + col[k]
            if not (0 <= nr < n and 0 <= nc < m):
                continue
            if visited[nr][nc] != my_room:
                ans = max(ans, numbering[i][j] + numbering[nr][nc])
print(num)
print(maxi)
print(ans)
