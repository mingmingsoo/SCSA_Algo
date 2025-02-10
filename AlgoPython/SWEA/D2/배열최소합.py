T = int(input())
for tc in range(T):
    '''
    순열
    '''

    n = int(input())
    grid = [list(map(int, input().split())) for i in range(n)]

    arr = list(range(n))

    visited = [False] * n
    ans = 1001

    def perm(idx, sm):
        global ans
        if(sm>=ans):
            return
        if(idx == n):
            ans = min(ans, sm)
            return
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                perm(idx+1,sm+grid[i][idx])
                visited[i] = False


    perm(0,0) # 세로 # 합.
    print(f"#{tc+1} {ans}")

