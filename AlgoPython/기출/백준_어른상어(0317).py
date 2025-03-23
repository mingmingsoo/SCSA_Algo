'''
# 백준 19237 어른상어
# 체감난이도 골1 (문제 이해가 어려웠음...)

# 문제 풀고 나서 기록

    문제 시작 14:00
    문제 종료 14:59
    총 풀이시간 59분
        00~17   : 문제 이해, 초기 주석, 문제 구상(17) - 중간에 화장실 3분
                  문제 이해가 잘 안돼서 문제 설명을 옮겨적으면서 재차 이해하려고 했음
                  문제 예시 줄거면 다주지 답은 14초인데 왜 4초까지만 보여주냐ㅠ
        17~21   : 탑다운 설계(4)
                  처음엔 shark_move, shark_delete 함수로 설계
        21~48   : shark_move 1차 설계(27)
                  1. 메서드 단위로 빼고 싶었는데 어려워서 일단 의식의 흐름대로 작성..
                  2. empty(영역이 없는 곳)로 우선순위대로 이동하는지 확인
                  3. empty가 없으면 내 영역들 중 우선순위 이동하는 로직 작성
                  4. shark_delete로 뺀거를 shark_move 마지막에서 처리하는 걸로 수정
                     편의상 3차원 배열로 상어 번호들을 append, sort 해주고 앞에있는 애들만 남기려고 했는데
                     grid 자체가 2차원 배열이여서 오류나서 대교비소로 바꾸는 걸로 수정
                  5. 1번 테케가 19 나오는 거 확인 왜 14인지 분석
        48~55   : 보니까 empty 없으면 내 영역으로 가는 건데(7)
                  나는 바로 전 영역으로 가게끔 설계 해놨었음
                  근데 내 영역으로 갈때도 limit이 몇이던지 간에 우선순위대로 가는거여서
                  shark_area[nr][nc][1] == limit -1 조건을 없애줌
        48~55   : 1번테케 14 나오는거 확인
                  근데 2번 테케가 무한루프돔!!
                  -> 입력 받을 때for i in range(4): 여서
                     for i in range(shark_num): 으로 수정!! 상어 갯수만큼 입력받는 것.
                     정답 나오는 거 확인
        55~59   : 시간 도는 로직 수정, 최솟값일 때 잘 나오는지 확인(4)
                  while True -> for t in range(1, 1001): 1000초 까지 가능!!!

    메모리 112548 KB
    시간 176 ms

    회고
        1. 문제 이해가 어려워서 설계가 잘 안됐음..
           오늘은 운이 좋아서 잘 풀린 것 같지만... 설계를 잘하자........ 명심 명심 !!
        2. 잘한 점은 코드를 와라라락 쓰지 않고 이동하는지, 냄새 잘 풍기는지(?) 확인하면서 해서 로직이 꼬이지 않았다.

# 문제 풀면서의 기록
문제가 잘 이해 안된다.ㅇ....
문제 설명
    1. 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다.
    2. 상어가 이동한다-> 냄새는 k번 이동하면 사라짐
    3. 이동 방향
        1. 인접한 칸 중 아무냄새 없는 칸
        2. 그런 칸이 없으면 자신의 냄새가 있는 칸
        3. 우선순위는 상어마다 다르고 현재 상어가 보고있는 방향에 따라 다름
        ㅇㅋㅇㅋ....
구상
    1. 상어 이동
    2. 상어 냄새표시
    3. 상어 삭제
    냄새표시는 따로 해줘야할 것 같고(상어번호와 k)
2 2 1
0 1
2 0
1 2
4 4 3 1
2 3 1 4
4 1 2 3
3 4 2 1
4 3 1 2
2 4 3 1
2 1 3 4
3 4 1 2
'''
n, shark_num, limit = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
shark_first_d_list = list(map(lambda x: int(x) - 1, input().split()))
shark_d = []
for i in range(shark_num):
    tmp = [list(map(lambda x: int(x) - 1, input().split())) for i in range(4)]
    shark_d.append(tmp)
shark_area = [[[] for i in range(n)] for i in range(n)]  # limit과 상어 번호를 남겨줌
ans = -1
row = [-1, 1, 0, 0]
col = [0, 0, -1, 1]


def shark_move():
    global grid
    new_grid = [[0] * n for i in range(n)]

    # 일단 영역표시
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0:
                shark_area[i][j] = [grid[i][j], limit]

    # 그 다음에 움직임
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0:
                # 빈 곳 중에 우선순위...
                shark_dir = shark_d[grid[i][j] - 1][shark_first_d_list[grid[i][j] - 1]]
                empty = False
                next_r, next_c, next_d = i, j, shark_first_d_list[grid[i][j] - 1]
                for k in shark_dir:
                    nr = i + row[k]
                    nc = j + col[k]
                    if not (0 <= nr < n and 0 <= nc < n):
                        continue
                    if not shark_area[nr][nc]:
                        empty = True
                        next_r, next_c, next_d = nr, nc, k
                        break
                if not empty:
                    # 내가 온 곳 중에서...
                    for k in shark_dir:
                        nr = i + row[k]
                        nc = j + col[k]
                        if not (0 <= nr < n and 0 <= nc < n):
                            continue
                        if shark_area[nr][nc] and shark_area[nr][nc][0] == grid[i][j]:
                            next_r, next_c, next_d = nr, nc, k
                            break
                if new_grid[next_r][next_c] == 0:
                    new_grid[next_r][next_c] = grid[i][j]
                else:
                    if grid[i][j] < new_grid[next_r][next_c]:
                        new_grid[next_r][next_c] = grid[i][j]
                shark_first_d_list[grid[i][j] - 1] = next_d
    # 이제.. 시간이 지난 애들 표시
    for i in range(n):
        for j in range(n):
            if shark_area[i][j]:
                shark_area[i][j][1] -= 1
                if shark_area[i][j][1] == 0:
                    shark_area[i][j] = []
    grid = new_grid


for t in range(1, 1001):
    # print(ans)
    shark_move()
    cnt = 0
    # print("-----------상어-------------")
    # for _ in grid:
    #     print(*_)
    # print("-----------냄새-------------")
    # for _ in shark_area:
    #     print(*_)
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0:
                cnt += 1
    if cnt == 1:
        ans = t
        break
print(ans)
########################################################
# 두번째 코드 : 변수 직관화
n, shark_num, limit = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
shark_d_list = list(map(lambda x: int(x) - 1, input().split()))
shark_pd = []  # shark_priority_d
for _ in range(shark_num):
    shark_pd.append([tuple(map(lambda x: int(x) - 1, input().split())) for i in range(4)])
shark_area = [[[] for _ in range(n)] for _ in range(n)]  # limit과 상어 번호를 남겨줌 limit은 계속 감소하기에 tuple을 사용하지 않음
ans = -1
row = [-1, 1, 0, 0]
col = [0, 0, -1, 1]

def shark_move():
    global grid

    # [1] 영역표시
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0:
                shark_area[i][j] = [grid[i][j], limit]  # 상어 번호와 시간

    # [2] 움직임
    new_grid = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0:
                # 빈 곳 중에 우선순위...
                shark_dir = shark_pd[grid[i][j] - 1][shark_d_list[grid[i][j] - 1]]  # shark_pd[상어번호][상어방향]
                empty = False
                next_r, next_c, next_d = i, j, shark_d_list[grid[i][j] - 1]  # 이동할 위치와 바뀔 방향
                for k in shark_dir:
                    nr = i + row[k]
                    nc = j + col[k]
                    if not (0 <= nr < n and 0 <= nc < n):
                        continue
                    if not shark_area[nr][nc]:  # 빈 영역이면 갈 수 있다.
                        empty = True
                        next_r, next_c, next_d = nr, nc, k
                        break
                if not empty:  # 빈 영역이 없으면 내 영역들 중 가야한다.
                    for k in shark_dir:
                        nr = i + row[k]
                        nc = j + col[k]
                        if not (0 <= nr < n and 0 <= nc < n):
                            continue
                        if shark_area[nr][nc] and shark_area[nr][nc][0] == grid[i][j]:  # 내 영역이면 간다.
                            next_r, next_c, next_d = nr, nc, k
                            break
                # [2-1] 좌표 이동
                if new_grid[next_r][next_c] == 0:  # 빈 곳이면 그냥 가는데
                    new_grid[next_r][next_c] = grid[i][j]
                else:  # 다른 상어가 있으면 상어 번호 비교
                    if grid[i][j] < new_grid[next_r][next_c]:
                        new_grid[next_r][next_c] = grid[i][j]
                # [2-1] 방향 전환
                shark_d_list[grid[i][j] - 1] = next_d

    # 이제.. 시간이 지난 애들 표시
    for i in range(n):
        for j in range(n):
            if shark_area[i][j]:
                shark_area[i][j][1] -= 1  # 시간 빼주고
                if shark_area[i][j][1] == 0:  # 0초로 도달했으면
                    shark_area[i][j] = []  # 빈 영역으로 만들어줌
    grid = new_grid


def is_end():
    cnt = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0:
                cnt += 1
    if cnt == 1:  # 하나만 남았나?
        return True
    return False


# main
for t in range(1, 1001):
    shark_move()  # 상어 이동
    if is_end():
        ans = t
        break
print(ans)

