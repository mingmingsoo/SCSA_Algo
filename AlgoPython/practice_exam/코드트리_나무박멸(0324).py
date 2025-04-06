'''
문제 설명
    1. 나무 성장
    2. 나무 번식 - plus_grid 필요
    3. 제초제 - 조건 확인 -> 정답 더해주기
        - c+1년 제초제 남기기 -> kill_grid 필요
        - -1년 빼주기
입력
    맵 n, 총 년 수 turn, 확산 범위 l, 제초제 년수 kill

5 5 2 1
0 0 0 0 0
0 30 23 0 0
0 0 -1 0 0
0 0 17 46 77
0 0 0 12 0

5 5 2 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0

5 5 2 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
'''

n, turn, length, kill = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
kill_grid = [[0] * n for i in range(n)]
ans = 0
row = [-1, 1, 0, 0, 1, 1, -1, -1]
col = [0, 0, 1, -1, 1, -1, 1, -1]
for t in range(turn):

    # 1. 나무 성장
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0:
                cnt = 0
                for k in range(4):
                    nr = i + row[k]
                    nc = j + col[k]
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 0:
                        cnt += 1
                grid[i][j] += cnt

    # 2. 번식
    plus_grid = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0:
                cnt = 0
                for k in range(4):
                    nr = i + row[k]
                    nc = j + col[k]
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and kill_grid[nr][nc] == 0:
                        cnt += 1
                if cnt:
                    tree = grid[i][j] // cnt
                    for k in range(4):
                        nr = i + row[k]
                        nc = j + col[k]
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and kill_grid[nr][nc] == 0:
                            plus_grid[nr][nc] += tree
    for i in range(n):
        for j in range(n):
            if plus_grid[i][j]:
                grid[i][j] += plus_grid[i][j]

    # 3. 제초제
    lst = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0:
                sm = grid[i][j]
                for k in range(4, 8):
                    for l in range(1, length + 1):
                        nr = i + row[k] * l
                        nc = j + col[k] * l
                        if not (0 <= nr < n and 0 <= nc < n):
                            break
                        if grid[nr][nc] > 0:
                            sm += grid[nr][nc]
                        else:
                            break
                lst.append((-sm, (i, j)))
    if lst:
        lst.sort()
        tree, (r, c) = lst[0]
        ans += abs(tree)

        # 제초제 뿌리고 년 수 기록
        for k in range(4, 8):
            for l in range(1, length + 1):
                nr = r + row[k] * l
                nc = c + col[k] * l
                if not (0 <= nr < n and 0 <= nc < n):
                    break
                if grid[nr][nc] > 0:
                    grid[nr][nc] = 0
                    kill_grid[nr][nc] = kill + 1
                else:
                    kill_grid[nr][nc] = kill + 1
                    break
        grid[r][c] = 0
        kill_grid[r][c] = kill + 1  # 본인 위치도

    for i in range(n):
        for j in range(n):
            if kill_grid[i][j]:
                kill_grid[i][j] -= 1

print(ans)


'''
# 코드트리 나무박멸
# 체감난이도 골1~골2

# 문제 풀고 나서 기록
    제출 횟수 1회
    문제 시작 14:00
    문제 종료 14:48
    총 풀이시간 48분
        00~04   : 문제 이해(4)
        04~09   : 초기 주석 및 문제 구상(5)
        09~11   : 탑다운 설계(2)
                    grow, spread, kill
                    나무 재테크처럼 grow, spread 로직 합쳐야하나? 했지만
                    시간이 충분하기에 안전하게 짜기 위해 grow, spread 나눔
        11~14   : [grow 설계](3)
                    벽이 -1이라 조건을 [grid[i][j] > 0] 으로 줬음
        14~19   : [spread 설계](5)
                    grid[i][j] == 0 and  kill_grid[i][j] == 0
                        빈 공간      and  제초제 없으면
                    위 조건으로 empty 를 세서 번식하게 했음
        19~34   : [kill 설계](15)
                    가장 꼼꼼히 봐야하는 함수!!
                    로직 중간중간 생각나는 엣지케이스가 있어서 기록해둠
                    오잉? 문제랑 제초제 퍼지는 영역이 달라서 보니까
                    "단 전파되는 도중 벽이 있거나 나무가 아예 없는 칸이 있는 경우, 그 칸 까지는 제초제가 뿌려지며 그 이후의 칸으로는 제초제가 전파되지 않습니다."
                    내 코드는 벽 or 나무 없는 칸 발견시 바로 break인데
                    그게아니라 제초제는 거기까지 뿌릴 수 있고 그 다음 break임 수정!

                    ################ before ##################
                    for k in range(4):
                        for l in range(1, dist + 1):
                            nr = i + row2[k] * l
                            nc = j + col2[k] * l
                            if not (0 <= nr < n and 0 <= nc < n) or grid[nr][nc] <= 0:
                                break
                            kill_cnt += grid[nr][nc]
                            ele_kill.append((nr, nc))

                    ################ after ##################
                    for k in range(4):
                        for l in range(1, dist + 1):
                            nr = i + row2[k] * l
                            nc = j + col2[k] * l
                            if not (0 <= nr < n and 0 <= nc < n):
                                break
                            kill_cnt += grid[nr][nc]
                            ele_kill.append((nr, nc))
                            if grid[nr][nc] <= 0:  # 검증 필요 0인곳 제초제 뿌리는지 확인 필요
                                break

        34~36   : 제초제 해 지나면 없어지는 로직 완료(2)
                    채워주자마자 1씩 빼줄거니까
                    for r, c in location:
                        kill_grid[r][c] = spray + 1         <- spray + 1 로 설정해줌
                        grid[r][c] = 0
                    제초년수는 계속 증가하는 것이 아니므로 += 가 아니라 = 다!
        36~37   :  2번 테케 zero division 에러!(1)
                    의심했던 부분인데 2번 테케에서 걸러줘서 땡큐
                    if empty: 조건 추가!
        37~40   : 아이쿠 그래도 2번 테케 답이 안나와서 보니까(3)
                    제초제만 뿌려주고 grid[i][j] = 0 , 즉 나무 죽이는 과정은 없어서 추가!
                    kill_cnt += grid[nr][nc]
                    여기서 벽도 포함되가지고 -1 되버려서 위치 바꿔줌!

                    ################ before ##################
                    for k in range(4):
                        for l in range(1, dist + 1):
                            nr = i + row2[k] * l
                            nc = j + col2[k] * l
                            if not (0 <= nr < n and 0 <= nc < n):
                                break
                            kill_cnt += grid[nr][nc]
                            ele_kill.append((nr, nc))
                            if grid[nr][nc] <= 0:  # 검증 필요 0인곳 제초제 뿌리는지 확인 필요
                                break

                    ################ after ##################
                    for k in range(4):
                        for l in range(1, dist + 1):
                            nr = i + row2[k] * l
                            nc = j + col2[k] * l
                            if not (0 <= nr < n and 0 <= nc < n): # 범위 벗어나면 바로 끝
                                break
                            if grid[nr][nc] != -1: # 벽이 아니면 좌표, 죽인 갯수 누적
                                kill_cnt += grid[nr][nc]
                                ele_kill.append((nr, nc))
                            if grid[nr][nc] <= 0:  # 0이면 위에서 연산은 되게하고 여기서 진짜 끝!
                                break

        40~48   : 검증 시작(8)
                    유레카!
                    살아있는 나무가 없어서 제초가 불가능할때 인덱스 에러 발견!
                    if kill_lst: 조건 추가해줌!
                    5 2 2 1
                    -1 -1 -1 -1 -1
                    -1 -1 -1 -1 -1
                    -1 -1 -1 -1 -1
                    -1 -1 -1 -1 -1
                    -1 -1 -1 -1 5


  메모리 24 KB
  시간 306 ms


    회고
        1. 오전 꼬리 잡기 문제에서 많이 틀렸어서,,, 오후 문제는 원큐에 성공하고자 검증을 확실히 했다!!
            덕분에 오류 잡아냄!!! 앞으로도 엣지케이스나 의심되는 부분 바로바로 기록하고 검증하자!!!!

        2. 역시 함수를 먼저 만들면 코드 짜기가 편해짐..... 함수화를 놓치지마!!!

        3. 문제는 좀 더 꼼꼼히 읽었으면 좋겠다...^^
            "단 전파되는 도중 벽이 있거나 나무가 아예 없는 칸이 있는 경우, 그 칸 까지는 제초제가 뿌려지며 그 이후의 칸으로는 제초제가 전파되지 않습니다."
            이 부분 놓친게 아쉽넹..


# 문제 풀면서의 기록
실제 시험이라고 생각하자.
문제 설명
    1. 인접한 4개 칸 중 나무가 있는 칸 수만큼 나무 성장
    2. 인접한 4개 칸 중 벽/다른나무/제초제 모두 없는 칸에 번식
        칸 갯수 // 만큼
    3. 제초제 뿌림
        4개 대각선으로 k만큼 전파 쭉쭊쭉 -> 멈추는 로직 필요
        우선순위
        (1) 가장 많은 나무
        (2) 행 열 작은 순
        -> 주의!! 나무가 없는칸에선 계산하면 안됨!!!
        제초제는 c년 만큼 남아있다가 c+1년 후에 사라짐.
입력
    맵 n, 박멸이 진행되는 년 수 m, 제초제 확산범위 k, 제초제 남아있는 년수 c
    벽 -1
출력
    총 박멸한 나무 그루 수
구상
필요한 함수
    1. grow()
    2. spread()
    3. kill()
필요한 변수
    제초제는 따로 2차원 배열로 관리.

테케
전부 박멸되는 경우

5 2 2 1
-1 -1 -1 -1 -1
-1 -1 -1 -1 -1
-1 -1 -1 -1 -1
-1 -1 -1 -1 -1
-1 -1 -1 -1 5


년수 잘 되는지
5 5 2 5
0 0 0 0 0
0 30 23 0 0
0 0 -1 0 0
0 0 17 46 77
0 0 0 12 0

제초제 잘 되는지 검증
5 1 2 1
0 0 0 0 0
0 9 0 9 0
0 0 9 0 0
0 9 0 9 0
-1 0 0 0 0
'''


def grow():  # 제초제 당한애들은 이미 grid가 0임
    plus_grid = [[0] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0:
                rnd = 0
                for k in range(4):
                    nr = i + row[k]
                    nc = j + col[k]
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 0:
                        rnd += 1
                plus_grid[i][j] = rnd

    for i in range(n):
        for j in range(n):
            grid[i][j] += plus_grid[i][j]


def spread():
    plus_grid = [[0] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0:
                empty = 0
                for k in range(4):
                    nr = i + row[k]
                    nc = j + col[k]
                    if 0 <= nr < n and 0 <= nc < n and \
                            grid[nr][nc] == 0 and kill_grid[nr][nc] == 0:
                        empty += 1
                if empty:
                    growth = grid[i][j] // empty
                    for k in range(4):
                        nr = i + row[k]
                        nc = j + col[k]
                        if 0 <= nr < n and 0 <= nc < n and \
                                grid[nr][nc] == 0 and kill_grid[nr][nc] == 0:
                            plus_grid[nr][nc] += growth

    for i in range(n):
        for j in range(n):
            grid[i][j] += plus_grid[i][j]


def kill():
    global ans
    kill_lst = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0:  # 이 조건 의심 필요
                kill_cnt = grid[i][j]
                ele_kill = [(i, j)]
                for k in range(4):
                    for l in range(1, dist + 1):
                        nr = i + row2[k] * l
                        nc = j + col2[k] * l
                        if not (0 <= nr < n and 0 <= nc < n):
                            break
                        if grid[nr][nc] != -1:
                            kill_cnt += grid[nr][nc]
                            ele_kill.append((nr, nc))
                        if grid[nr][nc] <= 0:  # 검증 필요 0인곳 제초제 뿌리는지 확인 필요
                            break
                kill_lst.append((-kill_cnt, (i, j), ele_kill))
    if kill_lst:
        kill_lst.sort()
        kill_cnt, (r, c), location = kill_lst[0]
        ans += abs(kill_cnt)

        for r, c in location:
            kill_grid[r][c] = spray + 1
            grid[r][c] = 0


n, total_time, dist, spray = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
ans = 0
kill_grid = [[0] * n for i in range(n)]

row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]

row2 = [-1, -1, 1, 1]
col2 = [-1, 1, -1, 1]

ans = 0
for time in range(total_time):
    grow()
    spread()
    kill()
    # 1씩 감소
    for i in range(n):
        for j in range(n):
            if kill_grid[i][j]:
                kill_grid[i][j] -= 1
print(ans)
