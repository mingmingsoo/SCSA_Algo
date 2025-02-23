'''
문제설명
    디귿 반대모양의 컨베이어 벨트
    M개의 선물을 포장하기 위해 N명의 직원을 고용
    선물 포장하는 시간은 다 다름
    직원들은 상하좌우 벨트 포장 가능 ->. 더 오래된거 포장

'''

n, m, present = map(int, input().split()) # 맵 크기, 직원, 선물갯수
grid = [[0]*(n+1) for i in range(n)]
people = [[False]*(n+1) for i in range(n)]
people_origin = [[0]*(n+1) for i in range(n)]


for mm in range(m):
    r,c,t =map(int, input().split())
    grid[r][c+1] = t
    people[r][c+1] = True
    people_origin[r][c+1] = t


grid[0][0] = present

row2 = [1,0,-1,0]
col2 = [0,1,0,-1]

out = 0
# for _ in grid:
#     print(*_)
time = 0
while time<(n*2+n-2+present):
    time+=1
    #  올려!
    if(grid[0][0]>0):
        grid[0][1] = 1
        grid[0][0]-=1

    # 포장중인 애들은 포장만해.
    for i in range(1,n-1):
        for j in range(1,n):
            if people[i][j] and grid[i][j]!= people_origin[i][j]:
                grid[i][j] -=1


    # 숫자 이면서 visited가 True 인 데에서 상하 좌우에 숫자가 있으면 포장해
    for i in range(1,n-1):
        for j in range(1,n):
            if people[i][j] and grid[i][j]== people_origin[i][j]: # 상자포장가능
                for k in range(4):
                    nr = i + row2[k]
                    nc = j + col2[k]
                    if (grid[nr][nc] > 0 and not people[nr][nc]):
                        grid[nr][nc] = 0
                        grid[i][j] -= 1  # 포장중
                        break

    # 그리고 0이면 시간 채워줘
    for i in range(1,n-1):
        for j in range(1,n):
            if people[i][j] and grid[i][j]==0:
                grid[i][j] = people_origin[i][j]

    # 회전
    # 뒤에서부터 댕기기
    for j in range(n):
        grid[n-1][j] = grid[n-1][j+1]

    for i in range(n-1,-1,-1):
        grid[i][n] = grid[i-1][n]

    for j in range(n,1,-1):
        grid[0][j] = grid[0][j-1]
    grid[0][1] = 0

    # 떨어지는 애 검사
    if(grid[n-1][0]>0):
        out+=1





    # print("-------------")
    # for _ in grid:
    #     print(*_)

print(present-out)