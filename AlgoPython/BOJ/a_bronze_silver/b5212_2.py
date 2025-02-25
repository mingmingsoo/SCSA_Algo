'''
문제설명
    50년후에 인접한 3, 4칸이 바다면 땅은 잠김
문제 구상
    주변 바다갯수를 세서 바다에 잠기게 해준다.
    이때 counting 메서드 사용
'''


def counting(r, c):
    count = 0

    for k in range(4):
        nr = r + row[k]
        nc = c + col[k]
        if not (0 <= nr < n and 0 <= nc < m):
            count += 1
        elif grid[nr][nc] == ".":
            count += 1

    return count


n, m = map(int, input().split())

grid = [list(input()) for i in range(n)]
grid_copy = [_[:] for _ in grid]

row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]

for i in range(n):
    for j in range(m):
        if grid[i][j] == "X":
            num = counting(i, j)
            if (num >= 3):
                grid_copy[i][j] = "."  # 3면 이상인 애들만 grid_copy에 바꿔줌
                # copy에 바꿔주는 이유는 바로 grid를 바꾸면
                # 인접한 섬들이 영향을 받기 때문

# 출력을 위한 min, max 구하기
minr, minc, maxr, maxc = n, m, 0, 0

for i in range(n):
    for j in range(m):
        if grid_copy[i][j] == "X":
            minr, maxr, minc, maxc = min(minr, i), max(maxr, i), min(minc, j), max(maxc, j)

for i in range(minr, maxr + 1):
    for j in range(minc, maxc + 1):
        print(grid_copy[i][j], end="")
    print()
