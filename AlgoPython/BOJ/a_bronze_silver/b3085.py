'''
문제설명
    인접한 곳에 나랑 다른 사탕 있으면 교환
    최대 사탕 구하기
구상
    0,0, ~ n,n 완탐

'''

n = int(input())
grid = [list(input()) for i in range(n)]
row = [1, 0]
col = [0, 1]
ans = 0


def find_max(r, c):
    ele_max = 1

    row_count = 1
    for j in range(n - 1):
        if grid[r][j] == grid[r][j + 1]:
            row_count += 1
            ele_max = max(ele_max, row_count)
        else:
            row_count = 1

    col_count = 1
    for i in range(n - 1):
        if grid[i][c] == grid[i + 1][c]:
            col_count += 1
            ele_max = max(ele_max, col_count)
        else:
            col_count = 1

    return ele_max


def candy():
    global ans

    for i in range(n):
        for j in range(n):
            for k in range(2):

                my_color = grid[i][j]
                nr = i + row[k]
                nc = j + col[k]
                if not (0 <= nr < n and 0 <= nc < n):
                    continue
                ans = max(find_max(i, j), ans)
                origin = grid[nr][nc]
                grid[i][j], grid[nr][nc] = grid[nr][nc], grid[i][j]
                ans = max(find_max(i, j), find_max(nr, nc), ans)
                if ans == n:  # 만약 최댓값이면 그냥 stop.
                    return
                grid[nr][nc] = origin
                grid[i][j] = my_color


candy()
print(ans)
