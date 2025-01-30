T = int(input())
for tc in range(T):
    '''
    1. 0인 곳에서 4가지 방향으로 모든 점수 계산
    2. 웜홀의 정보를 담는 배열 필요
    '''
    n = int(input())

    grid = [list(map(int, input().split())) for i in range(n)]
    ans = 0

    # 웜홀 정보를 담는 배열
    holls = [[] for i in range(5)]

    for i in range(n):
        for j in range(n):
            if (grid[i][j] >= 6):
                holls[grid[i][j] - 6].append([i, j])
    # for row in holls:
    #     print(row)

    row = [-1, 0, 1, 0]
    col = [0, -1, 0, 1]


    def startGame(r, c, d):
        ping = 0
        originR = r
        originC = c

        # 지금 위치가 벽인가 +1
        # 이동하는 곳이 1~5이면 +1

        while True:
            nextR = r + row[d]
            nextC = c + col[d]

            # 벽 검사
            if (nextR < 0 or nextR >= n or nextC < 0 or nextC >= n):
                # 벽에 부닥쳤음
                ping += 1
                # 위치는 원상복귀, 점수 획득, 위치는 반대
                nextR = r
                nextC = c

                d = (d + 2) % 4

            # 블록 검사
            if (1 <= grid[nextR][nextC] <= 5):
                ping += 1
                if (d == 0):
                    # 0(상)일때 2를 만나면 3이 되고 3을 만나면 1이됨
                    if (grid[nextR][nextC] == 2):
                        d = 3
                    elif (grid[nextR][nextC] == 3):
                        d = 1
                    else:  # 나머지는 방향 180도 전환
                        d = (d + 2) % 4
                elif (d == 1):
                    # 1(좌)일때 1를 만나면 0이 되고 2을 만나면 2이됨
                    if (grid[nextR][nextC] == 1):
                        d = 0
                    elif (grid[nextR][nextC] == 2):
                        d = 2
                    else:  # 나머지는 방향 180도 전환
                        d = (d + 2) % 4
                elif (d == 2):
                    # 2(하)일때 1를 만나면 3이 되고 4을 만나면 1이됨
                    if (grid[nextR][nextC] == 1):
                        d = 3
                    elif (grid[nextR][nextC] == 4):
                        d = 1
                    else:  # 나머지는 방향 180도 전환
                        d = (d + 2) % 4

                elif (d == 3):
                    # 3(우)일때 4를 만나면 0이 되고 3을 만나면 3이됨
                    if (grid[nextR][nextC] == 4):
                        d = 0
                    elif (grid[nextR][nextC] == 3):
                        d = 2
                    else:  # 나머지는 방향 180도 전환
                        d = (d + 2) % 4

            # 블랙홀 검사 : 게임 종료
            elif (grid[nextR][nextC] == -1):
                break

            # 원래 위치로 돌아왔는지: 게임 종료
            elif (nextR == originR and nextC == originC):
                break

            # 웜홀 검사
            # 가려고 하는 위치가 웜홀과 하나라도 같으면..
            elif (grid[nextR][nextC] >= 6):
                idx = grid[nextR][nextC] - 6
                if (nextR == holls[idx][0][0] and nextC == holls[idx][0][1]):
                    nextR = holls[idx][1][0]
                    nextC = holls[idx][1][1]
                else:
                    nextR = holls[idx][0][0]
                    nextC = holls[idx][0][1]

            r = nextR
            c = nextC
        return ping


    for i in range(n):
        for j in range(n):
            if (grid[i][j] == 0):
                # 좌표와 방향 d
                # print("=========i: ", i, "j: ", j , "d: ", 0)
                ans = max(startGame(i, j, 0), ans)  # 상
                # print("=========i: ", i, "j: ", j , "d: ", 1)
                ans = max(startGame(i, j, 1), ans)  # 좌
                # print("=========i: ", i, "j: ", j , "d: ", 2)
                ans = max(startGame(i, j, 2), ans)  # 하
                # print("=========i: ", i, "j: ", j , "d: ", 3)
                ans = max(startGame(i, j, 3), ans)  # 우

    print(f"#{tc+1} {ans}")