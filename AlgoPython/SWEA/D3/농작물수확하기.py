T = int(input())
for tc in range(T):
    n = int(input())
    grid = [list(input()) for i in range(n)]

    for i in range(n):
        for j in range(n):
            grid[i][j] = int(grid[i][j])
    sum = 0
    # # 위에 세모
    # for i in range(n // 2):
    #     for j in range(n // 2 - i, n // 2 + (i + 1)):
    #         sum += grid[i][j]
    # # # 중간 한줄
    # for j in range(n):
    #     sum += grid[n // 2][j]
    # # # 아래 세모
    # for i in range(n - 1, n // 2, -1):  # 3
    #     for j in range(n // 2 - (n - i) + 1, n // 2 + (n - i)):  # 1 2 3 #
    #         sum += grid[i][j]
    arr = []
    # idx = 0
    # for i in range(n):
    #     if(i<n//2+1):
    #         arr.append(i)
    #     else:
    #         arr.append(n-i-1)
    #
    # for i in range(n):
    #     margin = arr[i]
    #     for j in range(n//2 - margin, n//2+margin+1):
    #         sum+=grid[i][j]

    size = n//2
    for i in range(n):
        for j in range(n):
            if(abs(i-size)+abs(j-size)<=size):
                sum+=grid[i][j]

    print(f"#{tc+1} {sum}")