'''
두번째로 큰 수
풀이시간 6분
'''
n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]

while n > 1:
    new_grid = [[0] * (n // 2) for i in range(n // 2)]

    for i in range(0, n, 2):
        for j in range(0, n, 2):
            arr = [grid[i][j], grid[i][j + 1], grid[i + 1][j], grid[i + 1][j + 1]]
            arr.sort(reverse=True)
            maxi2 = arr[1]
            new_grid[i // 2][j // 2] = maxi2
    print("------------")
    for _ in new_grid:
        print(_)
    grid = new_grid
    n //= 2
print(grid[0][0])
