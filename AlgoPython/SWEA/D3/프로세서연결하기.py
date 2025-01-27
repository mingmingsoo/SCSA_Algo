'''
제출횟수 : 2회
틀린이유 : 최소 길이를 갱신하는 로직이 잘못됐었음
실행시간: 3,097 ms
코드길이: 2,765

모든 경우의 수를 탐색하고(코어 마다마다 사방으로도 경우의 수를 따져줘야함)
1. 가장 많은 코어에 연결
2. 코어 갯수가 같다면 전선 길이의 합이 최소
* 가장자리 = 테두리에 있는 애들은 이미 코어가 연결되어있으므로 제외해도됨.
'''
T = int(input())
for tc in range(T):
    n = int(input())

    grid = [list(map(int, input().split())) for i in range(n)]

    cores = []
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if (grid[i][j] == 1):
                cores.append([i, j]) # 가장자리에 있는 코어들읕 이미 전선이 연결되어있으므로 제외해도됨
    # print(cores)
    anslen = float("inf") # 출력해야할 전선 길이
    anscore = -1 # 최대 연결 코어 수


    def dfs(idx, core, length):
        global anscore, anslen
        if (idx > len(cores) - 1): # 모든 코어를 다 탐색했으면 출력값들을 갱신해줌.
            if (anscore < core):
                anscore = core
                anslen = length
            if(anscore == core and anslen > length): # 만약 코어 수가 같고 길ㄹ이가 더 짧으면 길이 갱신
                anslen = length
            return
        r, c = cores[idx] # 탐색하는 코어의 위치
        # 상 : 위쪽으로 전선을 둘 수 있는가?
        isUp = True
        for i in range(0, r):
            if (grid[i][c] != 0):
                isUp = False # 위쪽에 다른 코어나, 연결된 전선이 있으면 위로 못감
                break
        if (isUp): # 위로 갈 수 있다면
            for i in range(0, r):
                grid[i][c] = 3  # 전선 표시
            dfs(idx + 1, core + 1, length + r) # 다른 코어 idx, 연결가능한 코어수 +1, 현재까지 전선 길이 + 위치에 따른 전선 길이
            for i in range(0, r): # 전선 원상복구
                grid[i][c] = 0
        else:
            dfs(idx + 1, core , length ) # 만약 위쪽으로 갈 수 없다면 다음 코어 탐색

        # 하 : 아래쪽으로 전선을 둘 수 있는가?
        isDown = True
        for i in range(r + 1, n):
            if (grid[i][c] != 0):
                isDown = False
                break
        if (isDown):
            for i in range(r + 1, n):
                grid[i][c] = 3  # 전선 표시
            dfs(idx + 1, core + 1, length + (n - r - 1))
            for i in range(r + 1, n):
                grid[i][c] = 0  # 원상 복구
        else:
            dfs(idx + 1, core , length )

        # 좌 : 왼쪽으로 전선을 둘 수 있는가?
        isLeft = True
        for j in range(0, c):
            if (grid[r][j] != 0):
                isLeft = False
                break
        if (isLeft):
            for j in range(0, c):
                grid[r][j] = 3  # 전선 표시
            dfs(idx + 1, core + 1, length + c)
            for j in range(0, c):
                grid[r][j] = 0  # 원상 복구
        else:
            dfs(idx + 1, core , length )

        # 우 : 오른쪽으로 전선을 둘 수 있는가?
        isRight = True
        for j in range(c + 1, n):
            if (grid[r][j] != 0):
                isRight = False
                break
        if (isRight):
            for j in range(c + 1, n):
                grid[r][j] = 3  # 전선 표시
            dfs(idx + 1, core + 1, length + (n - c - 1))
            for j in range(c + 1, n):
                grid[r][j] = 0  # 원상 복구
        else:
            dfs(idx + 1, core , length )


    dfs(0, 0, 0)  # idx, core 수, 전선 길이
    # print(anscore)
    # print(f"#{tc+1} {anscore}")
    print(f"#{tc+1} {anslen}")


