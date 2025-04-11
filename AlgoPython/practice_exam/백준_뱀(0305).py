'''
# 백준 뱀
2025.04.07.월
두번째 풀이

# 문제 풀고 나서 기록
    제출 횟수 1회
    문제 시작 20:22
    문제 종료 17:19

    총 풀이시간 15분
        22~28 : 문제 이해, 구상(6)
        28~36 : 로직 작성(8)
                1. 시간별 방향 pop 해줄거라 reverse 해줌
                2. 머리는 좌표 r,c로 / 꼬리는 q로 관리
        36~37 : 테케들 뱀 잘 이동하는지 확인(1)

  메모리 113500 KB
  시간 120 ms

# 문제 풀면서의 기록
머리 r,c 로 관리
꼬리 q로 관리하고 사과 안먹으면 pop_left 0으로 바꾸고 머리넣고
                사과 먹으면 pop 안함
사과 1, 뱀 2 로 관리
'''
from collections import deque

n = int(input())
grid = [[0] * n for i in range(n)]
an = int(input())
for a in range(an):
    ar, ac = map(int, input().split())
    grid[ar - 1][ac - 1] = 1  # 사과
dn = int(input())
dir_lst = []
for d in range(dn):
    t, d = input().split()
    dir_lst.append((int(t), d))
dir_lst.reverse()
r, c, d = 0, 0, 0
q = deque([(0, 0)])
grid[r][c] = 2
row = [0, 1, 0, -1]
col = [1, 0, -1, 0]
time = 0
ans = 0
while True:
    time += 1
    nr = r + row[d]
    nc = c + col[d]
    if not (0 <= nr < n and 0 <= nc < n) or grid[nr][nc] == 2:
        ans = time
        break
    if grid[nr][nc] == 1:  # 사과면 그냥 늘려!
        grid[nr][nc] = 0
        grid[nr][nc] = 2
        r = nr
        c = nc
        q.append((r, c))
    else:
        # 사과 없으면 지워!
        r = nr
        c = nc
        tr, tc = q.popleft()
        grid[tr][tc] = 0
        grid[r][c] = 2
        q.append((r, c))
    if dir_lst:
        if dir_lst[-1][0] == time:
            t, order = dir_lst.pop()
            if order == "L":
                d = (d - 1) % 4
            else:
                d = (d + 1) % 4

print(ans)



'''
# 백준 3190 뱀

# 문제 풀고 나서 기록

    문제 시작 15:55
    문제 종료 17:07
    총 풀이시간 72분
        0~2분  : 문제 이해(2)
        2~4분  : 초기 주석 및 구상 완료(2)
        4~32분  : 삽질... bam_list에 class로 bam을 만들어서 좌표들을 담으려 했는데(28)
                    꼬리와 머리 관리가 어려워서 다시 재구상
                    아 근데 여기서 q를 생각했으면 좋았을텐데 아쉽다....
                    싹 지움
        32~57분  : 재삽질.... 달팽이처럼 당기려고 했음(25)
        52~72분   : 꼬리의 방향을 담는걸로 재구상(20)
                    맘 처럼 잘 되진 않았음.
                    dir_grid에 r,c 의 d를 담아야하는데 nr, nc의 d를 담아서 잘 안됐었음.

    - 첫 풀이(꼬리의 방향을 담는 룩업테이블 사용)
        메모리 109544 KB
        시간 96 ms

    - 두번째 풀이(좌표돌을 q에 넣어주고 맨 처음에 들어왔던 애가 꼬리임.)
        메모리 113500 KB
        시간 120 ms


    회고
    1. 너무 어렵게 접근했다.
        문제 풀면서 [뱀이 엄청나게 길어져서 그러면 각 뱀의 좌표에 방향이 다 다르다...]
        라고 생각했는데 뱀의 모든 좌표에 방향을 굳이 알지 않아도 되는데.....
        q를 쓴다는 것을 아예 생각하지 못해서 그런 것 같다.
    2. 뱀이 엄청나게 길어졌을 때 이 뱀들을 다 어떻게 이동시키지? 걱정했다.
        달팽이처럼 땡겨야 되나 생각도 했다ㅠㅠㅠ
    3.
        구상
        굳이 2차원 배열로 하지 않고
        뱀의 머리와 꼬리를 기록
        -> 왜 이런생각을 했니?^^.. 쉽게쉽게 가자 쉽게쉽게 가자 ㅠㅠㅠ
    4. 최강 삽질한 문제! 그래도 경험이다.....

문제 설명
    뱀은 사과를 먹으면 길어짐
    0,0 에서 1의 길이로 시작. 처음엔 오른쪽
    사과를 안먹으면 머리 +1 꼬리 -1
    사과를 먹으면 머리+1 꼬리-0
    벽 만나면 게임 끝.
    몇초만에 게임이 끝나는가?

입력
    맵 크기
    사과 갯수
    사과 위치
    방향 전환 횟수
    방향 전환 시기와 방향

구상
    굳이 2차원배열로하지않고
    뱀의 머리와 꼬리를 기록

'''
###################################################################
# 첫 풀이 (꼬리의 방향을 담는 룩업테이블 사용)

n = int(input())
grid = [[0] * n for i in range(n)]
apple = int(input())
for i in range(apple):
    r, c = map(int, input().split())
    grid[r - 1][c - 1] = 2  # 사과
rotation_list = []
rotation_list.sort(reverse=True)
dnum = int(input())
for i in range(dnum):
    t, d = input().split()
    rotation_list.append((int(t), d))

row = [0, 1, 0, -1]
col = [1, 0, -1, 0]
time = 0
grid[0][0] = 1  # 뱀
dir_grid = [[-1] * n for i in range(n)]


def game():
    global time
    r, c, d = 0, 0, 0
    dir_grid[r][c] = 0
    tail_r, tail_c = 0, 0

    while True:
        time += 1
        nr = r + row[d]
        nc = c + col[d]
        dir_grid[r][c] = d
        if not (0 <= nr < n and 0 <= nc < n):
            return
        if grid[nr][nc] == 1:  # 내 몸이면
            return
        if grid[nr][nc] == 2:
            # 사과 있으면 먹는다.
            grid[nr][nc] = 1
            # print(tail_r, tail_c)
        else:
            # 사과 없으면
            # 땡겨야함
            # print(tail_r, tail_c)
            grid[nr][nc] = 1
            grid[tail_r][tail_c] = 0
            tail_d = dir_grid[tail_r][tail_c]
            tail_r = tail_r + row[tail_d]
            tail_c = tail_c + col[tail_d]

        r = nr
        c = nc

        for i in range(len(rotation_list) - 1, -1, -1):
            t, direction = rotation_list[i][0], rotation_list[i][1]
            if t == time:
                rotation_list.pop(i)
                if direction == "L":
                    d = (d + 3) % 4
                else:
                    d = (d + 1) % 4
                    break


game()
print(time)

###################################################################
# 두번째 풀이 q 사용
'''
어렵게 접근했는데
tail을 q로 관리하기 가보기
'''
from collections import deque

n = int(input())
grid = [[0] * n for i in range(n)]
apple = int(input())
for i in range(apple):
    r, c = map(int, input().split())
    grid[r - 1][c - 1] = 2  # 사과
rotation_list = []
rotation_list.sort(reverse=True)
dnum = int(input())
for i in range(dnum):
    t, d = input().split()
    rotation_list.append((int(t), d))

row = [0, 1, 0, -1]
col = [1, 0, -1, 0]
time = 0
grid[0][0] = 1  # 뱀


def game():
    global time
    length = 1
    r, c, d = 0, 0, 0
    tail_q = deque([(0, 0)])

    while True:
        time += 1
        nr = r + row[d]
        nc = c + col[d]
        if not (0 <= nr < n and 0 <= nc < n):
            return
        if grid[nr][nc] == 1:  # 내 몸이면
            return
        tail_q.append((nr, nc))
        if grid[nr][nc] == 2:
            # 사과 있으면 먹는다.
            grid[nr][nc] = 1
        else:
            # 사과 없으면
            # 땡겨야함
            tail_r, tail_c = tail_q.popleft()
            grid[tail_r][tail_c] = 0
            grid[nr][nc] = 1

        r = nr
        c = nc

        for i in range(len(rotation_list) - 1, -1, -1):
            t, direction = rotation_list[i][0], rotation_list[i][1]
            if t == time:
                rotation_list.pop(i)
                if direction == "L":
                    d = (d + 3) % 4
                else:
                    d = (d + 1) % 4
                    break
        # print("------------------")
        # for _ in grid:
        #     print(_)


game()
print(time)
