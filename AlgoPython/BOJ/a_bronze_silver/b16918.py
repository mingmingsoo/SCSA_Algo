r, c, n = map(int, input().split())

grid = [list(input()) for i in range(r)]
fullbomb = [['O']*c for i in range(r)]

def bomb(grid):
    bombgrid = [['O'] * c for i in range(r)]
    for i in range(r):
        for j in range(c):
            if (grid[i][j] == 'O'):
                bombgrid[i][j] = '.'
                for k in range(4):
                    nr = i + row[k]
                    nc = j + col[k]
                    if (0 <= nr < r and 0 <= nc < c):
                        bombgrid[nr][nc] = '.'
    return bombgrid

if (n == 1):
    for i in range(r):
        for j in range(c):
            print(grid[i][j], end="")
        print()
elif (n == 2):
    fullgrid = [['O'] * c for i in range(r)]
    for i in range(r):
        for j in range(c):
            print(fullgrid[i][j], end="")
        print()
else:
    row = [-1, 1, 0, 0]
    col = [0, 0, 1, -1]

    firstBomb = bomb(grid)
    secondBomb = bomb(firstBomb)

    if n% 4 == 3:
        for row in firstBomb:
            print("".join(row))
    elif n%4 == 1:
        for row in secondBomb:
            print("".join(row))
    else:
        for row in fullbomb:
            print("".join(row))