T = int(input())
for tc in range(T):
    '''
    문제설명
        2개의 위치를 조합으로 뽑고 최대 벌꿀양 계산
    '''

    n, m, limit = map(int, input().split())
    grid = [list(map(int, input().split())) for i in range(n)]

    sel = [0, 0]  # 시작점을 담아줌
    ans = 0


    def perm(idx, arr, visited, honey_sel):
        global ele_score
        if idx == m:
            score = 0
            total = 0
            for honey in honey_sel:
                if total + honey <= limit:
                    total += honey
                    score += honey * honey
                else:
                    break
            ele_score = max(ele_score, score)
            return

        for i in range(m):
            if not visited[i]:
                visited[i] = True
                honey_sel[idx] = arr[i]
                perm(idx + 1, arr, visited, honey_sel)
                visited[i] = False


    ele_score = 0


    def combi(sidx, idx):
        global ans, ele_score
        if sidx == 2:
            score = 0
            for r, c in sel:
                tmp = []
                for j in range(c, c + m):
                    tmp.append(grid[r][j])
                visited = [False] * m
                honey_sel = [0] * m
                ele_score = 0
                perm(0, tmp, visited, honey_sel)
                score += ele_score
            ans = max(ans, score)
            return
        if idx == n * n:
            return

        r = idx // n
        c = idx % n
        if c + m > n:
            combi(sidx, idx + 1)
            return

        if sidx > 0:
            br, bc = sel[sidx - 1]
            if br == r and c - bc < m:
                combi(sidx, idx + 1)
                return

        sel[sidx] = (r, c)
        combi(sidx + 1, idx + 1)
        combi(sidx, idx + 1)


    combi(0, 0)
    print(f"#{tc+1} {ans}")
