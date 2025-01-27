T = int(input())
for tc in range(T):
    n, m = map(int, input().split())

    grid = [list(map(int, input().split())) + [0] for i in range(n)] + [[0] * (n + 1)]

    grid_T = list(map(list, zip(*grid)))

    ans = -1


    def count(grid):
        ret = 0
        for row in grid:
            cnt = 0
            for n in row:
                if n == 1:
                    cnt += 1
                else:
                    ret = max(ret, cnt)
                    cnt = 0
        # print(ret)
        return ret


    ans = max(ans, count(grid), count(grid_T))
    print(f"#{tc+1} {ans}")