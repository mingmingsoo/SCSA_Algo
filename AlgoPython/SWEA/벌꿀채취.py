T = int(input())
for tc in range(T):
    '''
    완.탐
    '''

    n, m, limit = map(int, input().split())
    grid = [list(map(int, input().split())) for i in range(n)]

    sel = [0] * 2
    ans = 0
    real_honey = 0
    maxx = 0


    def perm(idx, honey_list, sel_honey, visited):
        global maxx
        if idx == len(honey_list):
            summ = 0
            ele_max = 0
            ele_honey = []
            for honey in sel_honey:
                if summ + honey <= limit:
                    ele_honey.append(honey)
                    summ += honey
                else:
                    break
            for honey in ele_honey:
                ele_max += honey ** 2

            if ele_max > maxx:
                maxx = ele_max
            return

        for i in range(len(honey_list)):
            if not visited[i]:
                visited[i] = True
                sel_honey[idx] = honey_list[i]
                perm(idx + 1, honey_list, sel_honey, visited)
                visited[i] = False


    def find(honey_list):

        sel_honey = [0] * len(honey_list)
        visited = [False] * len(honey_list)
        perm(0, honey_list, sel_honey, visited)

        return maxx


    def combi(sidx, idx):
        global ans, maxx
        if sidx == 2:
            numbering = [[False] * n for i in range(n)]
            ele_total = 0
            for r, c in sel:
                maxx = 0
                ele_honey = []
                if c + m >= n + 1:
                    return
                for j in range(c, c + m):
                    if numbering[r][j]:
                        return
                    numbering[r][j] = True
                    ele_honey.append(grid[r][j])
                ele_total += find(ele_honey)

            ans = max(ele_total, ans)

            return

        if idx == n * n:
            return

        sel[sidx] = (idx // n, idx % n)
        combi(sidx + 1, idx + 1)
        combi(sidx, idx + 1)


    combi(0, 0)
    print(f"#{tc+1} {ans}")