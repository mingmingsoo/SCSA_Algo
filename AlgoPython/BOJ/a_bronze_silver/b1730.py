'''
b1730
문제설명
    0,0에서 시작
    조각도가 패인 흔적 출력
    격자 밖 나가면 무시
구상
    숫자로 표시하고
    한번에 출력
    1 이면 수직 2 면 수평

새로 시작...
흔적을 두번 남기기.

반례
5
DRUL
'''

n = int(input())
order_line = list(input())
r, c = 0, 0
row = [-1, 1, 0, 0]
col = [0, 0, -1, 1]
xgrid = [[0] * n for i in range(n)]
ygrid = [[0] * n for i in range(n)]

for i in range(len(order_line)):
    order_line[i] = "UDLR".index(order_line[i])

for d in order_line:

    if(not(0<=r+row[d]<n and 0<=c+col[d]<n)):
        continue

    if (d == 0 or d == 1):
        xgrid[r][c] = 1
    else:
        ygrid[r][c] = 1

    r = r + row[d]
    c = c + col[d]
    if (d == 0 or d == 1):
        xgrid[r][c] = 1
    else:
        ygrid[r][c] = 1

for i in range(n):
    for j in range(n):
        if xgrid[i][j] == 1 and ygrid[i][j] == 1:
            print("+", end="")
        elif xgrid[i][j] == 1 and ygrid[i][j] == 0:
            print("|", end="")
        elif xgrid[i][j] == 0 and ygrid[i][j] == 1:
            print("-", end="")
        else:
            print(".", end="")
    print()
