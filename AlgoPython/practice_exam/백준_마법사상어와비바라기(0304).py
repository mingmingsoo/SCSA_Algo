'''
# 코드트리 나무 타이쿤
2025.04.03.목
두번째 풀이 (특이사항: 백준은 시간초과나서 lst에서 set으로 코드 바꿈)

# 문제 풀고 나서 기록
    제출 횟수 1회
    문제 시작 20:50
    문제 종료 21:08
    총 풀이시간 18분
        50~59 : 문제 이해 및 초기 주석(9)
        59~08 : 로직 작성(9)

  메모리 18 MB
  시간 100 ms
  
  회고
  백준은 구름? 이라 문제 이해가 쉬웠던 것 같은데 오히려 코드트리 설명이 쩸 어려웠음
  백준 제출시 시간초과라 SET으로 변경했는데 백준에 내보길 잘했다..
    not in new_nu: 조회연산 때문인듯

왤케 어후 설명이 어려워
문제 설명
    - 초기: 영양제 왼,아래에 4개 -> set
    for 년수
        1. 영양제 이동 (도넛)
        2. 영양제 해당되는 애들 대각선 4방에 1 이상인 갯수만큼 성장(도넛X) -> new_grid 필요
        3. 기존 set 제외하고 맵에서 2 이상인 애들 -2 하고 영양제 new_set 에 담아줌
            set = new_set
입력
    맵 크기 n 총 년수 time
    맵 정보
    이동 규칙 d, l (방향 길이)
출력
    그리드 합
'''

n, time = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
nutrition = set([(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)])

row = [0, -1, -1, -1, 0, 1, 1, 1]
col = [-1, -1, 0, 1, 1, 1, 0, -1]

for t in range(time):
    d, l = map(int, input().split())
    d -= 1
    new_nu = set()
    for r, c in nutrition:
        nr = (r + row[d] * l) % n
        nc = (c + col[d] * l) % n
        grid[nr][nc] += 1
        new_nu.add((nr, nc))
    plus_grid = [[0] * n for i in range(n)]

    for r, c in new_nu:
        cnt = 0
        for k in (1, 3, 5, 7):
            nr = r + row[k]
            nc = c + col[k]
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc]:
                cnt += 1
        plus_grid[r][c] += cnt

    for i in range(n):
        for j in range(n):
            if plus_grid[i][j]:
                grid[i][j] += plus_grid[i][j]

    new_nutrition = set()
    for i in range(n):
        for j in range(n):
            if grid[i][j] >= 2 and (i, j) not in new_nu:
                grid[i][j] -= 2
                new_nutrition.add((i, j))

    nutrition = new_nutrition

print(sum(map(sum, grid)))

'''
# 백준 21610 마법사 상어와 비바라기 (코드트리 나무 타이쿤)

# 문제 풀고 나서 기록

    문제 시작 15:50
    문제 종료 16:13
    총 풀이시간 23분
        0~8분    : 문제 이해 ~ 문제 구상 및 초기 주석(8)
                    ㅠㅠ 녹화 버튼을 늦게 누름 ㅠㅠ
        8~23분   : 문제 조건에 맞춰서 순서대로 그대로 설계.(15)
                    이상없이 테케 돌아가서 디버깅 안하고 제출

    메모리 112360 KB
    시간 168 ms

    회고
    1.
    이번엔 나는 2차원 배열로 풀었는데 다른 친구들은 또 1차원 배열로 풀었네
    아까 상어 파이어볼 문제는 그 반대였는데 요상하네...................
    -> 2차원 배열로 풀어도 n*n*m(max 50*50*100 = 50000) 이여서 괜찮다!
    시간 차이는 없다만 나도 1차원 배열로 풀어보기!!!!

    2.
    디버깅 없이 한번에 푼 문제......!!!!!!!! 잘했다 !!!!!!!!!!!!!!!!!!!ㅠㅠㅠㅠㅠ
    (녹화버튼 늦게 누른건 잘못)
    (1잘못 1잘함 하나씩 있는지 휴ㅠ)

    3. 상어 초등학교에서 범위 넘어가는 거 확인했어서 요번 문제에서는 쉽게 캐치할 수 있었다.

문제설명
    1. 범위는 넘어간다.
    2. 처음 시작시  (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름
    3. 일단 구름은
        ㄱ. 방향과 속력만큼 이동
        ㄴ. 구름안에 있는 애들은 1 증가
        ㄷ. 구름 사라짐
        ㄹ. 물복사 버그 대각선에 물이면 그 칸만큼 증가.
    4. 2이상인 애들 모든 칸에 구름이 생기고 2씩 줄어듬.
        (아까 구름이였던 애들 말고.)

필요한 변수
    iscloud
    복사배열들 필요함.
'''
n, move_num = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

move_list = [list(map(int, input().split())) for i in range(move_num)]

row = [0, -1, -1, -1, 0, 1, 1, 1]
col = [-1, -1, 0, 1, 1, 1, 0, -1]

row2 = [1, 1, -1, -1]
col2 = [1, -1, 1, -1]

# 초기 구름 설정
is_cloud = [[False] * n for i in range(n)]
is_cloud[n - 1][0], is_cloud[n - 1][1], is_cloud[n - 2][0], is_cloud[n - 2][1] = True, True, True, True

for d, s in move_list:
    d -= 1

    # 모든 구름이 di 방향으로 si칸 이동한다.
    is_new_cloud = [[False] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if is_cloud[i][j]:
                nr = (i + row[d] * s) % n
                nc = (j + col[d] * s) % n
                is_new_cloud[nr][nc] = True

    # 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
    for i in range(n):
        for j in range(n):
            if is_new_cloud[i][j]:
                grid[i][j] += 1

    # 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다
    is_bug = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if is_new_cloud[i][j]:
                round_water = 0
                for k in range(4):
                    nr = i + row2[k]
                    nc = j + col2[k]
                    if not (0 <= nr < n and 0 <= nc < n):
                        continue
                    if grid[nr][nc] > 0:
                        is_bug[i][j] += 1

    for i in range(n):
        for j in range(n):
            if is_bug[i][j] > 0:
                grid[i][j] += is_bug[i][j]

    # 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다.
    is_cloud = [[False] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] >= 2 and not is_new_cloud[i][j]:
                is_cloud[i][j] = True
                grid[i][j] -= 2

ans = 0
for i in range(n):
    for j in range(n):
        ans += grid[i][j]

print(ans)
