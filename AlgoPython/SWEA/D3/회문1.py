T = 10
for tc in range(T):
    length = int(input())
    grid = [list(input()) for i in range(8)]

    row = [1, 0]
    col = [0, 1]

    cnt = 0


    def karocheck(r, c):
        origin = grid[r][c:c + length]
        # print(origin)
        rotation = origin[::-1]
        if (origin == rotation):
            return True


    def serocheck(r, c):
        origin = []
        for i in range(r, r + length):
            origin.append(grid[i][c])
        # print(origin)
        rotation = origin[::-1]
        if (origin == rotation):
            return True


    for i in range(8):
        for j in range(8):
            # 시작점 설정
            if (j <= 8 - length and karocheck(i, j)):
                cnt += 1
            if (i <= 8 - length and serocheck(i, j)):
                cnt += 1
    print(f"#{tc+1} {cnt}")