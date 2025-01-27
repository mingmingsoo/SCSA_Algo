T = int(input())
for tc in range(T):
    n = int(input())

    grid = [list(input()) for i in range(n)]

    row = [1, 0, 1, 1]
    col = [0, 1, -1, 1]
    isOk = False


    def check(r, c):

        for k in range(4):
            isOmok = True
            for l in range(1, 5):
                nr = r + row[k] * l
                nc = c + col[k] * l
                if (0 <= nr < n and 0 <= nc < n and grid[nr][nc] == '.'):
                    isOmok = False
                    break
                if (nr < 0 or nr >= n or nc < 0 or nc >= n):
                    isOmok = False
                    break
            if (isOmok):
                return True
        return False


    for i in range(n):
        for j in range(n):
            if (grid[i][j] == 'o'):
                if (check(i, j)):
                    isOk = True
                    break
        if (isOk):
            break
    if (isOk):
        print(f"#{tc+1} YES")
    else:
        print(f"#{tc+1} NO")
