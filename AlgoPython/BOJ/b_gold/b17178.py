'''
문제설명
    그 인하대 축제 문제랑 비슷
    대기열 관리

구상
    티켓 번호를 그냥 한번에 넘버링하기.

500번 틀린이유
	대기줄은 무한대만큼 들어올 수 있음..... 4명만 들어가지는 줄..저는 바보ㅖ요

'''
n = int(input())
tmp_grid = [list(input().split()) for i in range(n)]

tmp = []
for i in range(n):
    for j in range(5):
        alpha, number = tmp_grid[i][j].split("-")
        number = int(number)
        tmp.append((alpha, number))

tmp.sort()

grid = [[0] * 5 for i in range(n)]
for i in range(n):
    for j in range(5):
        alpha, number = tmp_grid[i][j].split("-")
        for w in range(5 * n):
            if alpha == tmp[w][0] and number == str(tmp[w][1]):
                grid[i][j] = w
                break

isOk = True

def do():
    global isOk

    exit = [[False] * 5 for i in range(n)]
    wait = []
    enter = 0

    for i in range(n):
        for j in range(5):
            if exit[i][j]:
                continue
            while grid[i][j] == enter or (wait and wait[0] == enter):
                if(grid[i][j] == enter):
                    enter += 1
                    exit[i][j] = True
                else:
                    wait.pop(0)
                    enter += 1
            if exit[i][j]:
                continue
            if grid[i][j] != enter:
                wait.insert(0, grid[i][j])
                exit[i][j] = True
    if wait:
        isOk = False
do()
if isOk:
    print("GOOD")
else:
    print("BAD")
