'''
# 코드트리 토스트 계란틀
2025.03.30.일
두번째 풀이

# 문제 풀고 나서 기록
    제출 횟수 2회
    문제 시작 12:45
    1차 제출  12:56 [틀린이유: visited 초기값 True 처리 안함 미친거야]
    문제 종료 12:58

    총 풀이시간 13분

  메모리 23 MB
  시간 212 ms

    회고
        1. 검증을 안하면 무조건 틀린다. 검증해라
        2. 진짜 검증한다 앞으로 무조건.

# 문제 풀면서 기록
bfs
답이 2000번이 될 수 있는건가?? 안되는 것 같은데 최대 1999인 듯
'''
from collections import deque

n, left, right = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
ans = 0
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]


def bfs(sr, sc):
    global change
    location = []
    q = deque([(sr, sc)])
    sm = 0
    while q:
        r, c = q.popleft()
        location.append((r, c))
        sm += grid[r][c]
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < n) or visited[nr][nc]:
                continue
            if left <= abs(grid[r][c] - grid[nr][nc]) <= right:
                visited[nr][nc] = 1
                q.append((nr, nc))
    avg = sm // len(location)
    if len(location) > 1:
        change = True
        for r, c in location:
            new_grid[r][c] = avg


for time in range(2000):

    change = False
    visited = [[0] * n for i in range(n)]
    new_grid = [_[:] for _ in grid]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] =1
                bfs(i, j)

    if not change:
        ans = time
        break
    grid = new_grid
print(ans)


'''
# 코드트리 토스트 계란틀 (백준 16234 인구이동)

# 일곱번째 풀이
    교수님 코드 참조, q 를 while에서 한번만 생성 -> 근데 이 방법은 자력으로는 생각 못할듯 ㅠㅠ
# 여섯번째 풀이
    위치담는 q 대신 lst 사용 왜나하면 조회도 많이하고 append도 많이해서!!!!!
# 다섯번째 풀이
    만약 인구이동이 많다면(최대 이천번뿐이긴 하지만......)
    bfs호출 횟수가 많아질 것이라고 생각돼서 함수화 하지 않아보겠음
# 네번째 풀이
    new_grid를 안쓰고 visited를 활용해보겠서요
# 세번째 풀이
    굳이 넘버링이 필요하지 않겠어요
    set말고 q써서 new_grid 반영해주기
# 두번째 풀이
    탈출 두개의 배열 비교하지 않고 flag

# 문제 풀고 나서 기록

    문제 시작 15:55
    문제 종료 16:13
    총 풀이시간 18분
        55~56   : 문제 이해(1)
        56~58   : 문제 구상 및 초기 주석(2)
        58~00   : 탑다운 설계(2)
        00~07   : bfs 설계(7)
                    [원래 계획]
                    :visited 넘버링 한 다음에 또 그 배열을 이중 포문 돌려서..갯수 샐라 했음
                    [수정 계획]
                    :코드 짜다보니까 bfs 끝나고 new_grid에 바로 반영하면 될 것 같아서 방향 바꿈
                    -> location set 사용
        07~12   : new_grid 에 0인 값이 있어서 확인(5)
                    디버깅 해보니까 location에 계속 같은 값 하나만 있는 거 확인

                    --------------------------- 원래 이거인데
                    r, c = q.popleft()
                    location.append((r, c))
                    summ += grid[r][c]
                    --------------------------- 이렇게 되어있었음 으휴
                    location.append((r, c))
                    summ += grid[r][c]
                    r, c = q.popleft()

        12~13   : 코드 이상한 부분 없는지 확인(1)

    첫 제출
        메모리 167836 KB
        시간 1500 ms

    마지막 제출
        메모리 117404 KB
        시간 760 ms

    회고
        냅다 내지 말고 제출 전에 최적화 할 수 없는지 고민 좀 해보자...............
        안써도 됐던것
        1. 넘버링
        2. new_grid
        3. grid == new_grid -> flag로 변경


# 문제 풀면서의 기록
문제설명
    2차원배열이 있을때
    상하좌우 인접한 칸과 내 차이가 기준에 해당하면 합쳐준다.
    -> 넘버링 필요...
    계란 이동이 없을떄까지 반복한다.

구상
    bfs로 넘버링 한다.
    넘버링 후 계산.
출력
    계란의 이동이 일어난 총 횟수

'''
###############################################################################
# 일곱번째 풀이
from collections import deque

n, small, big = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
time = 0
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]

while True:

    visited = [[False] * n for i in range(n)]
    is_exit = True
    q = deque()
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                q.append((i,j))
                visited[i][j] = True
                location = []
                summ = 0
                while q:
                    r, c = q.popleft()
                    location.append((r, c))
                    summ += grid[r][c]
                    for k in range(4):
                        nr = r + row[k]
                        nc = c + col[k]
                        if not (0 <= nr < n and 0 <= nc < n) or visited[nr][nc]:
                            continue
                        if small <= abs(grid[r][c] - grid[nr][nc]) <= big:
                            visited[nr][nc] = True
                            q.append((nr, nc))

                ele_num = summ // len(location)
                if len(location) > 1:
                    is_exit = False
                    for r, c in location:
                        grid[r][c] = ele_num

    if is_exit:
        break
    time += 1

print(time)
###############################################################################
# 첫 풀이
from collections import deque

n, small, big = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
time = 0
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]


def bfs(r, c, numbering):
    q = deque([(r, c)])
    cnt = 0
    location = set()
    summ = 0
    while q:
        r, c = q.popleft()

        location.add((r, c))
        summ += grid[r][c]
        cnt += 1
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < n):
                continue
            if visited[nr][nc] == 0 and small <= abs(grid[r][c] - grid[nr][nc]) <= big:
                visited[nr][nc] = numbering
                q.append((nr, nc))

    ele_num = summ // cnt
    for r, c in location:
        new_grid[r][c] = ele_num


while True:

    # 넘버링,
    visited = [[0] * n for i in range(n)]
    numbering = 1
    new_grid = [_[:] for _ in grid]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = numbering
                bfs(i, j, numbering)
                numbering += 1
    if grid == new_grid:
        break
    else:
        grid = new_grid
    time += 1

print(time)
