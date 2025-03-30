'''
# 백준 23291 어항정리
# 체감난이도 플5

# 문제 풀고 나서 기록

    문제 시작 09:00
    문제 종료 11:08
    총 풀이시간 128분
        00~16   : 문제 이해, 초기주석 및 문제 구상(16)
        16~03   : [1차 어항 쌓기 로직 구현](47)
                    N*N 2차원 배열로 구현.......
                    이 생각밖에 안드는 내가 밉지만 어떡해 해야지....
        03~16   : [1차 물고기 수 조절 로직 구현](13)
        16~21   : [1차 펼치는 로직 구현](5)
        21~30   : [2차 어항 쌓기 로직 구현](9)
                    여기서 문제가 생길 예정
                    N 크기에 따라 배열의 크기가 다른데 무조건 2*4 라고 생각하고 짰음
        30~32   : [2차 물고기 수 조절 로직 구현](2)
        32~35   : [2차 펼치는 로직 구현](3)
        35~37   : [검사 로직 구현](2)
        37~06   : N이 8일때는 답이 나오지만(29)
                    2차 어항쌓기 로직이 N이 8일때만 해당되는거라...
                    싹 지우고 2차 로직 작성..
                    느므느므 힘들었어요........ 인덱스와의 싸움........ㅠㅠㅠㅠ
        06~08   : 오픈테케 답 나오는 거 확인(2)
                    답이 0이 될 수도 있지 않나? 싶어서
                    입력 받고 검사 해주는 로직 추가
                    (답이 0인경우는 없음)


  메모리 113260 KB
  시간 200 ms


    회고
        1. 파이썬 기능을 전혀 활용하지못한 바보같은 코드
        2. 드래곤 커브때의 아픈 기억이 올라왔다......................
            그래도 잘한점은 해냈다는거......이렇게 다시 풀래면 못푼다 ㅠ
        3. 또 고생고생 하면서 풀었다 아오 ... 이건 꼭 남의 코드 이해하고 교수님 영상 보기


# 문제 풀면서의 기록
감도 안오네 이거는 -> 방법 생각하고 들어가기
규칙이 있을까 하는데 없는 것 같음
문제 설명
    1. 가장 작은 값을 가지는 애들한테 +1 씩 해주기
    2. 1차 어항 쌓기
    3. 물고기 수 조절하기
    4. 다시 펼치기
    5. 2차 어항 쌓기
    6. 물고기 수 조절하기
    7. 다시 펼치기
    8. 검증하기
'''


def rotation():
    sn, sm = len(small_grid), len(small_grid[0])
    # 회전...
    small = [[0] * sn for i in range(sm)]

    for i in range(sm):
        for j in range(sn):
            small[i][j] = small_grid[sn - j - 1][i]

    return small


n, limit = map(int, input().split())
grid = [[0] * n for i in range(n)]
ans = 0
tmp = list(map(int, input().split()))
for j in range(n):
    grid[n - 1][j] = tmp[j]

maxi, mini = 0, int(1e9)
for i in range(n):
    for j in range(n):
        if grid[i][j] > 0:
            maxi = max(maxi, grid[i][j])
            mini = min(mini, grid[i][j])

while True:
    mini = min(grid[n - 1])

    # 1. 가장 작은 값을 가지는 애들한테 +1 씩 해주기
    for j in range(n):
        if grid[n - 1][j] == mini:
            grid[n - 1][j] += 1

    # 2. 1차 어항 쌓기
    # 1. 일단 한개
    grid[n - 1][0], grid[n - 2][1] = grid[n - 2][1], grid[n - 1][0]

    cnt = 0

    while True:
        cnt += 1
        sr, sc, er, ec = n, n, -1, -1
        for i in range(n - 1):
            for j in range(n):
                if grid[i][j] != 0:
                    sr = min(sr, i)
                    sc = min(sc, j)
                    er = max(er, i)
                    ec = max(ec, j)

        small_grid = [[0] * (ec - sc + 1) for i in range(er - sr + 2)]
        for i in range(sr, er + 2):
            for j in range(sc, ec + 1):
                small_grid[i - sr][j - sc] = grid[i][j]
        small_ro = rotation()

        if len(small_ro[0]) + ec >= n:
            break
        for i in range(sr, er + 2):
            for j in range(sc, ec + 1):
                grid[i][j] = 0

        start_jdx = ec + 1
        for i in range(n - len(small_ro) - 1, n - 1):
            for j in range(start_jdx, start_jdx + len(small_ro[0])):
                grid[i][j] = small_ro[i - n + len(small_ro) + 1][j - start_jdx]

    # 3. 물고기 수 조절하기
    row = [-1, 1, 0, 0]
    col = [0, 0, 1, -1]
    plus_grid = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0:
                for k in range(4):
                    nr = i + row[k]
                    nc = j + col[k]
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 0 and grid[i][j] > grid[nr][nc]:
                        minus = grid[i][j] - grid[nr][nc]
                        diff = minus // 5
                        if diff > 0:
                            plus_grid[i][j] -= diff
                            plus_grid[nr][nc] += diff

    for i in range(n):
        for j in range(n):
            grid[i][j] += plus_grid[i][j]

    # 4. 다시 펼치기

    new_grid = [0] * n
    jdx = 0
    for j in range(n):
        for i in range(n - 1, -1, -1):
            if grid[i][j] != 0:
                new_grid[jdx] = grid[i][j]
                jdx += 1
    # 5. 2차 어항 쌓기
    sero_grid = [[0] * (n // 2) for i in range(2)]
    for j in range(n // 2):
        sero_grid[1][j] = new_grid[j + n // 2]
        sero_grid[0][j] = new_grid[n // 2 - j - 1]

    half = [[0] * (n // 4) for i in range(2)]
    for i in range(2):
        for j in range(n // 4):
            half[i][j] = sero_grid[i][j]

    half_copy = [_[:] for _ in half]
    namuji_half = [[0] * (n // 4) for i in range(2)]

    for i in range(2):
        for j in range(n // 4):
            namuji_half[i][j] = sero_grid[i][j + n // 4]

    for i in range(2):
        for j in range(n // 4):
            half[i][j] = half_copy[2 - i - 1][n // 4 - j - 1]

    sero_ro = half + namuji_half

    # 6. 물고기 수 조절하기
    plus_grid = [[0] * len(sero_ro[0]) for i in range(len(sero_ro))]

    for i in range(len(sero_ro)):
        for j in range(len(sero_ro[0])):
            if sero_ro[i][j] > 0:
                for k in range(4):
                    nr = i + row[k]
                    nc = j + col[k]
                    if 0 <= nr < len(sero_ro) and 0 <= nc < len(sero_ro[0]) and sero_ro[nr][nc] > 0 and sero_ro[i][j] > \
                            sero_ro[nr][nc]:
                        minus = sero_ro[i][j] - sero_ro[nr][nc]
                        diff = minus // 5
                        if diff > 0:
                            plus_grid[i][j] -= diff
                            plus_grid[nr][nc] += diff

    for i in range(len(sero_ro)):
        for j in range(len(sero_ro[0])):
            sero_ro[i][j] += plus_grid[i][j]

    # 7. 다시 펼치기
    grid = [[0] * n for i in range(n)]
    jdx = 0
    for j in range(len(sero_ro[0])):
        for i in range(len(sero_ro) - 1, -1, -1):
            grid[n - 1][jdx] = sero_ro[i][j]
            jdx += 1
    # 8. 검증하기
    maxi, mini = 0, int(1e9)
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0:
                maxi = max(maxi, grid[i][j])
                mini = min(mini, grid[i][j])

    ans += 1
    if maxi - mini <= limit:
        break
print(ans)
