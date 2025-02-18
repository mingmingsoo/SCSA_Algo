N = int(input())
line = input()
'''

###..#..
#.#..#..
###..#..
#.#..#..
###..#..

'''
n = 5
m = N // 5
grid = [[0] * (m) for i in range(n)]
num = 0
for s in line:
    i = num // m
    j = num % m
    if (s == "#"):
        grid[i][j] = 1
    num += 1

ans = []

jdx = 0
visited = [False] * m


def is_number(j):
    if ( j+2<m and
            grid[0][j] == 1 and grid[0][j + 1] == 1 and grid[0][j + 2] == 1 and
            grid[1][j] == 1 and grid[1][j + 1] == 0 and grid[1][j + 2] == 1 and
            grid[2][j] == 1 and grid[2][j + 1] == 0 and grid[2][j + 2] == 1 and
            grid[3][j] == 1 and grid[3][j + 1] == 0 and grid[3][j + 2] == 1 and
            grid[4][j] == 1 and grid[4][j + 1] == 1 and grid[4][j + 2] == 1):
        for jj in range(j, j + 3):
            visited[jj] = True
        return 0

    elif ( j+2<m and
            grid[0][j] == 1 and grid[0][j + 1] == 1 and grid[0][j + 2] == 1 and
            grid[1][j] == 0 and grid[1][j + 1] == 0 and grid[1][j + 2] == 1 and
            grid[2][j] == 1 and grid[2][j + 1] == 1 and grid[2][j + 2] == 1 and
            grid[3][j] == 1 and grid[3][j + 1] == 0 and grid[3][j + 2] == 0 and
            grid[4][j] == 1 and grid[4][j + 1] == 1 and grid[4][j + 2] == 1):
        for jj in range(j, j + 3):
            visited[jj] = True
        return 2

    elif ( j+2<m and
            grid[0][j] == 1 and grid[0][j + 1] == 1 and grid[0][j + 2] == 1 and
            grid[1][j] == 0 and grid[1][j + 1] == 0 and grid[1][j + 2] == 1 and
            grid[2][j] == 1 and grid[2][j + 1] == 1 and grid[2][j + 2] == 1 and
            grid[3][j] == 0 and grid[3][j + 1] == 0 and grid[3][j + 2] == 1 and
            grid[4][j] == 1 and grid[4][j + 1] == 1 and grid[4][j + 2] == 1):
        for jj in range(j, j + 3):
            visited[jj] = True
        return 3

    elif ( j+2<m and
            grid[0][j] == 1 and grid[0][j + 1] == 0 and grid[0][j + 2] == 1 and
            grid[1][j] == 1 and grid[1][j + 1] == 0 and grid[1][j + 2] == 1 and
            grid[2][j] == 1 and grid[2][j + 1] == 1 and grid[2][j + 2] == 1 and
            grid[3][j] == 0 and grid[3][j + 1] == 0 and grid[3][j + 2] == 1 and
            grid[4][j] == 0 and grid[4][j + 1] == 0 and grid[4][j + 2] == 1):
        for jj in range(j, j + 3):
            visited[jj] = True
        return 4

    elif ( j+2<m and
            grid[0][j] == 1 and grid[0][j + 1] == 1 and grid[0][j + 2] == 1 and
            grid[1][j] == 1 and grid[1][j + 1] == 0 and grid[1][j + 2] == 0 and
            grid[2][j] == 1 and grid[2][j + 1] == 1 and grid[2][j + 2] == 1 and
            grid[3][j] == 0 and grid[3][j + 1] == 0 and grid[3][j + 2] == 1 and
            grid[4][j] == 1 and grid[4][j + 1] == 1 and grid[4][j + 2] == 1):
        for jj in range(j, j + 3):
            visited[jj] = True
        return 5


    elif ( j+2<m and
            grid[0][j] == 1 and grid[0][j + 1] == 1 and grid[0][j + 2] == 1 and
            grid[1][j] == 1 and grid[1][j + 1] == 0 and grid[1][j + 2] == 0 and
            grid[2][j] == 1 and grid[2][j + 1] == 1 and grid[2][j + 2] == 1 and
            grid[3][j] == 1 and grid[3][j + 1] == 0 and grid[3][j + 2] == 1 and
            grid[4][j] == 1 and grid[4][j + 1] == 1 and grid[4][j + 2] == 1):
        for jj in range(j, j + 3):
            visited[jj] = True
        return 6

    elif ( j+2<m and
            grid[0][j] == 1 and grid[0][j + 1] == 1 and grid[0][j + 2] == 1 and
            grid[1][j] == 0 and grid[1][j + 1] == 0 and grid[1][j + 2] == 1 and
            grid[2][j] == 0 and grid[2][j + 1] == 0 and grid[2][j + 2] == 1 and
            grid[3][j] == 0 and grid[3][j + 1] == 0 and grid[3][j + 2] == 1 and
            grid[4][j] == 0 and grid[4][j + 1] == 0 and grid[4][j + 2] == 1):
        for jj in range(j, j + 3):
            visited[jj] = True
        return 7

    elif ( j+2<m and
            grid[0][j] == 1 and grid[0][j + 1] == 1 and grid[0][j + 2] == 1 and
            grid[1][j] == 1 and grid[1][j + 1] == 0 and grid[1][j + 2] == 1 and
            grid[2][j] == 1 and grid[2][j + 1] == 1 and grid[2][j + 2] == 1 and
            grid[3][j] == 1 and grid[3][j + 1] == 0 and grid[3][j + 2] == 1 and
            grid[4][j] == 1 and grid[4][j + 1] == 1 and grid[4][j + 2] == 1):
        for jj in range(j, j + 3):
            visited[jj] = True
        return 8

    elif ( j+2<m and
            grid[0][j] == 1 and grid[0][j + 1] == 1 and grid[0][j + 2] == 1 and
            grid[1][j] == 1 and grid[1][j + 1] == 0 and grid[1][j + 2] == 1 and
            grid[2][j] == 1 and grid[2][j + 1] == 1 and grid[2][j + 2] == 1 and
            grid[3][j] == 0 and grid[3][j + 1] == 0 and grid[3][j + 2] == 1 and
            grid[4][j] == 1 and grid[4][j + 1] == 1 and grid[4][j + 2] == 1):
        for jj in range(j, j + 3):
            visited[jj] = True
        return 9
    else:
        visited[j] = True
        return 1


while jdx < m:
    # 열만 팬다.
    if (not visited[jdx] and grid[0][jdx] == 1):
        visited[jdx] = True
        ans.append(is_number(jdx))
    jdx += 1
print("".join(map(str, ans)))
