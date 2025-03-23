'''
# 백준 20057 마법사 상어와 토네이도
    1. 중앙 -> 0,0으로 가는 달팽이로 다시 풀어보기!!!!! 꼭!!!
'''
######################################################################
# 두번째 풀이(코드최적화: 시간은 아니고 dict 사용)
n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]

location = []
row = [0, 1, 0, -1]
col = [-1, 0, 1, 0]
dirs = {
    2: [(-1, 1, -2, 2, 0, -1, 1, -1, 1, 0), (-1, -1, 0, 0, 2, 0, 0, 1, 1, 1)],  # 우
    1: [(-1, -1, 0, 0, 2, 0, 0, 1, 1, 1), (-1, 1, -2, 2, 0, -1, 1, -1, 1, 0)],  # 아래
    0: [(-1, 1, -2, 2, 0, -1, 1, -1, 1, 0, 0), (1, 1, 0, 0, -2, 0, 0, -1, -1, -1, -1)],  # 왼
    3: [(1, 1, 0, 0, -2, 0, 0, -1, -1, -1), (-1, 1, -2, 2, 0, -1, 1, -1, 1, 0)]}  # 위
munji_list = {1: (0, 1), 2: (2, 3), 5: (4,), 7: (5, 6), 10: (7, 8)}
out = d = 0
r = c = n // 2
# 방향은 2번씩 바뀐다.
cnt = 0 # 몇번?
num = 1 # 처음엔 1씩임 ! 11223344..
two = 0 # 얘네가 2번되면 num을 늘려줌
while not (r == c == 0):
    nr = r + row[d]
    nc = c + col[d]
    origin_mungi = grid[nr][nc]
    a = origin_mungi
    for m in (1, 2, 5, 7, 10):
        munji = origin_mungi * m // 100
        for k in munji_list[m]:
            nnr = nr + dirs[d][0][k]
            nnc = nc + dirs[d][1][k]
            if not (0 <= nnr < n and 0 <= nnc < n):
                out += munji
                a -= munji
            else:
                grid[nnr][nnc] += munji
                a -= munji
    grid[nr][nc] = 0  # 이동했다.
    anr = nr + dirs[d][0][9]
    anc = nc + dirs[d][1][9]
    if not (0 <= anr < n and 0 <= anc < n):
        out += a
    else:
        grid[anr][anc] += a
    cnt += 1
    r, c = nr, nc
    if cnt == num: # 방향 전환할 차례!
        cnt = 0
        two += 1
        d = (d + 1) % 4
    if two == 2: # num을 증가시켜주기
        num += 1
        two = 0
print(out)
