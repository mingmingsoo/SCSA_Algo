'''
# 코드트리 시공의 돌풍
2025.03.30.일
두번째 풀이

# 문제 풀고 나서 기록

    문제 시작 13:47
    문제 종료 14:06
    총 풀이시간 19분
        47~49   : 문제 이해(2)
        49~56   : 확산 함수(7)
                    -> 잘 되는지 확인
        56~06   : 회전 함수(10)
                    -> 잘 되는지 확인


  메모리 25 MB
  시간 557 ms

# 문제 풀면서 기록
시간복잡도
n*m*k
'''
n, m, time = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

air1 = (0, 0)
air2 = (0, 0)


def find():
    global air1, air2
    for i in range(n):
        if grid[i][0] == -1:
            air1 = (i, 0)
            air2 = (i + 1, 0)
            return


find()

row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]


def spread():
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0:
                rnd = 0
                for k in range(4):
                    nr = i + row[k]
                    nc = j + col[k]
                    if not (0 <= nr < n and 0 <= nc < m) or grid[nr][nc] < 0:
                        continue
                    rnd += 1
                munji = grid[i][j] // 5
                for k in range(4):
                    nr = i + row[k]
                    nc = j + col[k]
                    if not (0 <= nr < n and 0 <= nc < m) or grid[nr][nc] < 0:
                        continue
                    plus_grid[nr][nc] += munji
                plus_grid[i][j] -= munji * rnd


def rotation():
    # 위에 반시계
    for i in range(air1[0], 0, -1):
        grid[i][air1[1]], grid[i - 1][air1[1]] = grid[i - 1][air1[1]], grid[i][air1[1]]
    for j in range(m - 1):
        grid[0][j], grid[0][j + 1] = grid[0][j + 1], grid[0][j]
    for i in range(air1[0]):
        grid[i][m - 1], grid[i + 1][m - 1] = grid[i + 1][m - 1], grid[i][m - 1]
    for j in range(m - 1, 0, -1):
        grid[air1[0]][j], grid[air1[0]][j - 1] = grid[air1[0]][j - 1], grid[air1[0]][j]
    grid[air1[0]][air1[1] + 1] = 0
    grid[air1[0]][air1[1]] = -1

    # 아래 시계
    for i in range(air2[0], n - 1):
        grid[i][air2[1]], grid[i + 1][air2[1]] = grid[i + 1][air2[1]], grid[i][air2[1]]
    for j in range(m - 1):
        grid[n - 1][j], grid[n - 1][j + 1] = grid[n - 1][j + 1], grid[n - 1][j]
    for i in range(n - 1, air2[0], -1):
        grid[i][m - 1], grid[i - 1][m - 1] = grid[i - 1][m - 1], grid[i][m - 1]
    for j in range(m - 1, 0, -1):
        grid[air2[0]][j], grid[air2[0]][j - 1] = grid[air2[0]][j - 1], grid[air2[0]][j]
    grid[air2[0]][air2[1] + 1] = 0
    grid[air2[0]][air2[1]] = -1


for t in range(time):
    plus_grid = [[0] * m for i in range(n)]
    spread()

    for i in range(n):
        for j in range(m):
            grid[i][j] += plus_grid[i][j]

    rotation()

print(sum(map(sum, grid)) + 2)


'''
# 두번째  풀이
    공기청정기 찾는 로직 수정 : 찾자마자 break 하고 down_r을 up_r+1로 수정 -> min, max 안써도됨
    답 구하는 함수 수정 : 그냥 합해버리고 +2 하기 -> if 연산 줄이기

# 코드트리 시공의 돌풍 (백준 17144 미세먼지 안녕!)

문제 풀고 나서 기록

    문제 시작 13:40
    문제 종료 14:18
    총 풀이시간 36분
        0~6분    : 문제 이해(3)
        6~9분    : 문제 구상 및 초기 주석(3)
        9~12분   : 탑다운 설계(3)
        12~19분  : 1차 설계+ 확산 잘 안되는거 확인(7)
        19~23분  : 디버깅 완료 후 확산로직 잘 되는거 확인(4)
        23~33분  : 회전 로직, 마지막 먼지 세는 로직 완료(10)
        33~36분  : 문제 다시 읽고 내가 놓친 부분 없는지, n,m 범위 확인(3)
        제출

    메모리 129056 KB
    시간 736 ms (준영-316ms, 완진-440ms -> 왜 내가 더 긴지 분석 필요)

    회고
    구현문제에서 디버깅을 항상 하는 편이라 오래걸리는 편인데....풀어봤던 문제라 디버깅 없이 풀 수 있었습니다.
    +) plus_grid에 더해줄걸 grid에 더해줘서 났던 오류말고는 없었습니다.
    확산을 주변칸에 방해없이(?) 할 지 미리 구상하고 들어갔습니다.
    (내가 얼만큼 확산받냐) and (나는 얼마나 남냐) 를 잘 더해주기 위해 배열을 2가지 사용했습니다.
    계획했던 메서드보다 count_round, plus 메서드를 사용했습니다.



문제설명
    먼지는 상하좌우 인접하게 퍼져나간다
    주변은 먼지//5 가되고 중앙은 중앙 - 먼지//5 * 확산한 칸

    그리고 위 - 반시계, 아래 - 시계로 돈다

필요한 메서드
    wind - 확산
        1. 얼마나 더해지는지 필요한 2차원배열
        2. 남은 값을 기록해주는 배열
    rotate_up - 위 회전
    rotate_down - 아래 회전
    count - 먼지 갯수
'''


def count_round(r, c):  # 주변 몇개에 확산할 수 있는지 계산하는 함수
    ele_count = 0
    for k in range(4):
        nr = r + row[k]
        nc = c + col[k]

        if not (0 <= nr < n and 0 <= nc < m):
            continue
        if (nr, nc) == (up_r, 0) or (nr, nc) == (down_r, 0):
            continue
        ele_count += 1

    return ele_count


def plus(r, c, num):  # 나의 주변에 위치한 애들한테 내 먼지들을 확산하는 함수
    global origin_grid, plus_grid
    for k in range(4):
        nr = r + row[k]
        nc = c + col[k]

        if not (0 <= nr < n and 0 <= nc < m):
            continue
        if (nr, nc) == (up_r, 0) or (nr, nc) == (down_r, 0):
            continue
        plus_grid[nr][nc] += num  # 여기서 grid += 로 해서 디버깅했음


def wind():  # 바람을 일으키는 전체 함수
    global origin_grid, plus_grid
    origin_grid = [[0] * m for i in range(n)]  # 내가 얼만큼 남는지
    plus_grid = [[0] * m for i in range(n)]  # 내가 얼마나 더해질건지

    for i in range(n):
        for j in range(m):
            if (i, j) == (up_r, 0) or (i, j) == (down_r, 0):  # 에어컨이면 넘어가
                continue

            round = count_round(i, j)
            wind_num = grid[i][j] // 5
            origin_grid[i][j] = grid[i][j] - wind_num * round
            plus(i, j, wind_num)

    # 원본배열에 반영
    for i in range(n):
        for j in range(m):
            if (i, j) == (up_r, 0) or (i, j) == (down_r, 0):
                continue
            grid[i][j] = origin_grid[i][j] + plus_grid[i][j]  # 나 = 나에서 남아있는 먼지 + 확산받은 먼지


def rotate_up():
    # 위로 회전!
    # up_r을 기준으로 댕겨주기

    for i in range(up_r, 0, -1):
        grid[i][0] = grid[i - 1][0]
    for j in range(m - 1):
        grid[0][j] = grid[0][j + 1]
    for i in range(0, up_r):
        grid[i][m - 1] = grid[i + 1][m - 1]
    for j in range(m - 1, 0, -1):
        grid[up_r][j] = grid[up_r][j - 1]

    grid[up_r][0] = -1  # 공기청정기 복구!
    grid[up_r][1] = 0  # 청소!


def rotate_down():
    # 아래로 회전!
    # down_r을 기준으로 댕겨주기

    for i in range(down_r, n - 1):
        grid[i][0] = grid[i + 1][0]

    for j in range(m - 1):
        grid[n - 1][j] = grid[n - 1][j + 1]

    for i in range(n - 1, down_r, -1):
        grid[i][m - 1] = grid[i - 1][m - 1]

    for j in range(m - 1, 0, -1):
        grid[down_r][j] = grid[down_r][j - 1]

    grid[down_r][0] = -1  # 공기청정기 복구!
    grid[down_r][1] = 0  # 청소!


def count():  # t초 후에 총 몇개의 미세먼지가 있는지 세주는 함수
    sum = 0
    for i in range(n):
        for j in range(m):
            sum += grid[i][j]
    return sum


n, m, T = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

# 공기청정기 위치를 찾음
up_r, down_r = -1, -1

for i in range(n):
    if grid[i][0] == -1:
        up_r = i
        down_r = up_r + 1
        break

# print(up_r, down_r)
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]

for t in range(T):  # T 시간 만큼

    origin_grid = [[0] * m for i in range(n)]
    plus_grid = [[0] * m for i in range(n)]

    # 미세먼지 확장
    wind()
    print("===============")
    for _ in grid:
        print(*_)
    # 위에 회전
    rotate_up()
    # 아래 회전
    rotate_down()
    print("===============")
    for _ in grid:
        print(*_)

ans = count()
print(ans+2)
