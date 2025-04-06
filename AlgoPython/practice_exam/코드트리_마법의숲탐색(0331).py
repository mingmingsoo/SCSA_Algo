'''
# 체감난이도 골1

# 문제 풀고 나서 기록
    제출 횟수 2회
    문제 시작 14:00
    1차  제출 15:21
    문제 종료 15:30

    총 풀이시간 90분
        00~10   : 문제 이해 및 손코딩(10)
        10~14   : 손코딩 기반 초기 주석 및 필요한 변수/함수 세분화(4)
        14~15   : 입력받기(1)
        15~21   : down 설계(6)
                    clear 먼저 하려다가.. 로직이 꼬일 것 같아서 down 먼저
        21~24   : down 확인(3)
                    if r + 1 < n 이렇게 했는데
                    if r + 1 < n - 1 요렇게 해야된다.
                    왜냐하면 정령 중앙 r, 밑 r + 1
                    밑 칸이 한 칸 내려가서 해서 r+2 가 될 예정이므로 r+2 < n 이여야 하기 때문!
        24~48   : 왼쪽, 오른쪽 내려가는 거 설계(24)
                    이 부분이 제일 헷갈렸는데...
                    처음에는 왼쪽 기준 3칸만 보면 된다고 생각했는데 아니였다.
                    왼쪽으로 회전 후 한칸 내려가는 것까지 봐야하므로
                    왼쪽 3칸 + 그 밑 2칸이 된다.

                    그래서 잘못 이해한 처음 로직은 골렘들이 무조건 오른쪽으로 가버린다.
                    그래서 문제를 읽고 다시 설계를 함

                    함수화 했던걸 빼고 if 조건문으로 수정했다.

        48~52   : 왼쪽, 오른쪽 확인(4)
                    얼추 문제 예시처럼 떨어지는데 2번 골렘이 1번을 잡아먹는다(?)
                    down 함수에서 한칸 내려가고 맵을 검사해줘야하는데 내 위치를 검사해서 r+1씩으로 수정!
                    그리고 while 이 탈출 할 수 있도록 change flag 넣어줌!
        52~58   : 탈출구 표시(6)
                    탈출구가 문제 예시랑 다른 위치에 있음..
                    회전시키는 d+1, d-1 이 반대네 ? 수정!
        58~05   : 골렘탈출 bfs(7)
        05~11   : 골렘탈출 bfs 확인(6)
                    grid[r][c] == "X" 에서
                    grid[qr][qc] == "X" 로 오타 수정!
        11~12   : clear 설계(1)
        12~16   : 1번 테케 넣어보기(4)
                    답이 1 크게 나옴
                    처음엔 모든 탈출구를 "X"로 했었는데
                    남의 탈출구를 내 탈출구인 줄알고 가버리기 때문에 수정!!
                    탈출구를 -(idx+1) 로 남겨서 내 탈출구를 구분했다.
        16~21   : 검증(5)
                    (1) 테케 1번 검증
                        디버거로 로직들 확인
                         q.append((nr, nc, grid[nr][nc]))
                         만약 탈출구에서 탈출구로 이동하는 거면 넘버링이 음수값이 되버리니까
                          q.append((nr, nc, abs(grid[nr][nc])))로 수정!
                    (2) 정령 떨어지는 로직에서
                        처음엔 down 에 change 플래그를 줬는데
                        왼쪽/ 오른쪽 갈 데가 없으면 break 인 것 같아서 수정!
        21~30   : 1차 제출, 8번 테케 틀렸습니다(9)
                    정령 내려오는거 찍어보니까 오른쪽으로 갈 수 있는데 안가네?
                    디버거 돌려보니까 if / elif여서 if만 확인하고 elif는 확인을 안함 ㅠㅠㅠ 수정!!!

                    만약 if / elif 할거였으면
                    if 왼쪽 5칸:
                    elif 오른쪽 5칸: 여야하는데

                    기존 코드는
                    if 왼 3칸: <== 여기서 조건 걸리고
                        if 왼2칸: <== 여기서 조건 안걸리면
                    elif ~ <== 여기로 못내려옴!!!!!
                    그래서 오른쪽으로 못갔음...

                    그럼 수정한 코드는 왜 되냐?
                    이미 왼쪽 움직임에서 다 내려올 수 있는 만큼 내려와서 오른쪽 가는 조건은 해당할 수 가 없기 때문!


  메모리 23 MB
  시간 304 ms

    회고
        1. 테케 만들어볼걸....... 테케 만들기 어렵다고 생각해서 그냥 제출했는데
            왼/ 오 로직만 만들어볼 걸 그랬다. 머가 어렵다고 안만들었니???????

        2. 왼쪽/오른쪽 갈때 3방향만 보는 줄 알았는데 5방향 보는걸 놓쳐서 좀 헤맸다...........
            테케 보면서 이러면 오른쪽으로 무조건 쭉 가는거 아니야? 라고 생각했는데 문제 예시를 눈 크게 뜨고 보니까 아니라는 걸 알아낼 수 있었다.

# 문제 풀면서의 기록
틀린이유: 왼/오가 if elif가 아니라 if, if 여야함 ㅠㅠ
        전에코드는 왼쪽으로만 가는 코드...
문제설명
    1. 정령은 위에서 내려옴
        중앙, 위, 아래, 왼, 오, 방향 관리
    2.  while True:
            남쪽으로 쭉
            오른쪽/왼쪽 한칸
                오/왼 못가면 break
            break 조건은?
    3. 정령 이동
            골렘을 넘버링.
            출구를 -1로 기록
            내 넘버는 어디든 갈 수 있고
            출구로는 어디로든지 갈 수 있음
입력
    맵 크기 n,m, 정령수 player_num
    골렘 출발 열, 방향
    0 1 2 3
    북동남서
출력
    매 턴마다 정령 위치 합
필요한 변수
    idx, r,c,d: 골렘 넘버, 중앙, 방향
    grid: 골렘 2차원 배열 기록(출구 -1)
필요한 함수
    down()
    left()
    right()
    bfs()
    clear()
'''
# ------------------------- 입력 -------------------------
from collections import deque

n, m, player_num = map(int, input().split())
n += 3  # 위로 3개 패딩
grid = [[0] * m for i in range(n)]
row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]


# ------------------------- 함수 -------------------------
def down():
    global r, c
    while True:
        if r + 1 < n - 1 and grid[r + 1][c - 1] == grid[r + 1][c + 1] == grid[r + 2][c] == 0:
            r += 1
        else:
            break


def clear():
    for i in range(3):
        for j in range(m):
            if grid[i][j]:
                return True
    return False


def bfs():
    global r, c
    # 중앙은 r,c임
    visited = [[False] * m for i in range(n)]
    visited[r][c] = True
    q = deque([(r, c, grid[r][c])])

    while q:
        qr, qc, num = q.popleft()
        r = max(r, qr)  # 얼만큼 내려갈 수 있니
        for k in range(4):
            nr = qr + row[k]
            nc = qc + col[k]
            if not (0 <= nr < n and 0 <= nc < m) or visited[nr][nc]:
                continue
            if abs(grid[nr][nc]) == num:  # 같은 곳으로는 어디든 갈 수 이쏘...
                visited[nr][nc] = True
                q.append((nr, nc, num))
            elif grid[nr][nc] and grid[nr][nc] != num and grid[qr][qc] == -num:
                visited[nr][nc] = True
                q.append((nr, nc, abs(grid[nr][nc])))  # 탈출구까지 겹칠 수 있어서..


# ------------------------- 메인 -------------------------
ans = 0
for p in range(player_num):
    c, d = map(int, input().split())
    c -= 1
    r = 0  # 맨 처음 중앙은 격자밖
    while True:
        down()
        # 위 r-1, c -> r-1, c-1
        # 왼 r, c-1 -> r, c-2
        # 밑 r+1, c -> r+1, c-1
        if c - 1 > 0 and r + 1 < n - 1 and grid[r - 1][c - 1] == grid[r][c - 2] == grid[r + 1][c - 1] == grid[r + 1][
            c - 2] == grid[r + 2][c - 1] == 0:
            c -= 1
            r += 1
            d = (d - 1) % 4
        # 위 r-1, c -> r-1, c+1
        # 오 r, c+1 -> r, c+2
        # 밑 r+1, c -> r+1, c+1
        elif c + 1 < m - 1 and r + 1 < n - 1 and grid[r - 1][c + 1] == grid[r][c + 2] == grid[r + 1][c + 1] == \
                grid[r + 1][c + 2] == grid[r + 2][c + 1] == 0:
            r += 1
            c += 1
            d = (d + 1) % 4
        else:
            break

    grid[r][c] = grid[r - 1][c] = grid[r + 1][c] = grid[r][c - 1] = grid[r][c + 1] = p + 1  # 정령 표시

    if clear():  # 초기화!
        grid = [[0] * m for i in range(n)]
        continue

    # 탈출구 표시
    exit = {0: (r - 1, c), 1: (r, c + 1), 2: (r + 1, c), 3: (r, c - 1)}
    grid[exit[d][0]][exit[d][1]] = -(p + 1)
    bfs()
    ans += (r - 2)

print(ans)
