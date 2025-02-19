'''
구상을 하고싶었지만 머리가 안굴러가서 빡구현 했습니다.
광기 하드코딩ㅠ

1. 행을 무조건 5개로 고정되어있어서
주어지는 문자대로 5*len(문자길이//5) 배열을 만들고
#을 1로 채웠습니다.

2. 첫번째 행의 방문 체크만 확인해주면 돼서 1차원 visited 배열을 만들었습니다...

3. 0행만 검사하는데, 만약 열이 1이면 숫자가 뭔지 검사하고 방문체크를 해줘서 중복으로 체크하지 않게끔 했습니다.

4. 1일때가 좀 복병이라 열의 range 검사를 해줬습니다.


'''

N = int(input())
line = input()
n = 5 # 행
m = N // 5 # 열
grid = [[0] * (m) for i in range(n)]
num = 0

for s in line: # 배열 채우는 과정..
    i = num // m
    j = num % m
    if (s == "#"):
        grid[i][j] = 1
    num += 1

ans = []

jdx = 0
visited = [False] * m # 숫자를 중복되지 않게하기 위해서 방문체크 확인.

def is_number(j):
    # 모양대로 검사........
    if (j + 2 < m and
            grid[0][j] == 1 and grid[0][j + 1] == 1 and grid[0][j + 2] == 1 and
            grid[1][j] == 1 and grid[1][j + 1] == 0 and grid[1][j + 2] == 1 and
            grid[2][j] == 1 and grid[2][j + 1] == 0 and grid[2][j + 2] == 1 and
            grid[3][j] == 1 and grid[3][j + 1] == 0 and grid[3][j + 2] == 1 and
            grid[4][j] == 1 and grid[4][j + 1] == 1 and grid[4][j + 2] == 1):
        for jj in range(j, j + 3): # 방문체크는 해주고!
            visited[jj] = True
        return 0

    elif (j + 2 < m and
          grid[0][j] == 1 and grid[0][j + 1] == 1 and grid[0][j + 2] == 1 and
          grid[1][j] == 0 and grid[1][j + 1] == 0 and grid[1][j + 2] == 1 and
          grid[2][j] == 1 and grid[2][j + 1] == 1 and grid[2][j + 2] == 1 and
          grid[3][j] == 1 and grid[3][j + 1] == 0 and grid[3][j + 2] == 0 and
          grid[4][j] == 1 and grid[4][j + 1] == 1 and grid[4][j + 2] == 1):
        for jj in range(j, j + 3):
            visited[jj] = True
        return 2

    elif (j + 2 < m and
          grid[0][j] == 1 and grid[0][j + 1] == 1 and grid[0][j + 2] == 1 and
          grid[1][j] == 0 and grid[1][j + 1] == 0 and grid[1][j + 2] == 1 and
          grid[2][j] == 1 and grid[2][j + 1] == 1 and grid[2][j + 2] == 1 and
          grid[3][j] == 0 and grid[3][j + 1] == 0 and grid[3][j + 2] == 1 and
          grid[4][j] == 1 and grid[4][j + 1] == 1 and grid[4][j + 2] == 1):
        for jj in range(j, j + 3):
            visited[jj] = True
        return 3

    elif (j + 2 < m and
          grid[0][j] == 1 and grid[0][j + 1] == 0 and grid[0][j + 2] == 1 and
          grid[1][j] == 1 and grid[1][j + 1] == 0 and grid[1][j + 2] == 1 and
          grid[2][j] == 1 and grid[2][j + 1] == 1 and grid[2][j + 2] == 1 and
          grid[3][j] == 0 and grid[3][j + 1] == 0 and grid[3][j + 2] == 1 and
          grid[4][j] == 0 and grid[4][j + 1] == 0 and grid[4][j + 2] == 1):
        for jj in range(j, j + 3):
            visited[jj] = True
        return 4

    elif (j + 2 < m and
          grid[0][j] == 1 and grid[0][j + 1] == 1 and grid[0][j + 2] == 1 and
          grid[1][j] == 1 and grid[1][j + 1] == 0 and grid[1][j + 2] == 0 and
          grid[2][j] == 1 and grid[2][j + 1] == 1 and grid[2][j + 2] == 1 and
          grid[3][j] == 0 and grid[3][j + 1] == 0 and grid[3][j + 2] == 1 and
          grid[4][j] == 1 and grid[4][j + 1] == 1 and grid[4][j + 2] == 1):
        for jj in range(j, j + 3):
            visited[jj] = True
        return 5


    elif (j + 2 < m and
          grid[0][j] == 1 and grid[0][j + 1] == 1 and grid[0][j + 2] == 1 and
          grid[1][j] == 1 and grid[1][j + 1] == 0 and grid[1][j + 2] == 0 and
          grid[2][j] == 1 and grid[2][j + 1] == 1 and grid[2][j + 2] == 1 and
          grid[3][j] == 1 and grid[3][j + 1] == 0 and grid[3][j + 2] == 1 and
          grid[4][j] == 1 and grid[4][j + 1] == 1 and grid[4][j + 2] == 1):
        for jj in range(j, j + 3):
            visited[jj] = True
        return 6

    elif (j + 2 < m and
          grid[0][j] == 1 and grid[0][j + 1] == 1 and grid[0][j + 2] == 1 and
          grid[1][j] == 0 and grid[1][j + 1] == 0 and grid[1][j + 2] == 1 and
          grid[2][j] == 0 and grid[2][j + 1] == 0 and grid[2][j + 2] == 1 and
          grid[3][j] == 0 and grid[3][j + 1] == 0 and grid[3][j + 2] == 1 and
          grid[4][j] == 0 and grid[4][j + 1] == 0 and grid[4][j + 2] == 1):
        for jj in range(j, j + 3):
            visited[jj] = True
        return 7

    elif (j + 2 < m and
          grid[0][j] == 1 and grid[0][j + 1] == 1 and grid[0][j + 2] == 1 and
          grid[1][j] == 1 and grid[1][j + 1] == 0 and grid[1][j + 2] == 1 and
          grid[2][j] == 1 and grid[2][j + 1] == 1 and grid[2][j + 2] == 1 and
          grid[3][j] == 1 and grid[3][j + 1] == 0 and grid[3][j + 2] == 1 and
          grid[4][j] == 1 and grid[4][j + 1] == 1 and grid[4][j + 2] == 1):
        for jj in range(j, j + 3):
            visited[jj] = True
        return 8

    elif (j + 2 < m and
          grid[0][j] == 1 and grid[0][j + 1] == 1 and grid[0][j + 2] == 1 and
          grid[1][j] == 1 and grid[1][j + 1] == 0 and grid[1][j + 2] == 1 and
          grid[2][j] == 1 and grid[2][j + 1] == 1 and grid[2][j + 2] == 1 and
          grid[3][j] == 0 and grid[3][j + 1] == 0 and grid[3][j + 2] == 1 and
          grid[4][j] == 1 and grid[4][j + 1] == 1 and grid[4][j + 2] == 1):
        for jj in range(j, j + 3):
            visited[jj] = True
        return 9
    else:
        visited[j] = True # 1은 한 열만 차지해서 한열만 방문체크.
        return 1

while jdx < m:
    # 열만 팬다.
    if (not visited[jdx] and grid[0][jdx] == 1): # 너 숫자야?
        ans.append(is_number(jdx))
    jdx += 1 # 다음열 검사
print("".join(map(str, ans)))
