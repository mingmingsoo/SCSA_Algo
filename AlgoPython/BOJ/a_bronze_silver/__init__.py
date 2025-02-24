'''
문제설명
    최소 개수의 동전을 옮겨서 새로운 모양을 만든다
구상
    이야 이거 어케하냐
     같은 모양이면 0 임
     1. 같은 모양인지 검사.
     2. 최소 동전 갯수는 합쳤을 때 안 겹쳐지는 애들임

'''

n1, m1 = map(int, input().split())
grid1 = [list(input()) for i in range(n1)]

n2, m2 = map(int, input().split())
grid2 = [list(input()) for i in range(n2)]


# grid1을 고정시키겠음
grid = [[0] * (m2 * 2 + m1) for i in range(n2 * 2 + n1)]
for i in range(n2, n2 + n1):
    for j in range(m2, m2 + m1):
        if (grid1[i - n2][j - m2] == "O"):
            grid[i][j] = -1

coin = 100000000
for i in range(0, n2 + n1 + 1):
    for j in range(0, m2 + m1 + 1):
        # print(i,j)
        # 얘네가 grid2의 시작점
        grid_copy = [_[:] for _ in grid]
        for x in range(i, i + n2):
            for y in range(j, j + m2):                # print(x,y)
                if (grid2[x - i][y - j] == "O"):
                    grid_copy[x][y] *= -1

        ele_coin = 0
        for row in grid_copy:
            ele_coin += row.count(-1)
        coin = min(ele_coin, coin)

print(coin)
