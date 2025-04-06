'''
문제 설명
    - 점수판이 필요하다
    - 주사위 굴린다
      (1) 범위 검사 -> 방향만 바꾸기
      (2) nr, nc 구하고
      (0) 점수
      (3) 아랫면하고 비교 해서 방향 바꾸기
헷갈리는 게 처음 위치에서도 점수 얻는지? ㄴㄴ
처음엔 항상 오른쪽
'''
from collections import deque

n, m, turn = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

score_grid = [[0] * m for i in range(n)]
visited = [[False] * m for i in range(n)]
row = [0, 1, 0, -1]
col = [1, 0, -1, 0]


def bfs(r, c):
    num = grid[r][c]
    q = deque([(r, c)])
    location = set()
    while q:
        r, c = q.popleft()
        location.add((r, c))

        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < m) or visited[nr][nc] or grid[nr][nc] != num:
                continue
            visited[nr][nc] = True
            q.append((nr, nc))
    sm = num * len(location)

    for r, c in location:
        score_grid[r][c] = sm


for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            visited[i][j] = True
            bfs(i, j)
    #  위 아래 앞  뒤 왼 오
dice = [1, 6, 5, 2, 4, 3]
r = c = d = 0
ans = 0


def rotation():
    global dice
    if d == 0:
        dice = [dice[4], dice[5], dice[2], dice[3], dice[1], dice[0]]
    elif d == 2:
        dice = [dice[5], dice[4], dice[2], dice[3], dice[0], dice[1]]
    elif d == 3:  # 북
        dice = [dice[2], dice[3], dice[1], dice[0], dice[4], dice[5]]
    elif d == 1:  # 남
        dice = [dice[3], dice[2], dice[0], dice[1], dice[4], dice[5]]


for t in range(turn):
    nr = r + row[d]
    nc = c + col[d]
    if not (0 <= nr < n and 0 <= nc < m):
        d = (d + 2) % 4
    nr = r + row[d]
    nc = c + col[d]

    ans += score_grid[nr][nc]
    rotation()

    if dice[1] > grid[nr][nc]:
        d = (d + 1) % 4
    elif dice[1] < grid[nr][nc]:
        d = (d - 1) % 4
    r = nr
    c = nc
print(ans)


'''

# 백준 23288 주사위 굴리기2 (코드트리 정육면체 한번 더 굴리기)

# 문제 풀고 나서 기록

    문제 시작 09:00
    문제 종료 09:41
    총 풀이시간 41분
        0~3분    : 문제 이해(3)
        3~6분    : 문제 구상 및 초기 주석32)
        6~12분   : 탑다운 설계(6)
        12~23분  : 1차 설계(11)
        23~31분  : 점수계산을 처음엔 dfs로 했는데 그러면 와따?가따?가 복잡해서 bfs로 바꿈(8)
                    dfs로 하면 안되는거 테케2 보고 알았음. 이걸 꼭 봐야만 아냐고^_^
                    dfs로 해도 되긴 할듯?
        31~33분  : 인덱스 에러나서 확인(2)
                    if not (0 <= r + row[d] < n and 0 <= c + col[d] < m):
                        d = (d + 2) % 4
                    여기서 이걸 %2로 했음...
        33~41분  : 점수가 너무 크게나와서 회전 로직이 잘못된건지 확인
                    문제 다시 꼼꼼히 읽고 발견!(8)
                    ->회전로직은 맞았고 방향 전환할때 순서가 문제였음
                        1. 범위 확인 2. 방향 전환 3. 주사위 굴려가 맞는 순서인데
                        3. 주사위 굴려 1. 범위 확인 2. 방향전환 이였음!!
                    문제에 친절히 마지막 주사위 상태도 알려줘서 알 수 있었음

    메모리 114368 KB
    시간 192 ms

    회고
    디버깅없이 풀 수 있는 문제였는데 아쉽다.
    그래도 빨리 찾아내서 다행.
    천천히. 꼼꼼히..!!


문제 설명
    처음 주사위 이동 방향 동쪽
        1. 이동방향으로 한 칸, 이동방향에 칸이 없다면 반대로 굴러감
        2. 주사위가 도착한 칸 점수 획득
        3. 이동방향은
            주사위 아랫면 A, 주사위 있는 칸 B
            A>B : 이동방향  시계 90도 회전
            A<B : 이동방향  반시계 90도 회전
            A=B : 이동방향 유지
    점수는 x,y 에 있는 칸 B
    x,y 에서 동서남북 이동할 수 있는 칸의 수 C를 구함
    B*C?

입력
    N,M,K
구상
    성실히 구현.

해맸던 이유
    굴러갈 수 없으면 d를 바꿔준 다음에 주사위 굴려야하는데
    주사위 굴린다음에 d를 바꿔줬음.

'''
from collections import deque


def bfs(r, c, num):
    global ele_score

    visited = [[False] * m for i in range(n)]
    visited[r][c] = True
    q = deque([(r, c, num)])

    while q:
        r, c, num = q.popleft()
        ele_score += num

        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < m):
                continue
            if not visited[nr][nc] and grid[nr][nc] == num:
                visited[nr][nc] = True
                q.append((nr, nc, num))


n, m, move_num = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

dice = [1, 6, 5, 2, 4, 3]  # 위 아래 앞 뒤 왼 오
row = [0, 1, 0, -1]  # 동 남 서 북
col = [1, 0, -1, 0]
r, c, d = 0, 0, 0  # 처음엔 동쪽
score = 0

for move in range(move_num):

    # 주사위가 이동 방향으로 한 칸 굴러간다.
    # 만약, 이동 방향에 칸이 없다면,
    # 이동 방향을 반대로 한 다음 한 칸 굴러간다.

    if not (0 <= r + row[d] < n and 0 <= c + col[d] < m): # 만약, 이동 방향에 칸이 없다면,
        d = (d + 2) % 4 # 이동 방향을 반대로 한 다음 한 칸 굴러간다.
    r = r + row[d]
    c = c + col[d]

    # 주사위가 이동 방향으로 한 칸 굴러간다.
    if d == 0:  # 동
        dice = [dice[4]] + [dice[5]] + [dice[2]] + [dice[3]] + [dice[1]] + [dice[0]]
    elif d == 1:  # 남
        dice = [dice[3]] + [dice[2]] + [dice[0]] + [dice[1]] + [dice[4]] + [dice[5]]
    elif d == 2:  # 서
        dice = [dice[5]] + [dice[4]] + [dice[2]] + [dice[3]] + [dice[0]] + [dice[1]]
    elif d == 3:  # 북
        dice = [dice[2]] + [dice[3]] + [dice[1]] + [dice[0]] + [dice[4]] + [dice[5]]

    # 주사위가 도착한 칸 (x, y)에 대한 점수를 획득한다.
    ele_score = 0
    bfs(r, c, grid[r][c])
    score += ele_score

    # 주사위의 아랫면에 있는 정수 A와 주사위가 있는 칸 (x, y)에 있는 정수 B를 비교해 이동 방향을 결정한다.
    # A > B인 경우 이동 방향을 90도 시계 방향으로 회전시킨다.
    # A < B인 경우 이동 방향을 90도 반시계 방향으로 회전시킨다.
    # A = B인 경우 이동 방향에 변화는 없다.
    dice_bottom = dice[1]
    if dice_bottom > grid[r][c]:
        d = (d + 1) % 4
    elif dice_bottom < grid[r][c]:
        d = (d + 3) % 4

print(score)
