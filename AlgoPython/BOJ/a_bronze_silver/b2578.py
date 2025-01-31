grid = [list(map(int, input().split())) for i in range(5)]

order =[list(map(int, input().split())) for i in range(5)]


def bingo():
    line = 0
    # 확인해야할 점 : 사각형의 모서리 끝점, 행/열
    # 행, 열
    for i in range(5):
        isLine = True
        for j in range(5):
            if(grid[i][j]!=0):
                isLine = False
                break
        if(isLine):
            line+=1
        else:
            continue
    for j in range(5):
        isLine = True
        for i in range(5):
            if(grid[i][j]!=0):
                isLine = False
                break
        if(isLine):
            line+=1
        else:
            continue
    #  대각선
    isLine = True
    for i in range(5):
        if(grid[i][i] != 0):
            isLine = False
            break
    if (isLine):
        line += 1

    isLine = True
    for i in range(5):
        if(grid[i][5-i-1] != 0):
            isLine = False
            break
    if (isLine):
        line += 1
    return line


def game():
    for i in range(5):
        for j in range(5):
            num = order[i][j]
            for r in range(5):
                for c in range(5):
                    if (grid[r][c] == num):
                        grid[r][c] = 0
                        if (bingo() >= 3):
                            print(i * 5 + j+1)
                            return


game()

