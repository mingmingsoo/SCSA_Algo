'''
약간 재귀같은데
'''
n = int(input())
arr = [[" "] * (5 ** n) for i in range(5 ** n)] # 배열 먼저 만들어준다.
# 서현코드보고 파이썬에 감탄했다..

def star(n, r, c):
    if n == 0:
        arr[r][c] = "*"
        return

    star(n - 1, r * 5 + 0, c * 5 + 2)
    star(n - 1, r * 5 + 1, c * 5 + 2)
    for j in range(5):
        star(n - 1, r * 5 + 2, c * 5 + j)
    for j in range(1,4):
        star(n - 1, r * 5 + 3, c * 5 + j)
    star(n - 1, r * 5 + 4, c * 5 + 1)
    star(n - 1, r * 5 + 4, c * 5 + 3)

star(n, 0, 0)

for row in arr:
    print("".join(row))
