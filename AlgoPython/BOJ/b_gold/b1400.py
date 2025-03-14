import heapq

row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]
while True:

    n, m = map(int, input().split())
    if n == m == 0:
        break
    grid = [list(input()) for i in range(n)]
    sr = sc = er = ec = -1
    num = -1
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "A":
                sr, sc = i, j
                grid[i][j] = "#"
            elif grid[i][j] == "B":
                er, ec = i, j
                grid[i][j] = "#"
            elif "0" <= grid[i][j] <= "9":
                num = max(num, int(grid[i][j]))

    time_list = []
    for i in range(num + 1):
        tmp = list(input().split())
        two = int(tmp[2])
        three = int(tmp[3])
        if tmp[1] == "-":
            time_list.append([(1, two), (1 + two, two + three), two + three])
        else:
            time_list.append([(1 + three, two + three), (1, three), two + three])
    input()

    d = [[int(1e9)] * m for i in range(n)]  # 교차로는 두개연결밖에 안돼서 방향까지 담을 필요는 없다.
    d[sr][sc] = 0
    q = []
    heapq.heappush(q, (0, sr, sc))  # 시간, 위치
    ans = "impossible"
    while q:
        time, r, c = heapq.heappop(q)
        if r == er and c == ec:
            ans = time
            break
        if time > d[r][c]:
            continue
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < m):
                continue
            # # 으로는 아무때나 갈 수 있다
            if grid[nr][nc] == "#":
                if d[nr][nc] > time + 1:
                    d[nr][nc] = time + 1
                    heapq.heappush(q, (time + 1, nr, nc))
            elif "0" <= grid[nr][nc] <= "9":
                # 시간 계산 필요 여기서!!!
                # 동서 계산
                num = int(grid[nr][nc])
                unit = time_list[num][2]
                mok = (time + 1) // unit
                if k in (2, 3):  # 동서
                    karo1, karo2 = time_list[num][0][0] + (mok * unit), time_list[num][0][1] + (mok * unit)
                    if karo1 <= time + 1 <= karo2:  # 타이밍 맞았음
                        if d[nr][nc] > time + 1:
                            d[nr][nc] = time + 1
                            heapq.heappush(q, (time + 1, nr, nc))
                    else:  # 타이밍 안맞아서 기달려야댐
                        if time + 1 > karo1:  # 다음턴까지 기달려야댐
                            if d[nr][nc] > karo1 + unit:
                                d[nr][nc] = karo1 + unit
                                heapq.heappush(q, (karo1 + unit, nr, nc))
                        else:  # 곧 가로 턴옴
                            if d[nr][nc] > karo1:
                                d[nr][nc] = karo1
                                heapq.heappush(q, (karo1, nr, nc))
                elif k in (0, 1):
                    sero1, sero2 = time_list[num][1][0] + (mok * unit), time_list[num][1][1] + (mok * unit)
                    if sero1 <= time + 1 <= sero2:
                        if d[nr][nc] > time + 1:
                            d[nr][nc] = time + 1
                            heapq.heappush(q, (time + 1, nr, nc))
                    else:
                        if time + 1 > sero1:
                            if d[nr][nc] > sero1 + unit:
                                d[nr][nc] = sero1 + unit
                                heapq.heappush(q, (sero1 + unit, nr, nc))
                        else:
                            if d[nr][nc] > sero1:
                                d[nr][nc] = sero1
                                heapq.heappush(q, (sero1, nr, nc))

    print(ans)
