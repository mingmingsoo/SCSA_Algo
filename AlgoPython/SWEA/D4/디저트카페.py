'''
코드리팩토링
    가지치기

문제설명
    대각선의 범위를 찾아서 중복이 발생하지 않는 최대 합을 구하기

구상
    대각선 길이 1<=d1,d2<=n-2
    시작점은 (0,1) ~ (n-3,n-2) 까지
    각 점 (r,c), (r+d1,c-d1), (r+d2,c+d2),(r+d1+d2,c+d2-d1)
'''

row = [1, 1]
col = [-1, 1]


def cal(i, j, d1, d2):
    global ans
    dessert = set()
    r, c = i, j
    dessert.add(grid[i][j])
    for cnt in range(d1):
        nr = r + row[0]
        nc = c + col[0]
        if grid[nr][nc] not in dessert:
            dessert.add(grid[nr][nc])
        else:
            return
        r = nr
        c = nc

    for cnt in range(d2):
        nr = r + row[1]
        nc = c + col[1]
        if grid[nr][nc] not in dessert:
            dessert.add(grid[nr][nc])
        else:
            return
        r = nr
        c = nc

    r, c = i, j
    for cnt in range(d2):
        nr = r + row[1]
        nc = c + col[1]
        if grid[nr][nc] not in dessert:
            dessert.add(grid[nr][nc])
        else:
            return
        r = nr
        c = nc

    for cnt in range(d1 - 1):
        nr = r + row[0]
        nc = c + col[0]
        if grid[nr][nc] not in dessert:
            dessert.add(grid[nr][nc])
        else:
            return
        r = nr
        c = nc

    ans = max(ans, (d1 + d2) * 2)


T = int(input())
for tc in range(T):

    n = int(input())
    grid = [list(map(int, input().split())) for i in range(n)]
    ans = -1

    for i in range(n - 2):
        for j in range(1, n - 1):
            for d1 in range(1, n - 1):
                for d2 in range(1, n - 1):
                    if (j - d1 >= 0 and j + d2 < n and i + d1 + d2 < n):
                        if (d1 + d2) * 2 <= ans: # 어차피 값 갱신 안됨 대각선 작아서
                            continue
                        cal(i, j, d1, d2)
    print(f"#{tc + 1} {ans}")
