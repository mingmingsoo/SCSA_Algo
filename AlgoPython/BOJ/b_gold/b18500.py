'''
문제설명
    왼오왼오 화살날린다.
    중력영향받는다.

구상
필요한 메서드
    1. ash : 화살쏜다.
    2. fall : 클러스터가 전부 떨어져야함..
        1. 이 클러스터가 얼마나 떨어질 수 있는지 검사해야되고
        2. 바닥에서부터 검사해서 바닥에 있는 클러스터는 검사안해도됨
        3. 떨굴 수 있는 최대 높이를 계산하고 한번에 내려준다.

넣어본 테케
........
........
.....x..
...xxx..
...xx...
..x.xx..
..x...x.
.xxx..x.
5
6 6 4 3 1

'''
from collections import deque

def ashing(i):
    target = ash_list[i]
    if i % 2 == 0:  # 왼쪽화살
        for j in range(m):
            if grid[n - target - 1][j] == "x":
                grid[n - target - 1][j] = "."
                break
    else: # 오른쪽 화살
        for j in range(m - 1, -1, -1):
            if grid[n - target - 1][j] == "x":
                grid[n - target - 1][j] = "."
                break

def bfs(i, j, C, num):  # C: 클러스트 담을것인지(T/F), num : visited를 뭘로 채울 것인지.
    q = deque([(i, j)])
    while q:
        r, c = q.popleft()
        if C:
            cluster.add((r, c)) # 바닥이 아닌 클러스터들만 담는 로직 실행.
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]

            if not (0 <= nr < n and 0 <= nc < m):
                continue
            if not visited[nr][nc] and grid[nr][nc] == "x":
                visited[nr][nc] = num # 클러스트에 넘버링 해주는 과정. 1이면 바닥, 아니면 공중
                q.append((nr, nc))

def fall(cluster):
    l = 1 # 일단 떨어질수 있는 높이 1로 시작
    while True:
        isfall = True
        for r, c in cluster:
            if r + l >= n: # 못떨어지는 조건
                isfall = False
                break
            if grid[r + l][c] == "x" and visited[r + l][c] != num:
                # visited[r + l][c] != num : 내 클러스터가 아닌 다른 클러스터가 있으면 못떻어짐
                isfall = False
                break
        if not isfall:
            break
        # 이게 아니면 l 증가
        if isfall:
            l += 1

    # 이제 l만큼 떨구자  밑에서부터 swap / c 오름차순, r 내림차순
    cluster = list(cluster)
    cluster.sort(key=lambda x: (x[1],-x[0])) # 요런 방법이

    for r, c in cluster:
        grid[r][c], grid[r + l - 1][c] = grid[r + l - 1][c], grid[r][c]
        visited[r][c], visited[r + l - 1][c] = visited[r + l - 1][c], visited[r][c]


n, m = map(int, input().split())
grid = [list(input()) for i in range(n)]
ash_num = int(input())
ash_list = list(map(lambda x: int(x) - 1, input().split()))
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]

for i in range(ash_num):
    # 1.
    # 화살날림
    ashing(i)

    # 2.
    # 바닥에 붙어있는 클러스터들은 어차피 못떨어지니까
    # visited를 1로 표시해줌
    visited = [[0] * m for i in range(n)]
    for j in range(m):
        if not visited[n - 1][j]:
            visited[n - 1][j] = 1
            bfs(n - 1, j, False, 1)

    # 3.
    # 떨어질 수 있는애들은 grid가 x이면서 visited가 0인애들(아직 안간애들)
    # 떨어뜨려준다.
    num = 2 # 넘버링 해줄 거임
    for i in range(n - 2, -1, -1): # 바닥 위부터
        for j in range(m):
            if grid[i][j] == 'x' and visited[i][j] == 0:
                cluster = set() # 군집 좌표를 담아줄 set
                visited[i][j] = num # 군집 넘버링
                bfs(i, j, True, num) # 넘버링 완료
                fall(cluster) # 넘버링 된 애들 떨어뜨릴 것임.
                num += 1

for _ in grid:
    print("".join(_))
