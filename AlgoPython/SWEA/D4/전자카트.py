T = int(input())
for tc in range(T):
    '''
    문제
        사무실 -> 관리구역 -> 사무실
        행을 기준으로 관리구역 번호?
    출력
        최소베터리 사용량

    고려사항
        0 1 -> 1 2 -> 2 3 -> 3 4 -> 4 0
        0 1 -> 1 2 -> 2 4 -> 4 3-> 3 0
        ...
        
        0,0은 불가능하므로
        열을 1부터 시작해서 행은 다시 1로, 열은 2로 이런식으로 가야함.
    '''

    n = int(input())
    grid = [list(map(int, input().split())) for i in range(n)]

    ans = 1001
    visited = [False]*n
    sel = [0]*n

    def btk(idx,cur,sm):
        global ans
        if(sm>ans):
            return
        if(idx ==n-1):
            sm += grid[cur][0]
            ans = min(ans, sm)
            return

        for i in range(1,n):
            if(not visited[i]):
                visited[i]= True
                btk(idx+1,i,sm+grid[cur][i])
                visited[i]= False

    btk(0,0,0) # idx, cur, sm
    print(f"#{tc+1} {ans}")