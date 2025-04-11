# 10:46~12:18
'''
문제 설명
    미리 bfs로 구해놓고
    시뮬 돌려라
궁굼한게... dp, cc 매번 초기화임? 아니지?
'''
from collections import deque

n, m = map(int, input().split())
grid = [list(input()) for i in range(n)]

# 미리 방향 별 최대 좌표 구해놓기
# 그 넘버링과 무슨 문자인지도 연결
visited = [[0] * m for i in range(n)]
num = 1
location_dict = {}
word_dict = {}
row = [0, 1, 0, -1]
col = [1, 0, -1, 0]


def bfs(sr, sc):
    s = grid[sr][sc]
    q = deque([(sr, sc)])
    location = []
    while q:
        r, c = q.popleft()
        location.append((r, c))
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < m) or visited[nr][nc] or grid[nr][nc] != s:
                continue
            visited[nr][nc] = num
            q.append((nr, nc))
    location.sort()  # r기준 정렬
    # dp가 1, 3(하,상 일때)
    sr, er = location[0][0], location[-1][0]
    d1 = []
    d3 = []
    for r, c in location:
        if r == sr:
            d3.append((r, c))
        if r == er:
            d1.append((r, c))
    # d1 의 0번째가 0- 왼
    # d3의 -1번째가 0- 우
    location_dict[(num, 1, -1)] = d1[-1]  # -1이 왼
    location_dict[(num, 1, 1)] = d1[0]  # 1이 우

    location_dict[(num, 3, -1)] = d3[0]  # -1이 왼
    location_dict[(num, 3, 1)] = d3[-1]  # 1이 우

    location.sort(key=lambda x: (x[1], x[0]))  # c기준 정렬
    # dp가 0, 2( 우,왼 일때)
    sc, ec = location[0][1], location[-1][1]
    d0 = []
    d2 = []
    for r, c in location:
        if c == sc:
            d2.append((r, c))
        if c == ec:
            d0.append((r, c))
    # d0 의 0번째가 0- 왼
    # d0의 -1번째가 0- 우
    location_dict[(num, 0, -1)] = d0[0]
    location_dict[(num, 0, 1)] = d0[-1]

    location_dict[(num, 2, -1)] = d2[-1]
    location_dict[(num, 2, 1)] = d2[0]


for i in range(n):
    for j in range(m):
        if grid[i][j] != "X" and not visited[i][j]:
            visited[i][j] = num
            word_dict[num] = grid[i][j]
            bfs(i, j)
            num += 1


r, c = 0, 0
dp = 0
cc = -1
ans = ""
while True:
    num = visited[r][c]
    ans += word_dict[num]
    move = False
    for k in range(4):  # dp 4번 cc 2번
        # dp,cc 기준 좌표 찾기
        maxr, maxc = location_dict[(num, dp, cc)]
        nr = maxr + row[dp]
        nc = maxc + col[dp]
        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != "X":
            r, c = nr, nc
            move = True
            break
        else:
            cc *= -1
            maxr, maxc = location_dict[(num, dp, cc)]
            nr = maxr + row[dp]
            nc = maxc + col[dp]
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != "X":
                r, c = nr, nc
                move = True
                break
            else:
                dp = (dp + 1) % 4
    if not move:
        break
print(ans)