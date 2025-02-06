'''
코드를 줄여보았습니다.
'''
def isrange(nr, nc):
    if (0 <= nr < n and 0 <= nc < m and grid[nr][nc] == "."):
        return True
    else:
        return False
def game(order):
    global r, c, d
    if (order in "URDL"):
        nd = "URDL".index(order)
        nr = r + row[nd]
        nc = c + col[nd]
        if (isrange(nr, nc)):
            r = nr
            c = nc
        d = nd #  못가도 방향은 바뀜
    elif (order == "S"):
        # 지금 방향은 d 위치는 r,c
        br = r
        bc = c

        while True:
            bomb_r = br + row[d]
            bomb_c = bc + col[d]
            if (not (0 <= bomb_r < n and 0 <= bomb_c < m)):  # 폭탄이 넘어갔어요
                break
            if (grid[bomb_r][bomb_c] == "*"):  # 벽이 부서졌어요
                grid[bomb_r][bomb_c] = "."
                break
            elif (grid[bomb_r][bomb_c] == "#"):  # 강철에 부딛혀서 아무일도 없어요
                break
            br = bomb_r
            bc = bomb_c

T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    r, c, d = -1, -1, -1
    grid = [list(input()) for i in range(n)]
    for i in range(n):  # 초기 위치와 방향 확인
        for j in range(m):
            if (grid[i][j] in "^>v<"):
                r, c, d = i, j, "^>v<".index(grid[i][j])
                grid[r][c] = "." # 떠날거니까 평지로..

    input()
    order_list = list(input())
    row = [-1, 0, 1, 0]
    col = [0, 1, 0, -1]

    for order in order_list:
        game(order)

    grid[r][c] = "^>v<"[d]

    print(f"#{tc + 1}",end = " ")
    for i in range(n):
        for j in range(m):
            print(grid[i][j],end="")
        print()
