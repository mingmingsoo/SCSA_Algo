c, r = map(int, input().split())
num = int(input())

grid = [[0] * c for i in range(r)]
# for row in grid:
#     print(*row)

ridx = r - 1
cidx = 0
row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]
d = 0
n = 1
grid[ridx][cidx] = n
ansX = -1
ansY = -1
while n < r * c:

    n += 1
    if (0 > ridx + row[d] or ridx + row[d] >= r or 0 > cidx + col[d] or cidx + col[d] >= c or grid[ridx + row[d]][
        cidx + col[d]] != 0):
        d = (d + 1) % 4
    ridx = ridx + row[d]
    cidx = cidx + col[d]
    grid[ridx][cidx] = n
    if(n==num):
        ansX = r-ridx
        ansY = cidx+1
# for row in grid:
#     print(*row)
if(ansX == -1 and ansY == -1):
    if(num!=1):
        print(0)
    else:
        print("1 1")
else:
    print(ansY, ansX)
