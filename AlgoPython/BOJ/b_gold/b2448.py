import math

# for i in range(3): # 1
#     for j in range(3-i-1): # 0~2
#         print(" ", end= "")
#     for j in range(2*i+1): #0~3
#         if (i % 2 == 1 and j % 2 == 1):
#             print(" ", end="")
#         else:
#             print("*", end = "")
#     print()
#
n = int(input())

stars = [[" "]* (2*n-1) for i in range(n)]


def star(r, c, n):
    if(n==3):
        stars[r][c] = '*'
        stars[r+1][c-1] = stars[r+1][c+1] = '*'
        stars[r+2][c-2] =stars[r+2][c-1]=stars[r+2][c]=stars[r+2][c+1] = stars[r+2][c+2] = '*'
        return
    else:
        cut = n//2
        star(r,c,cut)
        star(r+cut, c-cut, cut)
        star(r+cut, c+cut, cut)


star(0,n-1,n) # 꼭대기 별이 n-1 에 위치


for i in range(n):
    for j in range(2*n-1):
        print(stars[i][j], end = "")
    print()