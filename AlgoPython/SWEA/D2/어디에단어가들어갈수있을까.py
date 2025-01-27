T = int(input())


def count(grid):
    ret = 0
    for row in grid:
        cnt = 0
        for n in row:
            if n == 1:
                cnt+=1
            else:
                if cnt == k:
                    ret +=1
                cnt = 0
    return ret


for tc in range(T):
    n, k = map(int, input().split())
    grid = [[0]*(n+2)]+ [[0]+list(map(int, input().split()))+[0] for i in range(n)]+[[0]*(n+2)]
    for row in grid:
        print(*row)
    # grid_t = list(zip(*grid))
    grid_t = list(map(list, zip(*grid)))
    # print(grid_t)
    print(count(grid))
    print(count(grid_t))
    ans = count(grid) + count(grid_t)

    print(f"#{tc+1} {ans}")