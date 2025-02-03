'''
문제 시작: 18:50
문제 중단 19:10
문제 다시 시작 19:48
시간 의미가 없음 걍 오래걸림.......

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

무조건 큰 거 덮으면 되는거 아니야? 했지만
이 경우에 무조건 큰걸로 하면 안됨. 다 따져줘야함.

1일때 좌표를 다 담고,
그 좌표들마다 1~5 색종이를 덮었을 경우의 수 계산
재귀할 때 : 중복되게 덮힌 부분이 없는지 확인. -> 중복됐으면 다시 취소하고 돌아가야함.

'''
import sys
input = sys.stdin.readline

oneLocation = []
grid = [[] for i in range(10)]
for i in range(10):
    grid[i] = list(map(int, input().split()))
    for j in range(10):
        if (grid[i][j] == 1):
            oneLocation.append((i, j))

visited = [[False] * 10 for i in range(10)]
ans = 3126  # 5의 5 승
one, two, three, four, five = 5, 5, 5, 5, 5


def isfill(grid, visited):
    for i in range(10):
        for j in range(10):  # 1인데 안채워져있으면...
            if (grid[i][j] == 1 and not visited[i][j]):
                return False
    return True


def isSquare(r, c, plus):
    if (r + plus >= 11 or c + plus >= 11):
        return False
    for i in range(r, r + plus):
        for j in range(c, c + plus):
            if(visited[i][j]): # 이거 없으면 색종이 겹쳐서 채워지는 건데 캐치를 못해서 틀렸슴
                return False
            if (grid[i][j] != 1):
                return False
    return True


def dfs(idx, cnt, one, two, three, four, five):  # 1인 애들의 idx, 몇장썼는지, 색종이 몇장 남았는지
    global ans
    if (ans <= cnt):  # 더 탐색할 가치가 없으면 return 이거 없으면 시초남
        return

    if (idx >= len(oneLocation)):  # 최솟값 갱신.
        # print(idx, cnt,one,two,three,four,five)

        if (isfill(grid, visited)):  # grid가 1인데 visited가 그 부분이 다 True면 = 조건을 만족했으면
            ans = min(ans, cnt)
        return

    r, c = oneLocation[idx]

    if (visited[r][c]):  # 이미 덮혔으면 넘어가..
        dfs(idx + 1, cnt, one, two, three, four, five)  # 이게 없어서 해맸음
        return

    # 한장은 무조건 가능
    # 검사해서 visited true 해주고 , 복구도 해줘야함.
    # 색종이 몇개썼는지도 ...
    if (five > 0 and isSquare(r, c, 5)):
        # 방문체크
        for i in range(r, r + 5):
            for j in range(c, c + 5):
                visited[i][j] = True
        # 다음 1번으로 넘어가
        dfs(idx + 1, cnt + 1, one, two, three, four, five - 1)
        # 방문체크해제
        for i in range(r, r + 5):
            for j in range(c, c + 5):
                visited[i][j] = False
    if (four > 0 and isSquare(r, c, 4)):
        for i in range(r, r + 4):
            for j in range(c, c + 4):
                visited[i][j] = True
        dfs(idx + 1, cnt + 1, one, two, three, four - 1, five)
        for i in range(r, r + 4):
            for j in range(c, c + 4):
                visited[i][j] = False

    if (three > 0 and isSquare(r, c, 3)):
        for i in range(r, r + 3):
            for j in range(c, c + 3):
                visited[i][j] = True
        dfs(idx + 1, cnt + 1, one, two, three - 1, four, five)
        for i in range(r, r + 3):
            for j in range(c, c + 3):
                visited[i][j] = False
    if (two > 0 and isSquare(r, c, 2)):
        for i in range(r, r + 2):
            for j in range(c, c + 2):
                visited[i][j] = True
        dfs(idx + 1, cnt + 1, one, two - 1, three, four, five)
        for i in range(r, r + 2):
            for j in range(c, c + 2):
                visited[i][j] = False
    if (one > 0):
        visited[r][c] = True
        dfs(idx + 1, cnt + 1, one - 1, two, three, four, five)
        visited[r][c] = False





dfs(0, 0, one, two, three, four, five)
if (ans == 3126):
    ans = -1
print(ans)
