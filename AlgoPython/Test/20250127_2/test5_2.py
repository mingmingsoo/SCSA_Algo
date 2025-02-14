'''
엣지케이스
시작점이 0이라는 조건이 없는데 0으로 설정할 수 있을 것 같습니다.

1
4
0 0 3 3
9999
9999
9999
9999

정답 63

1
5
0 0 4 4
11111
00001
11111
10000
11111
정답 3

1
5
0 0 4 4
11111
99991
11111
19999
11111
정답 17

'''
T = int(input())
for tc in range(T):

    n = int(input())
    sr, sc, er, ec = map(int, input().split())

    grid = [list(map(int, input())) for i in range(n)]
    ans = 90_001  # 최대 먼지양
    visited = [[False] * n for i in range(n)]
    row = [-1, 1, 0, 0]
    col = [0, 0, 1, -1]


    def dfs(r, c, er, ec, smog):
        global ans
        if(smog>ans): # 볼 필요가 없음
            return
        if (r == er and c == ec):
            ans = min(ans, smog)
            return
        visited[r][c] = True

        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if (not (0 <= nr < n and 0 <= nc < n)):
                continue
            if (not visited[nr][nc]):
                dfs(nr, nc, er, ec, smog + grid[nr][nc])

        visited[r][c] = False


    dfs(sr, sc, er, ec, grid[sr][sc])
    print(f"#{tc+1} {ans}")
