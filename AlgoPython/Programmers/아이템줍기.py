from collections import deque

rectangle =[[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
characterX = 1*2
characterY = 3*2
itemX = 7*2
itemY = 8*2

size = 60

# bfs로 채운다.
# 둘레 구한다.


grid = [[0] * size for i in range(size)]

for row in rectangle:
    x1, y1, x2, y2 = row
    x1*=2
    y1*=2
    x2*=2
    y2*=2
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            grid[i][j] = 1
# for i in range(size):
#     for j in range(size):
#         if i == characterX and j == characterY:
#             grid[i][j] =2
#         if i == itemX and j == itemY:
#             grid[i][j] =2

ans = 0
row = [-1, 1, 0, 0, 1, 1, -1, -1]
col = [0, 0, 1, -1, 1, -1, 1, -1]


def is_eight_zero(r, c):

    for k in range(8):
        nr = r+row[k]
        nc = c+col[k]
        if not(0<=nr<size and 0<=nc<size):
            continue
        if grid[nr][nc] ==0:
            return True
    return False

def is_four_zero(r, c):
    for k in range(4):
        nr = r+row[k]
        nc = c+col[k]
        if not(0<=nr<size and 0<=nc<size):
            continue
        if grid[nr][nc] ==0:
            return True
    return False

def bfs(sr, sc, er, ec):  # 8방에 0이 있는 애들만 갈 수 있고. 4방에 0이 있어야 거리를 더해줌.
    global ans
    visited = [[False] * size for i in range(size)]
    visited[sr][sc] = True
    q = deque([(sr, sc, 0)])

    while q:
        r, c, cnt = q.popleft()
        grid[r][c] = 3
        if r == er and c ==ec:
            ans = cnt+1
            return

        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]

            if not (0 <= nr < size and 0 <= nc < size):
                continue
            if not visited[nr][nc] and is_eight_zero(nr, nc) and grid[nr][nc]==1:
                visited[nr][nc] = True
                q.append((nr, nc, cnt + 1))


# bfs 가는데 ㅇㅋ 0이 ㅇ붙은 애들만
bfs(characterX, characterY, itemX, itemY)
print(ans//2)
