'''
# 코드트리 놀이기구 탑승
2025.04.03 목
두번째 풀이

# 문제 풀고 나서 기록
    제출 횟수 2회
    문제 시작 08:18
    1차 제출  20:40
    문제 종료 20:41

    총 풀이시간 24분
        18~23 : 문제 이해 및 초기 주석(5)
        23~32 : 로직 작성(9)
        32~42 : 틀렸습니다 -> 디버깅 (10)
                테케가 커서 안봤음
                분명 우선순위에서 놓친걸텐데 로직 확인
                empty 는 큰 순임 , - 붙혀서 append
  메모리 16 MB
  시간 49 ms

  회고
    1.  우선순위 틀린건 미친거야.. 똑바로 하자...............


문제 설명
학생들은 무조건 비어있는 칸에 앉는데
    1. 4방 중 좋아하는 친구수가 가장 많은
    2. 비어있는 곳이 많은
    3. 행 작, 열 작
-> 첫 학생은 무조건 1,1 에 앉게된다.

입력
    격자크기n
    학생정보 (학생 번호: 좋아하는 학생들)
출력
    다 앉히고 나서 각 학생마다 4방에 인접한 친구들이 몇명이나 있나? 로 계산
'''
n = int(input())
student_info = []
link = [0] * (n * n)
for _ in range(n * n):
    tmp = list(map(int, input().split()))
    student_info.append(tmp)
    link[tmp[0] - 1] = _

grid = [[0] * n for i in range(n)]
# 첫 학생은 무조건 1,1 에 앉는다.
first = student_info[0][0]
grid[1][1] = first
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]


for i in range(1, n * n):
    num, like_lst = student_info[i][0], student_info[i][1:]

    seat_lst = []
    for i in range(n):
        for j in range(n):
            if not grid[i][j]:
                like = empty = 0
                for k in range(4):
                    nr = i + row[k]
                    nc = j + col[k]
                    if not (0 <= nr < n and 0 <= nc < n):
                        continue
                    if not grid[nr][nc]:
                        empty += 1
                    if grid[nr][nc] in like_lst:
                        like += 1
                seat_lst.append((-like, -empty, i, j)) # empty 에 - 안붙혀서 1회틀
    seat_lst.sort()
    _1, _2, r, c = seat_lst[0]
    grid[r][c] = num

score = 0


for i in range(n):
    for j in range(n):
        num = grid[i][j]
        idx = link[num - 1]
        like_lst = student_info[idx][1:]
        like = 0
        for k in range(4):
            nr = i + row[k]
            nc = j + col[k]
            if not (0 <= nr < n and 0 <= nc < n):
                continue
            if grid[nr][nc] in like_lst:
                like += 1
        if like > 0:
            score += 10 ** (like - 1)

print(score)


'''
# 코드트리 놀이기구 탑승 (백준 21608 상어 초등학교)

# 두번째 풀이
    좌표 저장해서 점수계산할 떄 3중포문 -> 1중포문으로 줄여보기
    ... 아쉽게도 시간 차이는 없네요
    힙큐를 써서 연산이 더 있는 것 같습니다.


# 문제 풀고 나서 기록

    문제 시작 13:40
    문제 종료 14:08
    총 풀이시간 28분
        0~4분    : 문제 이해(4)
        4~6분    : 문제 구상 및 초기 주석(2)
        6~16분   : 자리 채우는 설계 1차 완료(10) -> 잘 안채워졌음
        16~19분  : 1차 디버깅(3)
                    heapq.heappush(q, (-like_num, -empty_num, i, j))
                    여기서 i,j 가 아닌 nr, nc 를 넣어서 잘 안넣어졌었음
                    변경 후 자리 채우는 설계 끝.
        19~23분  : 만족도 계산 1차 완료(4) -> 정답이 작게나옴
        23~28분  : 2차 디버깅(5)
                    근접한 친구 센건 잘 했는데 보니까
                    elif like == 2:
                    score += 2(10이여야함) 으로 잘못 들어가있었음

    메모리 113484 KB
    시간 240 ms

    회고
    1. 습관적으로 이렇게 써서 n^2 배열이 잘 안만들어졌음. 시험 때면 당황했을 것 같다. n**(2) 습관 들이기
    2. 필요한 메서드를 정의해놓고 하는 편인데... 동작이 크게 구분되지 않아서 안했음
    3. 처음에 q에 뭘 넣어야할지 고민했음. 당연히 좋아요수와 빈공간수인데 순간적으로 막혔음
    4. 다른친구들은 힙큐를 안쓴것 같은데..... 이렇게 해도 괜찮은건지 교수님께 여쭤보기

문제설명
    각자 선호하는 학생들이 있을 때
    우선순위에 맞춰 자리를 넣어줌.
입력
    맵크기N(학생수 ^2)
    학생들 정보
출력
    학생의 만족도
구상
    1. 처음 학생은 무조건 1,1에 넣는다.
    2. 완탐 때린다.?
        2중 포문에서
        우선순위를 계산. -> 힙큐로
'''
import heapq
import sys

input = sys.stdin.readline

n = int(input())
grid = [[0] * n for i in range(n)]
student_list = [list(map(int, input().split())) for i in range(n * n)]
row = [-1, 0, 1, 0]
col = [0, -1, 0, 1]
student_seat = [[0] * 2 for i in range(n * n)]
# 첫번째 학생
grid[1][1] = student_list[0][0]
student_list[0].append((1, 1))

for w in range(1, n * n):
    student = student_list[w][0]
    like_list = student_list[w][1:]

    q = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] != 0:
                continue
            like_num = 0
            empty_num = 0
            for k in range(4):
                nr = i + row[k]
                nc = j + col[k]
                if not (0 <= nr < n and 0 <= nc < n):
                    continue
                if grid[nr][nc] in like_list:
                    # 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
                    like_num += 1
                if grid[nr][nc] == 0:
                    empty_num += 1
            heapq.heappush(q, (-like_num, -empty_num, i, j))

    like_num, empty_num, r, c = heapq.heappop(q)
    grid[r][c] = student
    student_list[w].append((r, c))
# for _ in grid:
#     print(_)
# 만족도 계산
score = 0
for i in range(n * n):
    like_list = student_list[i][1:]
    r, c = student_list[i][-1][0], student_list[i][-1][1]
    like = 0
    for k in range(4):
        nr = r + row[k]
        nc = c + col[k]
        if not (0 <= nr < n and 0 <= nc < n):
            continue
        if grid[nr][nc] in like_list:
            like += 1
    if like == 1:
        score += 1
    elif like == 2:
        score += 10
    elif like == 3:
        score += 100
    elif like == 4:
        score += 1000

    # score+= 10**(like-1) # 요런 방법이...!!!
print(score)
