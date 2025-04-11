from collections import deque, defaultdict


def solution(game_board, table):
    n = len(game_board)
    for i in range(n):
        for j in range(n):
            table[i][j] = 1 - table[i][j]  # table 값 바꿔치기 해주기

    table_dict = defaultdict(list)
    row = [-1, 1, 0, 0]
    col = [0, 0, 1, -1]

    def rotation(small_grid):
        sn, sm = len(small_grid), len(small_grid[0])
        ro = [[0] * sn for i in range(sm)]
        for i in range(sm):
            for j in range(sn):
                ro[i][j] = small_grid[sn - j - 1][i]
        return ro

    def bfs(sr, sc, num, grid):
        q = deque([(sr, sc)])
        minr, minc, maxr, maxc = sr, sc, sr, sc
        while q:
            r, c = q.popleft()
            maxr = max(r, maxr)
            maxc = max(c, maxc)
            minr = min(r, minr)
            minc = min(c, minc)
            for k in range(4):
                nr = r + row[k]
                nc = c + col[k]
                if not (0 <= nr < n and 0 <= nc < n) or grid[nr][nc] or visited[nr][nc]:
                    continue
                visited[nr][nc] = num
                q.append((nr, nc))
        small_grid = [_[minc:maxc + 1] for _ in grid[minr:maxr + 1]]
        table_dict[num].append(small_grid)  # 0
        small_grid = rotation(small_grid)
        table_dict[num].append(small_grid)  # 90
        small_grid = rotation(small_grid)
        table_dict[num].append(small_grid)  # 180
        small_grid = rotation(small_grid)
        table_dict[num].append(small_grid)  # 270

    def bfs_board(sr, sc, num, grid):
        q = deque([(sr, sc)])
        cnt = 0
        minr, minc, maxr, maxc = sr, sc, sr, sc
        lo = []
        while q:
            r, c = q.popleft()
            cnt += 1
            lo.append((r, c))
            maxr = max(r, maxr)
            maxc = max(c, maxc)
            minr = min(r, minr)
            minc = min(c, minc)
            for k in range(4):
                nr = r + row[k]
                nc = c + col[k]
                if not (0 <= nr < n and 0 <= nc < n) or grid[nr][nc] or visited[nr][nc]:
                    continue
                visited[nr][nc] = num
                q.append((nr, nc))
        small_grid = [_[minc:maxc + 1] for _ in grid[minr:maxr + 1]]
        board_dict[sr * n + sc] = small_grid
        board_location[sr * n + sc] = lo
        cnt_dict[sr * n + sc] = cnt

    def is_same(lo, i):
        for grid in table_dict[i]:
            if grid == board_dict[lo]:
                return True
        return False

    visited = [[0] * n for i in range(n)]
    num = 1
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and not table[i][j]:
                visited[i][j] = num
                bfs(i, j, num, table)
                num += 1
    tn = num

    # 미리 테이블 어떤 모양인지 만들어 놓기

    visited = [[0] * n for i in range(n)]
    board_dict = {}
    board_location = {}
    cnt_dict = {}
    num = 1
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and not game_board[i][j]:
                visited[i][j] = 1
                bfs_board(i, j, num, game_board)

    ans = 0
    used = [False] * tn
    for lo in range(n * n):
        r = lo // n
        c = lo % n
        if game_board[r][c]:  # 이미 채워졌으면 넘어가
            continue
        if lo in board_dict:
            for i in range(1, tn):
                if not used[i]:
                    if is_same(lo, i):
                        used[i] = True
                        for r, c in board_location[lo]:
                            game_board[r][c] = 1
                        ans += cnt_dict[lo]
                        break

    return ans
