'''
문제 설명
    1. 공격 -> 맵 0처리 (점수 기록: 카운트 늘려주기)
    2. 0 제외 1차원 배열 변환
    3. while:
        4개이상 아닌애들만 담기
    4. 채우기

입력
    격자크기 n, 라운드 수 m
    공격 방향과 칸 수
출력
    점수 -> score = [] 배열 만들어서 한번에 계산하기

주의할 점
다 터질 때 오류 안나나? 검사하기.
7 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1
0 0
이런 테케는 없지만 인덱스 에러난다.

7 1
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0
'''

n, turn = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

# location 미리 만들어 놓기
location = set()
cnt, num, two, d = 0, 1, 0, 0
r = c = n // 2

snape_row = [0, 1, 0, -1]
snape_col = [-1, 0, 1, 0]
while (r, c) != (0, 0):
    r += snape_row[d]
    c += snape_col[d]
    location.add((r, c))

    cnt += 1
    if cnt == num:
        cnt = 0
        two += 1
        d = (d + 1) % 4
    if two == 2:
        num += 1
        two = 0

r = c = n // 2
row = [-1, 1, 0, 0]
col = [0, 0, -1, 1]
score = [0] * 3
for t in range(turn):
    d, p = map(int, input().split())
    d -= 1

    for l in range(1, p + 1):
        nr = r + row[d] * l
        nc = c + col[d] * l
        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc]:
            grid[nr][nc] = 0

    arr = []
    for sr, sc in location:
        if grid[sr][sc]:
            arr.append(grid[sr][sc])

    # 4개 이상 제거
    while True:
        arr.append(0)
        new_arr = []
        tmp = []
        same = 0
        cnt = 0
        end = True
        for num in arr:
            if num == same:
                cnt += 1
                tmp.append(num)
            elif num != same:
                if cnt <= 3:
                    new_arr.extend(tmp)
                else:
                    end = False
                    score[same - 1] += len(tmp)
                tmp = [num]
                same = num
                cnt = 1
        arr = new_arr
        if end:
            break

    # 배열 채우기
    new_arr = []
    if arr:
        arr.append(0)
        same = 0
        cnt = 0
        for num in arr:
            if num == same:
                cnt += 1
            elif num != same:
                new_arr.append(cnt)
                new_arr.append(same)
                same = num
                cnt = 1
        new_arr.pop(0)
        new_arr.pop(0)

    # 다시 이차원 배열에 넣어주기
    grid = [[0] * n for i in range(n)]
    new_arr.reverse()
    for sr, sc in location:
        if new_arr:
            grid[sr][sc] = new_arr.pop()

print(score[0] * 1 + score[1] * 2 + score[2] * 3)


'''
# 백준 21611 마법사 상어와 블리자드
# 체감난이도 골1~골2

# 문제 풀고 나서 기록

    문제 시작 14:00
    문제 종료 15:00
    총 풀이시간 60분
        00~06   : 문제 이해하면서 일단 손으로 필요한 함수 정의(6)
        06~08   : 초기 주석 및 문제 구상(2)
        08~13   : 탑다운 설계(5)
        13~15   : attack 함수 설계(2)
        15~24   : 달팽이 순서대로 위치 담는 로직 설계(9)
                    오랜만에 하니까 헷갈리대...
        24~27   : pull 함수 설계(3)
                    중력하고 비슷하다고 생각해서 쉽게 짰음
                    다만!!!!!
                    달팽이 위치 배열에 가운데도 들어가있어서 가운데도 당겨버리더라구요
                    그래서 location_idx.pop(0) 해줌

                    +) 0,0이 구슬이고 0,1이 빈공간일 때 잘 당겨지는지 확인
        27~40   : bomb 함수 설계(13)
                    상어 바로 옆에 4개 이상 있는 테케 이따 넣어보자고 메모 달아놓음
        39~56   : fill 함수 설계
                    bomb랑 비슷하게 짜려고 했음.
                    fill은 시작을 arr[0]으로 둬야하기 때문에 약~ 간 다르게 접근
                    맨 마지막 1이 1,1 로 안들어가서 보니까 마지막 1은 비교해주는 대상이 없어서 그런거 확인
                    그래서 arr에 0을 append 해줘서 1이 비교돼서 들어갈 수 있게 해줌

                   +) 새로 만들어진 new_arr을 가운데서부터 채웠는데
                    아님! 상어(가운데)는 0임!! 그거 수정해줌
        56~60   : 아까 메모해놨던 거 검증, 테케 맵하고 똑같은지 비교

    메모리 112304 KB
    시간 404 ms

    회고
        1. 저번에 교수님이 보여주셨던 문제라 읽는데 문제 이해가 빨랐음
        2. 시험 직전에 달팽이 풀고가기.... 어우 헷갈려
        3. 역시 설계가 중요하다. 설계 하고 들어가니까 잘 풀린 듯 함
        4. 왜 또 시간이 뚱뚱하지!!!! 아마도.. 나는 하나씩만 당겨서 pull에서 차이나는 듯

# 문제 풀면서의 기록
문제 설명
    1. 공격 - 얘는 쉬움
    2. 댕기기 while 필요
    3. 구슬 폭발
            while
                발견(4개이상) - 폭발
                (발견 못했으면 break)
                댕겨
    4. 순서대로 배열 만들어주고
        새로운 순서대로 배열 생성
        그걸 또 순서대로 grid 새로 생성

출력
     1×(폭발한 1번 구슬의 개수) + 2×(폭발한 2번 구슬의 개수) + 3×(폭발한 3번 구슬의 개수)
     -> bomb에서 처리

테케
7 1
0 0 0 0 0 0 0
3 2 1 3 2 3 0
2 1 2 1 2 1 0
2 1 1 0 2 1 1
3 3 1 1 1 1 2
3 3 3 1 3 3 2
2 3 2 2 3 2 3
0 0

(상어 바로 옆에 폭발하는 1이 있을 때)
'''


def make_location():  # 한번만 실행하는 함수, 달팽이 순서대로 위치 담아주기
    # 달팽이용 방향
    s_row = [0, 1, 0, -1]
    s_col = [-1, 0, 1, 0]
    r, c, d = n // 2, n // 2, 0
    num, two, cnt = 1, 0, 0
    while not (r == 0 and c == 0):

        location_idx.append((r, c))

        r = r + s_row[d]
        c = c + s_col[d]

        cnt += 1
        if cnt == num:
            d = (d + 1) % 4
            cnt = 0
            two += 1
        if two == 2:
            two = 0
            num += 1
    location_idx.pop(0)  # 가운는 빼주고
    location_idx.append((0, 0))  # 맨 끝에는 넣어주기


def attack():  # 공격!
    for dist in range(1, distance + 1):
        nr = r + row[d] * dist
        nc = c + col[d] * dist
        grid[nr][nc] = 0


def pull():  # 당겨! : 중력처럼 swap 해줌
    while True:
        p = 0  # pull 했는지 여부
        for i in range(len(location_idx) - 1):
            r, c = location_idx[i]
            nr, nc = location_idx[i + 1]
            if grid[r][c] == 0 and grid[nr][nc] != 0:
                grid[r][c], grid[nr][nc] = grid[nr][nc], grid[r][c]
                p = 1
        if not p:
            break


def bomb():
    while True:
        is_bomb = False
        idx = 0
        same = 0
        block = []

        while idx < len(location_idx):
            r, c = location_idx[idx]
            if grid[r][c] == same:
                block.append((r, c))
            else:
                same = grid[r][c]
                if len(block) >= 4:
                    num = grid[block[0][0]][block[0][1]]
                    ans[num - 1] += (len(block))
                    is_bomb = True
                    for br, bc in block:
                        grid[br][bc] = 0
                    block = [(r, c)] # <- 이거 넣어줘야함 빈배열 생성했었음
                else:
                    block = [(r, c)]

            idx += 1
        if not is_bomb:
            break

        pull()  # 다시 당기기


def fill():
    global grid
    arr = []
    for r, c in location_idx:
        if grid[r][c]:
            arr.append(grid[r][c])  # 기존 배열을 1차원 배열로 변환
    arr.append(0)  # 마지막 숫자 비교를 위해 0 넣어줌
    new_arr = []
    same = arr[0]  # 일단 첫번째 숫자를 스타트로
    cnt = 1
    idx = 1
    while idx < len(arr):
        num = arr[idx]
        if num == same:  # 같으면 갯수 증가
            cnt += 1
        else:
            new_arr.append(cnt)  # 아니면 여태 몇개였는지 추가
            new_arr.append(same)
            same = num
            cnt = 1  # cnt 초기화
        idx += 1

    grid = [[0] * n for i in range(n)]  # 배열 새로!
    for r, c in location_idx:  # 새로 만들어진 숫자들 넣어주기
        # 아무리 많아도 map을 채울 수 있는 만큼만
        if new_arr:
            grid[r][c] = new_arr.pop(0)


row = [-1, 1, 0, 0]  # 공격용 방향
col = [0, 0, -1, 1]
n, attack_num = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
location_idx = []
make_location()
r, c = n // 2, n // 2
ans = [0, 0, 0]  # 정답 출력용

for a in range(attack_num):
    d, distance = map(int, input().split())  # 공격 방향과 거리
    d -= 1

    attack()  # 공격
    pull()  # 당겨줌
    bomb()  # 폭발
    fill()  # 채워줌

print(ans[0] * 1 + ans[1] * 2 + ans[2] * 3)
