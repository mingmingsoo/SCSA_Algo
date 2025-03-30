import sys

sys.setrecursionlimit(10 ** 5)
time = 1


def dfs(r, c, cnt):
    global ans, visited
    # 갈 수 있는 곳이 없으면 return
    if cnt >= 1_000_001:
        return
    if cnt >= ans:
        return
    ori_r, ori_c = r, c
    path = set()
    real_go = False
    for k in range(4):
        go = False
        r, c = ori_r, ori_c
        while True:
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < m) or visited[nr][nc]:
                break
            visited[nr][nc] = True
            path.add((nr,nc))
            go = True
            r = nr
            c = nc
        if go:
            real_go = True
            dfs(r, c, cnt + 1)
            for pr,pc in path:
                visited[pr][pc] = False

    if not real_go:
        fill = True
        for i in range(n):
            for j in range(m):
                if not visited[i][j]:
                    fill = False
                    break
            if not fill:
                break
        if fill:
            ans = min(ans, cnt)
        return


while True:
    '''
    구슬탈출 비슷한데
    q에 visited를 달고다녀야할듯 합니다.
    모든 점에서 봐야되는건가??
    이러면 메모리가..........
    '''

    try:
        line = sys.stdin.readline().strip()
        if not line:
            break
        n, m = map(int, line.split())
    except EOFError:
        break
    grid = [list(input()) for i in range(n)]
    ans = 1_000_001
    visited = [[False] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "*":
                visited[i][j] = True
    row = [-1, 1, 0, 0]
    col = [0, 0, 1, -1]

    for i in range(n):
        for j in range(m):
            if grid[i][j] == ".":
                visited[i][j] = True
                dfs(i, j, 0)
                visited[i][j] = False
    print(f"Case {time}:", end=  " ")
    if ans == 1_000_001:
        print(-1, end = " ")
    else:
        print(ans, end = " ")
    time+=1