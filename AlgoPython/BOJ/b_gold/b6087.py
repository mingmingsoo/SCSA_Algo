
'''
문제설명
    C->C
    방향전환을 최소로
구상
    bfs같당 원래의 d를 데리고다녀야함!
'''
import heapq

m, n = map(int, input().split())
grid = [list(input()) for i in range(n)]

sr, sc, er, ec = -1, -1, -1, -1
for i in range(n):
    for j in range(m):
        if grid[i][j] == "C":
            grid[i][j] = "."
            if sr == sc == -1:
                sr, sc = i, j
            else:
                er, ec = i, j

row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]
ans = int(1e9)


def bfs():
    global ans
    di = [[[int(1e9)] * 4 for i in range(m)] for i in range(n)]
    di[sr][sc][0] = 0
    di[sr][sc][1] = 0
    di[sr][sc][2] = 0
    di[sr][sc][3] = 0
    q = []
    heapq.heappush(q, (0, sr, sc, 0))
    heapq.heappush(q, (0, sr, sc, 1))
    heapq.heappush(q, (0, sr, sc, 2))
    heapq.heappush(q, (0, sr, sc, 3))

    while q:
        rotation, r, c, d = heapq.heappop(q)
        # print(r, c, d, rotation)
        # print("--------------------")
        # for _ in di:
        #     print("".join(map(str, _)))
        if rotation > di[r][c][d]:
            continue
        if r == er and c == ec:
            ans = min(ans, rotation)
            break

        nr = r + row[d]
        nc = c + col[d]
        # 그냥 갈 수 있으면 그냥 퍼져가~~
        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == ".":
            if di[nr][nc][d] > rotation:
                di[nr][nc][d] = rotation
                heapq.heappush(q, (rotation, nr, nc, d))

            right_nr = nr + row[(d + 1) % 4]
            right_nc = nc + col[(d + 1) % 4]
            left_nr = nr + row[(d - 1) % 4]
            left_nc = nc + col[(d - 1) % 4]

            if 0 <= right_nr < n and 0 <= right_nc < m and grid[right_nr][right_nc] == ".":
                if di[right_nr][right_nc][(d + 1) % 4] > rotation + 1:
                    heapq.heappush(q, (rotation + 1, nr, nc, (d + 1) % 4))
                    di[nr][nc][(d + 1) % 4] = rotation + 1

            if 0 <= left_nr < n and 0 <= left_nc < m and grid[left_nr][left_nc] == ".":
                if di[left_nr][left_nc][(d - 1) % 4] > rotation + 1:
                    heapq.heappush(q, (rotation + 1, nr, nc, (d - 1) % 4))
                    di[nr][nc][(d - 1) % 4] = rotation + 1


bfs()
print(ans)
'''
5 5
C....
####.
..C#.
.###.
.....

4 1
C..C

2 1
CC

6 5
C.....
#####.
...C#.
.####.
......

5 6
C....
####.
..C#.
.###.
.###.
.....



4 3
..*C
C.*.
*...

'''

