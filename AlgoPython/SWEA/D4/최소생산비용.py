T = int(input())
for tc in range(T):
    '''

    열을 선택하는데 중복되면 안된다.
    '''

    n = int(input())
    grid = [list(map(int, input().split())) for i in range(n)]
    ans = 1501
    sel = [0] * n
    visited = [False] * n


    def btk(idx,sm):
        global ans
        if(sm>ans):
            return
        if (idx == n):
            ans = min(ans, sm)
            return

        for i in range(n):
            if (not visited[i]):
                visited[i] = True
                sel[idx] = i
                btk(idx + 1, sm+grid[i][idx])
                visited[i] = False


    btk(0,0)
    print(f"#{tc + 1} {ans}")
