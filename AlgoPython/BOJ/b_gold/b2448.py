'''
이젠 규칙까지 유추하라네
'''
n = int(input())
arr = [[" "]*(n*2) for i in range(n)]

def star(n,r,c):
    if n == 3:
        arr[r][c+2] = "*"

        arr[r+1][c+1] = "*"
        arr[r+1][c+3] = "*"

        arr[r+2][c+0] = "*"
        arr[r+2][c+1] = "*"
        arr[r+2][c+2] = "*"
        arr[r+2][c+3] = "*"
        arr[r+2][c+4] = "*"

        return

    star(n//2,r,c+n//2) # 위
    star(n//2,r+n//2,c) # 아래 왼
    star(n//2,r+n//2,c+n) # 아래 오


star(n,0,0)
for _ in arr:
    print("".join(_))