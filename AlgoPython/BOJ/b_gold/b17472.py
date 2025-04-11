'''
섬들을 넘버링하고
섬들의 테두리에서 가로/ 세로로 뻗었을 때 다른 섬에 닿으면 그 길이를 기록. 그담에 연결할 수 있는 최소..를 ㄻ너우마움니움
다익스트라? 는 안되고요 유니언 파인드 필요합니다.
'''
# -------------- 입력 --------------
from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

visited = [[0] * m for i in range(n)]

num = 1
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]


# -------------- 함수 --------------
def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def union(ap, bp):
    if ap != bp:
        p[bp] = ap


def bfs(r, c):
    q = deque([(r, c)])
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < m) or not grid[nr][nc] or visited[nr][nc]:
                continue
            visited[nr][nc] = num
            q.append((nr, nc))


for i in range(n):
    for j in range(m):
        if grid[i][j] and not visited[i][j]:
            visited[i][j] = num
            bfs(i, j)
            num += 1

adj = set()  # 정점 번호와 길이 .

for i in range(n):
    for j in range(m):
        if visited[i][j]:
            mosuri = False
            for k in range(4):
                nr = i + row[k]
                nc = j + col[k]
                if not (0 <= nr < n and 0 <= nc < m):
                    continue
                if grid[nr][nc] == 0:
                    mosuri = True
                    break
            if mosuri:
                for k in range(4):
                    r, c = i, j
                    dist = 0
                    while True:
                        nr = r + row[k]
                        nc = c + col[k]
                        if not (0 <= nr < n and 0 <= nc < m) or visited[nr][nc] == visited[i][j]:
                            break
                        dist += 1
                        if visited[nr][nc]:
                            if dist > 2:
                                tmp = [visited[i][j], visited[nr][nc]]
                                tmp.sort()
                                adj.add((tmp[0], tmp[1], dist - 1))
                            break
                        r = nr
                        c = nc

adj = list(adj)
adj.sort(key=lambda x: x[2])

p = [-1] * num
for i in range(1, num):
    p[i] = i

cnt, sum = 0, 0

for a, b, dist in adj:
    ap = find(a)
    bp = find(b)
    if ap != bp:
        union(ap, bp)
        sum += dist
        cnt += 1
    if cnt == num - 1:
        break

myp = find(1)

for you in range(2, num):
    youp = find(you)
    if myp != youp:
        sum = -1
        break
print(sum)
