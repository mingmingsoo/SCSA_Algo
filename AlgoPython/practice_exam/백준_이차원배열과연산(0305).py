'''
# 코드트리 격자 숫자 놀이
2025.03.30.일
두번째 풀이

# 문제 풀고 나서 기록
    제출 횟수 2회
    문제 시작 14:11
    1차 제출  14:37 [틀린이유: 답이 0이 될 수 있음]
    문제 종료 14:38

    총 풀이시간 27분
        11~15   : 문제 이해(4)
        15~30   : row_sort(15)
        30~35   : col 일때 전치 작성, 0일때는 카운트 제외, 100까지 잘라주기(5)
        35~37   : 검증용 테케 넣어보기 (2)
                   - 근데 답이 0이 될줄은 몰랐서요
        37~38   : 틀렸습니다 -> 아 답이 0 이 될수도 있구나 검증 로직 위로 빼기(1)

  메모리 24 MB
  시간 176 ms

    회고
        1. 틀린 이유 : 답이 0이 될 수 도 있음....
                        아 저번엔 답이 100일때를 생각 못했는데 ^^ 가지가지한다 증말

        2. 전치할 때
            list(map(list, zip(*grid))) <- 이렇게하면 list로 됨
            list(zip(*grid)) <- 이거는 튜플로...

# 문제 풀면서의 기록
시간복잡도
100*100*100

2차원 배열의 값은 100이 최대임

'''
from collections import Counter

er, ec, num = map(int, input().split())
er -= 1
ec -= 1
grid = [list(map(int, input().split())) for i in range(3)]
ans = -1


def sort():
    global grid
    new_grid = []
    max_len = 0
    for row in grid:
        cnt = Counter(row)
        tmp = []
        for k, v in cnt.items():
            if k != 0:
                tmp.append([k, v])
        tmp.sort(key=lambda x: (x[1], x[0]))
        new_row = []
        for _ in tmp:
            new_row.extend(_)
        max_len = max(max_len, len(new_row))
        new_grid.append(new_row)
    for _ in new_grid:
        if len(_) < max_len:
            _.extend([0] * (max_len - len(_)))
    grid = new_grid


for t in range(0, 101):  # 100초까지 가능
    if len(grid) > er and len(grid[0]) > ec and grid[er][ec] == num:
        ans = t
        break

    if len(grid) >= len(grid[0]):
        sort()

    else:
        grid = list(zip(*grid))
        sort()
        grid = list(zip(*grid))

    grid = [_[:100] for _ in grid[:100]]
print(ans)


'''

# 백준 17140 이차원 배열과 연산 (코드트리 격자 숫자 놀이)

# 문제 풀고 나서 기록

    문제 시작 13:40
    1차 제출 14:27
    2차 제출 14:30
    총 풀이시간 50분
        0~2분    : 문제 이해(2)
        2~6분    : 문제 구상 및 초기 주석(4)
        6~47분   : 흐름대로 설계, 중간중간 행렬 잘 만들어지는지 검사(41)
                    코드 짜면서 count 잘 세고, 정렬 잘되는지 확인
                    R정렬 잘 되는지 확인
                    C정렬 잘 되는지 확인
        47~50분  : 틀려서 문제를 다시 읽음. (3)
                    내 코드는 100초가 출력될 수 없는 코드
                    -> for time range 바꿔줌

    메모리 114368 KB
    시간 192 ms

    회고
    0. 1번 틀린 이유★
        100초 까지인데 99초까지만 검사. 조금만 생각했으면 안틀리는데.. ㅠㅠㅠ 아쉽다........!!!
        0이나 100이 정답이 될 수 있나? 라고 생각했으면 됐을텐데... min/max는 필수다 !!!!!!!!!!!!
    1.
    전치 쉽게하는 법 모르는 내가 미워........................😥
    count 배열밖에 못쓰는 내가 미워.........................😥
    그래도... 해냈으니 됐다...................

    2.
    디버깅 한 번 할때마다 count가 100까지 돌아서 F8 누르는데 오래걸렸다
    '오래 걸리네?' 생각이 든 순간 함수로 빼면 됐었을텐데 ^^...... 후후...

    3.
    코드 함수화해서 다시 풀어보기!!


문제 설명
    갯수에 따른 연산.
    R연산: 행에 대해 정렬 단 행 갯수>=열갯수
    C연산: 열에 대해 정렬 단 열갯수>행갯수

    정렬 기준
    수의 등장 횟수가 커지는 순으로, 같다면 수가 커지는 순으로

    3 1 1 2
    2 1 3 1 1 2

    만약 가장 큰 행/열 을 기준으로 크기가 변함. 모자란 곳은 0을 넣어줌
    100을 넘어가면 100까지만.

출력
    A[r][c] 가 k가 되기위한 최소 시간.
    100초가 지나도 달성하지 못하면 -1 출력

구상
    성실히 구현
'''

er, ec, target = map(int, input().split())
er -= 1
ec -= 1
ans = -1
grid = [list(map(int, input().split())) for i in range(3)]
for time in range(101):

    # 4. 목표 달성 검사
    if 0 <= er < len(grid) and 0 <= ec < len(grid[0]) and grid[er][ec] == target:
        ans = time
        break

    # 1. 크기에 따른 R,C 연산
    r_size = len(grid)
    c_size = len(grid[0])
    if r_size >= c_size:
        new_grid = []
        max_row_size = 0
        for i in range(r_size):
            count = [0] * 101
            for j in range(c_size):
                if grid[i][j] == 0:
                    continue
                count[grid[i][j]] += 1
            sort_list = []
            for i in range(101):
                if count[i] > 0:
                    sort_list.append((i, count[i]))
            sort_list.sort(key=lambda x: (x[1], x[0]))
            tmp = []
            for count_num, idx in sort_list:
                tmp.append(count_num)
                tmp.append(idx)
            max_row_size = max(max_row_size, len(tmp))
            new_grid.append(tmp)
        # 2. 최대 크기 기준으로 맞춰주기
        for row in new_grid:
            if len(row) < max_row_size:
                row += [0] * (max_row_size - len(row))
    else:
        new_grid = []
        max_col_size = 0
        for j in range(c_size):
            count = [0] * 101
            for i in range(r_size):
                if grid[i][j] == 0:
                    continue
                count[grid[i][j]] += 1
            sort_list = []
            for i in range(101):
                if count[i] > 0:
                    sort_list.append((i, count[i]))
            sort_list.sort(key=lambda x: (x[1], x[0]))
            tmp = []
            for count_num, idx in sort_list:
                tmp.append(count_num)
                tmp.append(idx)
            max_col_size = max(max_col_size, len(tmp))
            new_grid.append(tmp)
        # 2. 최대 크기 기준으로 맞춰주기
        for row in new_grid:
            if len(row) < max_col_size:
                row += [0] * (max_col_size - len(row))
        # 전치.
        new_grid2 = [[0] * len(new_grid) for i in range(len(new_grid[0]))]
        for i in range(len(new_grid)):
            for j in range(len(new_grid[0])):
                new_grid2[j][i] = new_grid[i][j]
        new_grid = new_grid2

    # 3. 행 or 열 크기가 100 넘어가면 버려주기. # 해당만 하면 실행하게 바꾸기
    r_size = len(new_grid)
    c_size = len(new_grid[0])
    is_small_need = False
    if r_size > 100:
        is_small_need = True
        r_size = 100
    if c_size > 100:
        is_small_need = True
        c_size = 100

    if is_small_need:

        new_grid2 = [[0] * c_size for i in range(r_size)]
        for i in range(r_size):
            for j in range(c_size):
                new_grid2[i][j] = new_grid[i][j]
        grid = new_grid2
    else:
        grid = new_grid

print(ans)
