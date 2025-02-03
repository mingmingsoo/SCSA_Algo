'''
문제 시작: 18:50
문제 중단 19:10
문제 다시 시작 19:48

0,0에서 탐색해서
5,4,3,2,1, 순으로 정사각형 덮을 수 있는지 확인하고
덮을 수 있으면 큰 순으로 덮음(덮음처리 필요) -> 이건 안될듯...

재귀로 1,2,3,4,5 일 때 다 탐색
0 0 0 0 0 0 0 0 0 0
0 1 1 1 1 1 0 0 0 0
0 1 1 1 1 1 0 0 0 0
0 0 1 1 1 1 0 0 0 0
0 0 1 1 1 1 0 0 0 0
0 1 1 1 1 1 1 1 1 1
0 1 1 1 0 1 1 1 1 1
0 1 1 1 0 1 1 1 1 1
0 0 0 0 0 1 1 1 1 1
0 0 0 0 0 1 1 1 1 1

이 경우에 무조건 큰걸로 하면 안됨. 다 따져줘야함.
1일때 좌표를 다 담아서
덭혔으면 넘어가고 안덮혔으면 재귀 실행

각각의 색종이는 5개씩만 있음

색종이 위치를 리스트로 담으면 안되고
이중포면돌면서 1이 있다면 다 따져주고 그에 맞는 i,j로 넘어가게 해야함.

'''
import math

oneLocation = []
grid = [[] for i in range(10)]
for i in range(10):
    grid[i] = list(map(int, input().split()))
    for j in range(10):
        if(grid[i][j]==1):
            oneLocation.append((i,j))

visited = [[False] * 10 for i in range(10)]
ans = 3126 # 5의 5 승
one, two, three, four, five = 5,5,5,5,5


def isfill(grid, visited):
    for i in range(10):
        for j in range(10):
            if(grid[i][j]==1):
                if(not visited[i][j]):
                    return False
    return True


def isSquare(r, c, plus):
    if(r+plus>10 or c+plus >10):
        return False
    for i in range(r,r+plus):
        for j in range(c, c+plus):
            if(grid[i][j]!=1):
                return  False
    return True


def dfs(idx, cnt,one,two,three,four,five): # 1인 애들의 idx, 몇장썼는지, 색종이 몇장 남았는지
    global ans
    # if(ans<=cnt): # 더 탐색할 가치가 없으면 return 근데 isfill도 확인해 줘야함
    #     return # 그래서 일단 주석처리

    if(idx == len(oneLocation)): # 최솟값 갱신.
        print(idx, cnt,one,two,three,four,five)
        if(isfill(grid,visited)): # grid가 1인데 visited가 그 부분이 다 True면
            ans = min(ans,cnt)
        return

    r,c = oneLocation[idx]

    if(visited[r][c]):
        return

    # 한장은 무조건 가능
    # 검사해서 visited true 해주고 , 복구도 해줘야함.
    # 색종이 몇개썼는지도 ...
    if(one>0):
        visited[r][c] = True
        one-=1
        dfs(idx+1, cnt+1, one, two, three, four, five)
        visited[r][c] = False
        one += 1
        dfs(idx+1, cnt, one, two, three, four, five)


    if(two>0 and isSquare(r,c,2)):
        for i in range(r,r+2):
            for j in range(c,c+2):
                visited[i][j] = True
        two -=1
        dfs(idx + 1, cnt + 1, one, two, three, four, five)
        for i in range(r,r+2):
            for j in range(c,c+2):
                visited[i][j] = False
        two += 1
        dfs(idx + 1, cnt, one, two, three, four, five)


    if(three>0 and isSquare(r,c,3)):
        for i in range(r,r+3):
            for j in range(c,c+3):
                visited[i][j] = True
        three -=1
        dfs(idx + 1, cnt + 1, one, two, three, four, five)
        for i in range(r,r+3):
            for j in range(c,c+3):
                visited[i][j] = False
        three += 1
        dfs(idx + 1, cnt, one, two, three, four, five)

    if(four>0 and isSquare(r,c,4)):
        for i in range(r,r+4):
            for j in range(c,c+4):
                visited[i][j] = True
        four -=1
        dfs(idx + 1, cnt + 1, one, two, three, four, five)
        for i in range(r,r+4):
            for j in range(c,c+4):
                visited[i][j] = False
        four += 1
        dfs(idx + 1, cnt, one, two, three, four, five)


    if (five > 0 and isSquare(r, c, 5)):
        for i in range(r, r + 5):
            for j in range(c, c + 5):
                visited[i][j] = True
        five += 1
        dfs(idx + 1, cnt + 1, one, two, three, four , five)
        for i in range(r, r + 5):
            for j in range(c, c + 5):
                visited[i][j] = False
        five -= 1
        dfs(idx + 1, cnt, one, two, three, four, five)


dfs(0,0, one,two,three,four,five)

print(ans)