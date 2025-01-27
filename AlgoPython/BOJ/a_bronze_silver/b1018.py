n, m = map(int, input().split())

grid = [list(input()) for i in range(n)]
# print(grid)
max = float('inf')


def changeColor(r, c, color):
    change = 0
    for i in range(r, r + 8):
        for j in range(c, c + 8):
            if ((i + j) % 2 == 0 and grid[i][j] != color):
                change += 1
            if ((i + j) % 2 == 1 and grid[i][j] == color):
                change += 1

    return change


for i in range(0, n - 8 + 1):
    for j in range(0, m - 8 + 1):
        # i,j 는 시작점임
        max = min(max, changeColor(i, j, "W"))
        max = min(max, changeColor(i, j, "B"))

print(max)
