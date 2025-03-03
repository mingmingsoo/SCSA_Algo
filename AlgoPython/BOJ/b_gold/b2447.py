# 별찍기 왕이 되것서요

n = int(input())
arr = [[" "] * n for i in range(n)]

def star(n,r,c):
    if n == 1:
        arr[r][c] = "*"
        return

    star(n//3, r*3, c*3)
    star(n//3, r*3, c*3+1)
    star(n//3, r*3, c*3+2)

    star(n//3, r*3+1, c*3)

    star(n//3, r*3+1, c*3+2)

    star(n//3, r*3+2, c*3)
    star(n//3, r*3+2, c*3+1)
    star(n//3, r*3+2, c*3+2)



star(n,0,0)
for row in arr:
    print("".join(row))