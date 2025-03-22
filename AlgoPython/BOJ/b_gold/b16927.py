'''
배열을 한칸씩 돌리는데
mod 찾아내기

한칸 흐어 흠 ㄹ남음낭ㅁㄴ어ㅏㅣㄴ

도대체가 왜안되느지 모르겠네
while 에서 for문으로 변경
'''
import sys

input = sys.stdin.readline

n, m, rot = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
r, c, N, M = 0, 0, n, m
cnt = 0

def rotate(grid, r, c, N, M):
    global cnt
    cnt+=1
    mod = (N - r) * 2 + (M - c - 2) * 2
    if mod == 0:
        new_rot = 0
    else:
        new_rot = rot % mod
    for idx in range(new_rot):
        tmp = grid[r][c]
        for j in range(c, M - 1):
            grid[r][j] = grid[r][j + 1]
        for i in range(r, N - 1):
            grid[i][M - 1] = grid[i + 1][M - 1]
        for j in range(M - 1, c, -1):
            grid[N - 1][j] = grid[N - 1][j - 1]
        for i in range(N - 1, r, -1):
            grid[i][c] = grid[i - 1][c]
        grid[r + 1][c] = tmp


for i in range(min(m, n) // 2):
    rotate(grid, r, c, N, M)
    r += 1
    c += 1
    N -= 1
    M -= 1
for _ in grid:
    print(*_)
print(cnt)
# num = 1
# for i in range(300):
#     for j in range(149):
#         print(num, end = " ")
#         num+=1
#     print()