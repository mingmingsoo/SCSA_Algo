n = int(input())
whatRC = int(input())

# 목표로 하는 r,c
r = -1
c = -1

# 방향 순서 설정
row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]
grid = [[0] * n for i in range(n)]

d = 0 # 방향 설정

curR = n // 2 # 처음 시작점
curC = n // 2
num = 1
grid[curR][curC] = num
if (num == whatRC): # 만약 1이 목표값이면 여기서 해결해야함
    r = curR + 1
    c = curC + 1


def myPrint(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end = " ")
        print()


while (num < n * n):
    num += 1
    if (grid[curR + row[d]][curC + col[d]] == 0): # 방향대로 못가면 방향 변화시키지말고 유지
        curR += row[d]
        curC += col[d]
        grid[curR][curC] = num
        d = (d + 1) % 4
    else:
        d = (d - 1 + 4) % 4 # 방향 유지
        curR += row[d]
        curC += col[d]
        grid[curR][curC] = num
        d = (d + 1) % 4

    if (num == whatRC):
        r = curR + 1
        c = curC + 1
    print("------------")
    myPrint(grid)

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()
print(r, c)
