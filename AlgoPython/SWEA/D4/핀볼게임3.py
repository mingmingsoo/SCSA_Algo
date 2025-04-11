# 최적화 -> 사실 벽만나면 게임 끝임
from collections import defaultdict

row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]

change_d = {(0, 2): 1, (0, 3): 3,  # 방향 전환
            (1, 3): 2, (1, 4): 0,
            (2, 1): 1, (2, 4): 3,
            (3, 1): 0, (3, 2): 2}
stop_d = set([(0, 1), (0, 4), (0, 5),  # 벽 만나면 게임 종료
              (1, 1), (1, 2), (1, 5),
              (2, 2), (2, 3), (2, 5),
              (3, 3), (3, 4), (3, 5)])


def game(sr, sc, d):
    global ans
    r, c = sr, sc
    score = 0

    while True:

        nr = r + row[d]
        nc = c + col[d]

        # 종료 조건
        if grid[nr][nc] == -1 or (nr, nc) == (sr, sc):
            return score

        # 점수 획득
        if (d, grid[nr][nc]) in stop_d:
            return score * 2 + 1
        if (d, grid[nr][nc]) in change_d:
            d = change_d[(d, grid[nr][nc])]
            score += 1

        # 웜홀
        if 6 <= grid[nr][nc] <= 10:
            (wsr, wsc), (wer, wec) = white_holl[grid[nr][nc]]
            if (nr, nc) == (wsr, wsc): nr, nc = wer, wec
            else:  nr, nc = wsr, wsc
        r = nr
        c = nc


T = int(input())
for tc in range(T):

    n = int(input())
    grid = [[5] * (n + 2)] + [[5] + list(map(int, input().split())) + [5] for i in range(n)] + [[5] * (n + 2)]
    n += 2
    ans = 0

    white_holl = defaultdict(list)
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if 6 <= grid[i][j] <= 10:
                white_holl[grid[i][j]].append((i, j))

    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if not grid[i][j]:
                for k in range(4):
                    ans = max(game(i, j, k), ans)
    print(f"#{tc + 1} {ans}")
