'''
문제 설명
    각 구역을 5개로 나눈다
    선거구는 구역을 적어도 하나 포함
    기준점 (x, y)와 경계의 길이 d1, d2를 정한다.
    (d1, d2 ≥ 1, 1 ≤ x < x+d1+d2 ≤ N, 1 ≤ y-d1 < y < y+d2 ≤ N)

틀린이유 : 5만나면 break 임
'''
n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]
row = [1, 1]
col = [1, -1]


def btk(r, c, d1, d2):
    global ans
    # print(r,c,d1,d2)
    numbering = [[0] * n for i in range(n)]
    R, C = r, c
    # 오른쪽 대각선
    numbering[r][c] = 5
    for i in range(d2):
        nr = r + row[0]
        nc = c + col[0]
        numbering[nr][nc] = 5
        r = nr
        c = nc
    #  오른쪽 에서 밑쪽
    for i in range(d1):
        nr = r + row[1]
        nc = c + col[1]
        numbering[nr][nc] = 5
        r = nr
        c = nc
    r, c = R, C
    # 왼쪽 아래로
    for i in range(d1):
        nr = r + row[1]
        nc = c + col[1]
        numbering[nr][nc] = 5
        r = nr
        c = nc
    #  오른쪽 에서 밑쪽
    for i in range(d2):
        nr = r + row[0]
        nc = c + col[0]
        numbering[nr][nc] = 5
        r = nr
        c = nc
    r1, c1, r2, c2, r3, c3, r4, c4 = 0, 0, 0, 0, 0, 0, 0, 0

    for i in range(n):
        s1, s2 = 10000, -1
        for j in range(n):
            if numbering[i][j] == 5:
                s1 = min(s1, j)
                s2 = max(s1, j)
        for j in range(s1 + 1, s2):
            numbering[i][j] = 5

    # 끝점을 어케구하냐.
    for i in range(R + d1):
        for j in range(C + 1):
            if numbering[i][j] == 5:
                break
            numbering[i][j] = 1

    for i in range(R + d2 + 1):
        for j in range(n - 1, C, -1):
            if numbering[i][j] == 5:
                break
            numbering[i][j] = 2

    for i in range(R + d1, n):
        for j in range(C - d1 + d2):
            if numbering[i][j] == 5:
                break
            numbering[i][j] = 3

    for i in range(R + d2 + 1, n):
        for j in range(n - 1, C - d1 + d2 - 1, -1):
            if numbering[i][j] == 5:
                break
            numbering[i][j] = 4

    a1, a2, a3, a4, a5 = 0, 0, 0, 0, 0
    for i in range(n):
        for j in range(n):
            if numbering[i][j] == 1:
                a1 += grid[i][j]
            elif numbering[i][j] == 2:
                a2 += grid[i][j]
            elif numbering[i][j] == 3:
                a3 += grid[i][j]
            elif numbering[i][j] == 4:
                a4 += grid[i][j]
            elif numbering[i][j] == 5:
                a5 += grid[i][j]

    diff = max(a1, a2, a3, a4, a5) - min(a1, a2, a3, a4, a5)
    ans = min(ans, diff)


ans = 10000000000
for i in range(n):
    for j in range(n):
        # i,j, 가 기준점 (윗점)
        for d1 in range(1, n):
            for d2 in range(1, n):
                if 0 <= i < i + d1 + d2 <= n - 1 and 0 <= j - d1 < j < j + d2 <= n - 1:
                    btk(i, j, d1, d2)
                    # print(d1, d2)
print(ans)
