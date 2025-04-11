'''
# 04.06.일 2회차 풀이
# 코드트리 고대문명유적탐사

# 문제 풀고 나서 기록

    제출 횟수 1회
    문제 시작 16:54
    문제 종료 17:29
    총 풀이시간 35분
        54~00   : 문제 이해 및 손코딩(6)
        00~08   : rotation 설계(8)
        08~13   : bfs 설계(5)
        13~20   : bfs에서 유물 좌표도 반환해야겠다 해서 수정(7)
                    & 반환된 좌표 0으로 만들고 채우는 로직 작성
        20~29   : 테케 답이 안나와서 디버깅(9)
                    회전은 잘 됐는데, sort 해서 뽑아낸게 그 회전한 맵이 아니라 알아차렸음

                    sel.append((-cnt, degree, c, r, grid))
                    여기서 맵을 통쨰로 넣어주는데 깊은 복사가 안돼서 답이 안나왔었음! 수정!
                    sel.append((-cnt, degree, c, r, [_[:] for _ in grid]))

    메모리 22 MB
    시간 166 ms

    회고
        1. 맞추고 나서 리팩토링 하다가 1회틀함 시험땐 정직히 짜자 ^^ 코드 짧은게 좋은게 아니다
        2. 깊은 복사를 잊지마!

# 문제 풀면서의 기록
문제 설명
    1. 격자 선택
    2. bfs 진행 (while)
'''
from collections import deque

n = 5
turn, fn = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
fill = list(map(int, input().split()))
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]


def rotation(small_grid):
    ro = [[0] * 3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            ro[i][j] = small_grid[3 - j - 1][i]
    return ro


def bfs():
    total = 0
    visited = [[False] * n for i in range(n)]
    lo = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                ele = 0
                visited[i][j] = True
                q = deque([(i, j)])
                ele_lo = []
                while q:
                    qr, qc = q.popleft()
                    ele_lo.append((qr, qc))
                    ele += 1
                    for k in range(4):
                        nqr = qr + row[k]
                        nqc = qc + col[k]
                        if not (0 <= nqr < n and 0 <= nqc < n) or visited[nqr][nqc] or grid[nqr][nqc] != grid[i][j]:
                            continue
                        visited[nqr][nqc] = True
                        q.append((nqr, nqc))
                if ele >= 3:
                    lo.extend(ele_lo)
                    total += ele

    return total, lo


for t in range(turn):
    ans = 0
    sel = []

    for r in range(3):
        for c in range(3):
            grid_origin = [_[:] for _ in grid]
            for degree in range(90, 360, 90):
                small_grid = [_[c:c + 3] for _ in grid[r:r + 3]]
                ro = rotation(small_grid)
                for i in range(3):
                    for j in range(3):
                        grid[i + r][j + c] = ro[i][j]
                cnt, location = bfs()
                if cnt:
                    sel.append((-cnt, degree, c, r, [_[:] for _ in grid]))
                small_grid = ro
            grid = [_[:] for _ in grid_origin]

    if not sel:
        break
    sel.sort()
    score, degree, cc, rr, new_grid = sel[0]
    grid = new_grid

    while True:
        cnt, location = bfs()
        if cnt:
            ans += cnt
            for r, c in location:
                grid[r][c] = 0
        else:
            break
        for j in range(n):
            for i in range(n - 1, -1, -1):
                if not grid[i][j]:
                    grid[i][j] = fill.pop(0)
    print(ans, end=" ")

'''
# 체감난이도 골1

# 문제 풀고 나서 기록
    제출 횟수 1회
    문제 시작 09:00
    문제 종료 10:08

    총 풀이시간 68분
        00~06   : 문제 이해 및 손코딩(6)
        06~10   : 손코딩 기반 초기 주석 및 필요한 변수/함수 세분화(6)
        10~12   : 입력받기(2)
        12~19   : 90,180,270 회전 설계(7)
        19~40   : bfs 로직 및 확인(21)
                    오잉 문제 예시에서 7인 애가 2개 이상은 나와야 하는데 한 개만 나오네..
                    -> 당연하지 90도 회전만 하고 bfs 돌렸으니까!ㅋㅋ
                    -> 오키오키, 나머지 180 / 270 회전 후 bfs 돌려보니까
                        문제 예시처럼 7인 애가 2개 나옴!!
        40~51   : 우선순위에 해당하는 정보로 맵 회전하기, 지우기, 채우기(11)
                    지우려면 위치정보도 받아두면 좋겠다 해서 bfs에서 위치정보도 받게 수정
        51~54   : 유물이 있을 때까지 제거해주고 채워주는 while 로직 작성(3)
                    위에 코드들 복붙!
        54~08   : 검증(14)
                1. 인덱스 에러나서 if rotation_lst: 추가해서
                    없으면 break 하게 수정!
                2. 테케와 동일한 2차원 배열을 가지는지
                3. 180도 회전이 1등했을 때 잘 회전하고 지워지는지 확인
                4. 오타없는지 확인!

  메모리 24 MB
  시간 162 ms

    회고
        1. 매 로직마다 확인 후 진행해서 디버깅을 줄였다!
            이렇게 동작 순서가 확실히 나누어져 있는 문제들은 편한 것 같다....
        2. 검증을 오래했는데 잘 했다! 덕분에 한번에 맞춤!!

# 문제 풀면서의 기록
90,180,270 for문으로 한번에
문제 설명
    5*5, 유물 번호 1~7, 총 K턴
    1. 3*3 격자 90,180,270 회전
        (1) 유물 1차 획득이 높은 순
        (2) 각도가 작은
        (3) 열, 행 작은 순으로 선택
        * 유물 1차 획득은 3개 이상 사라질 수 있는 조각의 총 "갯수"
    2. 사라진 빈 칸에 열 작, 행 큰 순으로 채워줌
        for j in range(n):
            for i in range(n-1,-1,-1):
                if grid[i][j] == 0:~

        popleft 필요

    3. 다시 bfs
        while
            find = False
            bfs()
            if not find:
                break
    4. bfs 발견 못하면 종료
주의할 점
    출력형태 만족하는지 확인
    무조건 회전하는거지? 0도는 없는거지?
1 20
7 6 7 6 7
6 7 6 7 6
6 7 1 5 4
7 9 8 -1 1
5 4 3 2 7
3 2 3 5 2 4 6 1 3 2 5 6 2 1 6 6 7 5 4 2 2 3 1 3 1 2 4 2 1 3

180도 회전이 선택됨
'''
# --------------------------- 입력 ---------------------------
from collections import deque

n = 5
turn_num, fill_num = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
fill_lst = list(map(int, input().split()))  # 얘가 모자랄 일이 없다는거지?

row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]

# --------------------------- 함수 ---------------------------
def rotation(grid):
    ro_grid = [[0] * 3 for i in range(3)]

    for i in range(3):
        for j in range(3):
            ro_grid[i][j] = grid[3 - j - 1][i]

    return ro_grid


def bfs(sr, sc):
    q = deque([(sr, sc)])
    num = grid[sr][sc]
    ele_lo = []
    ele = 0
    while q:
        r, c = q.popleft()
        ele_lo.append((r, c))
        ele += 1
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < n) or visited[nr][nc] or grid[nr][nc] != num:
                continue
            visited[nr][nc] = True
            q.append((nr, nc))
    if ele >= 3:
        ele_location.extend(ele_lo)
        return ele
    else:
        return 0



def delete(location):
    for lr, lc in location:
        grid[lr][lc] = 0


def fill():
    for j in range(n):
        for i in range(n - 1, -1, -1):
            if grid[i][j] == 0:
                grid[i][j] = fill_lst.pop(0)


def cal():
    global cnt
    for r in range(n):
        for c in range(n):
            if not visited[r][c]:
                visited[r][c] = True
                cnt += bfs(r, c)

# --------------------------- 메인 ---------------------------
for turn in range(turn_num):
    ans = 0
    rotation_lst = []
    grid_origin = [_[:] for _ in grid]
    for i in range(n - 2):
        for j in range(n - 2):
            small_grid = [_[j:j + 3] for _ in grid[i:i + 3]]

            for degree in range(90, 360, 90):
                ro = rotation(small_grid)
                for r in range(3):
                    for c in range(3):
                        grid[r + i][c + j] = ro[r][c]

                cnt = 0
                ele_location = []
                visited = [[False] * n for i in range(n)]
                cal()

                if cnt > 0:
                    rotation_lst.append((-cnt, degree, (j, i), ele_location))

                grid = [_[:] for _ in grid_origin]
                small_grid = [_[:] for _ in ro]

    if rotation_lst:
        rotation_lst.sort()
        cnt, degree, (j, i), location = rotation_lst[0]
        ans += abs(cnt)
    else:
        break

    # 선택한거 기준으로 grid 실제로 반영
    small_grid = [_[j:j + 3] for _ in grid[i:i + 3]]
    ro_grid = [[0] * 3 for i in range(3)]
    for ro in range(0, degree, 90):
        ro_grid = rotation(small_grid)
        small_grid = [_[:] for _ in ro_grid]

    for r in range(3):
        for c in range(3):
            grid[r + i][c + j] = ro_grid[r][c]

    delete(location)
    fill()

    while True:
        cnt = 0
        ele_location = []
        visited = [[False] * n for i in range(n)]
        cal()

        if cnt > 0:
            ans += len(ele_location)
            delete(ele_location)
            fill()

        else:
            break

    print(ans, end=" ")
