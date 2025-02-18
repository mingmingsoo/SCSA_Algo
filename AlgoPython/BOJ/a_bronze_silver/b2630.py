n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]

blue = 0
white = 0


def isfull(start_r, start_c, size):
    first = grid[start_r][start_c]
    for i in range(start_r, start_r+size):
        for j in range(start_c,start_c+size):
            if grid[i][j]!=first:
                return False
    return True

def check(start_r, start_c, size):
    global blue, white

    if(isfull(start_r, start_c, size)):
        if (grid[start_r][start_c] == 1):
            blue += 1
        else:
            white += 1
    else:
        check(start_r, start_c, size // 2)
        check(start_r, start_c+size // 2, size // 2)
        check(start_r+size // 2, start_c, size // 2)
        check(start_r+size // 2, start_c+size // 2, size // 2)


check(0, 0, n)
print(white)
print(blue)
