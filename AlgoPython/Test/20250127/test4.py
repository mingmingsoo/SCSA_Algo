T = int(input())
for tc in range(T):
    n = int(input())

    grid = [list(input()) for i in range(n)]

    visited = [[0] * n for i in range(n)]
    cnt = 0
    isOneSquare = False


    def square(r, c):
        karoLen = 0
        for j in range(c, n):
            if (grid[r][j] == "#"):
                karoLen += 1
            else:
                break
        seroLen = 0
        for i in range(r, n):
            if (grid[i][c] == "#"):
                seroLen += 1
            else:
                break
        if (karoLen != seroLen):
            return False
        for i in range(r, r + seroLen):
            for j in range(c, c + karoLen):
                visited[i][j] = 1

        for i in range(r, r + seroLen):
            for j in range(c, c + karoLen):
                if (grid[i][j] != "#"):
                    return False

        for i in range(r, r + karoLen):
            if (c + seroLen < n and grid[i][c + seroLen] == '#'):
                return False
        for i in range(r, r + karoLen):
            if (c - 1 >= 0 and grid[i][c - 1] == '#'):
                return False
        for j in range(c, c + seroLen):
            if (r - 1 >= 0 and grid[r - 1][j] == '#'):
                return False
        for j in range(c, c + seroLen):
            if (r + karoLen < n and grid[r + karoLen][j] == '#'):
                return False

        return True


    for i in range(n):
        for j in range(n):
            if (grid[i][j] == "#" and visited[i][j] == 0):
                if (square(i, j)):
                    cnt += 1
                    isOneSquare = True
                if (cnt >= 2):
                    isOneSquare = False
                    break
        if (cnt >= 2):
            break
    if (isOneSquare):
        print(f"#{tc+1} yes")
    else:
        print(f"#{tc+1} no")

