T = int(input())


def make_q():
    for i in range(N):
        for j in range(N):
            if grid[i][j] and grid[i][j] != -1:
                if grid[i][j][0] > 0:
                    grid[i][j][0] -= 1
                elif grid[i][j][0] == 0:
                    q.append((i, j, grid[i][j][2]))
                    grid[i][j][1] += 1


def myprint():
    print("-------------------")
    for i in range(N):
        for j in range(N):
            if grid[i][j] and grid[i][j] != -1:
                print(grid[i][j][2], end=" ")
            elif grid[i][j] == -1:
                print("X", end=" ")
            else:
                print(0, end=" ")
        print()


for tc in range(T):
    '''
    문제 설명
        t초후 줄기세포 갯수
    입력
        n,m, 시간 time
    구상
        맵 800*800 늘리기
        그리고 400,400에 위치시키기
    '''
    from collections import deque

    n, m, time = map(int, input().split())
    tmp = [list(map(int, input().split())) for i in range(n)]
    for i in range(n):
        for j in range(m):
            if tmp[i][j]:
                tmp[i][j] = [tmp[i][j], 0, tmp[i][j]]  # 0 번째가 0이되면 활성화 1번째가 2번째가 되면 쥬금
    N = 700
    # N = 20
    grid = [[0] * N for i in range(N)]

    for i in range(n):
        for j in range(m):
            if tmp[i][j]:
                grid[i + N // 2][j + N // 2] = tmp[i][j]
    # for _ in grid:
    #     print(_)
    row = [-1, 1, 0, 0]
    col = [0, 0, 1, -1]

    for t in range(time):

        q = deque()
        # 1. 1 이상인 애들 0 빼주기, 0인 애들은 q 에 넣어주기
        make_q()

        # print(q)
        # 2. q 인애들 bfs 돌려서 확산하기
        die_set = set()
        while q:
            r, c, power = q.popleft()
            if grid[r][c][1] == grid[r][c][2]:
                die_set.add((r, c))
            for k in range(4):
                nr = r + row[k]
                nc = c + col[k]
                if not (0 <= nr < N and 0 <= nc < N) or grid[nr][nc] == -1:
                    continue
                if grid[nr][nc] == 0:
                    grid[nr][nc] = [power, 0, power]
                elif grid[nr][nc][0] == grid[nr][nc][2] and grid[nr][nc][2] < power:  # 내가 더 클때만 가능
                    grid[nr][nc] = [power, 0, power]

        # # 1. 죽은 애들 검사 -> 1번째 2번째 같은 애들 -1로 바꿔주기
        for r, c in die_set:
            grid[r][c] = -1
        # myprint()
    ans = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] != 0 and grid[i][j] != -1:
                ans += 1

    print(f"#{tc + 1} {ans}")
