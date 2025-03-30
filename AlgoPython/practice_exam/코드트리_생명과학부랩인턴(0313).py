'''
# 19238 백준 스타트 택시
# 체감난이도 골2

# 문제 풀고 나서 기록

    문제 시작 14:00
    1차 제출 14:44
    문제 종료 14:55
    총 풀이시간 55분
        00~06   : 문제 이해(4)
        04~10   : 문제 구상 및 초기 주석(6)
        10~14   : 입력 받기(4)
                    원래 1인곳 -1 처리,
                    시작위치(2차원 배열), 목적지(딕셔너리) 각각 다르게 기록
        14~16   : 탑다운 설계(2)
        16~26   : 손님 데러러 가는 로직 설계(10)
                    2번 손님 잘 태우는지 확인
        26~30   : 손님 데려다 주는 로직 설계(4)
        30~38   : 1번 테케 14가 아닌 15가 나와서 디버깅 시작(8)
                    (1) 손님 태우고 맵에 0으로 안바꿔줘서 계속 2번 손님만 태우는 거 확인
                        grid[r][c] = 0 수정 완료
                    (2) 1번 손님 아닌 3번 먼저 태워서 힙큐를 while 문 밖으로 위치시켜서 수정
        38~40   : 3번 테케 인덱스 에러나서 확인(2)
                    손님을 못데리러 갈 경우 next_r, next_c이 -1,-1 이여서 오류가났음!
                    -> 손님을 못태울 경우, 손님을 못데려다줄 경우 실패하는 로직으로 수정
                    (end 플래그 사용)
        40~44   : 택시 시작위치가 손님이 있는 곳일 때 반례가 생각나서 반례 만들어봄(4)
                    visited[r][c] = True 만 주석처리 하면 된다고 생각했음
                    그리고 1차 제출 -> 틀렸습니다
        44~55   : 만든 반례에서 답이 19인데 17 나온 거확인(11)
                   visited[r][c] = True 를 해버리면 dist가 무조건 2가 되기에 생기는 오류 확인
                   로직 수정!

    메모리 115720 KB
    시간 216 ms

    회고
        1. 아 반례까지 만들어놓고 -1 안나온다고 내버린거 바보같음.. 계산은 해봤어야지 이사람아
        2. 시간 줄이는 거 고려해보기

# 문제 풀면서의 기록
문제설명
    승용이가 0~ C-1 까지 가는데 채취한 곰팡이 총 합
구상
    1. 승용이 움직임
    2. 승용이 채취함
    3. 이동함
    4. 합쳐짐
    속도는 2(크기 -1) 로 나눠줌
    와리가리는 2(크기-1)임
5 6 1
3 3 999 4 1

5 6 1
3 3 998 4 1

'''
#################################################################
# 두번째 풀이 : 시간은 기나 더 간단함
n, m, virus_num = map(int, input().split())  # 맵 크기와 곰팡이 수
grid = [[() for i in range(m)] for i in range(n)]
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]
for v in range(virus_num):
    r, c, s, d, b = map(int, input().split())  # 위치, 속력, 방향, 크기
    if d in (1,2):
        grid[r - 1][c - 1] = (b, d - 1,s % (2 * (n - 1)))  # 크기, 방향, 속력 순으로 넣는다
    else:
        grid[r - 1][c - 1] = (b, d - 1, s % (2 * (m - 1)))
move = {0: 1, 1: 0, 2: 3, 3: 2}
jdx = eat = 0
while jdx < m:  # 승용이 움직임
    for i in range(n):
        if grid[i][jdx]:  # 곰팡이 있으면
            eat += grid[i][jdx][0]  # 크기만큼 먹는다
            grid[i][jdx] = ()  # 비었다!
            break
    # 2. 움직인다.
    move_list = []
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                virus = grid[i][j]
                b, d, s = virus[0], virus[1], virus[2]  # 크기, 방향, 속력
                grid[i][j] = ()
                r, c = i, j
                for ss in range(s):
                    nr = r + row[d]
                    nc = c + col[d]
                    if not (0 <= nr < n and 0 <= nc < m):
                        d = move[d]
                        nr = r + row[d]
                        nc = c + col[d]
                    r = nr
                    c = nc
                move_list.append((r, c, b, d, s))
    for r, c, b, d, s in move_list:
        if not grid[r][c]:
            grid[r][c] = (b, d, s)
        else:
            if b > grid[r][c][0]:
                grid[r][c] = (b, d, s)
    jdx += 1  # 다음 칸 탐색
print(eat)
#################################################################
# 첫 풀이

n, m, virus_num = map(int, input().split())  # 맵 크기와 곰팡이 수
grid = [[[] for i in range(m)] for i in range(n)]
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]
for v in range(virus_num):
    r, c, s, d, b = map(int, input().split())  # 위치, 속력, 방향, 크기
    if d in (1, 2):  # 위 아래
        grid[r - 1][c - 1].append((b, d - 1, s % (2 * (n - 1))))  # 크기, 방향, 속력 순으로 넣는다
    else:
        grid[r - 1][c - 1].append((b, d - 1, s % (2 * (m - 1))))

move = {0: 1, 1: 0, 2: 3, 3: 2}
jdx = 0
eat = 0
while jdx < m:  # 승용이 움직임
    # 1. 누구 먹을래
    for i in range(n):
        if grid[i][jdx]:  # 곰팡이 있으면
            eat += grid[i][jdx][0][0]  # 크기만큼 먹는다
            grid[i][jdx] = []  # 비었다!
            break
    # 2. 움직인다.
    new_grid = [[[] for i in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                for w in range(len(grid[i][j]) - 1, -1, -1):
                    virus = grid[i][j][w]
                    b, d, s = virus[0], virus[1], virus[2]  # 크기, 방향, 속력
                    nr = i + row[d] * s
                    nc = j + col[d] * s
                    if d in (0, 1):
                        size = 2 * (n - 1)
                        nr = (nr + size) % size
                        if nr >= n:
                            nr = size - nr
                            d = move[d]
                    elif d in (2, 3):
                        size = 2 * (m - 1)
                        nc = (nc + size) % size
                        if nc >= m:
                            nc = size - nc
                            d = move[d]
                    new_grid[nr][nc].append((b, d, s))
                    # grid[i][j].pop(w)
    # 3-0. sort 하고
    for i in range(n):
        for j in range(m):
            if new_grid[i][j]:
                new_grid[i][j].sort(reverse=True)
    # 3-1. 겹치는 애들 검사
    for i in range(n):
        for j in range(m):
            if len(new_grid[i][j]) >= 2:
                new_grid[i][j] = [new_grid[i][j][0]]
    grid = new_grid
    jdx += 1  # 다음 칸 탐색

print(eat)
