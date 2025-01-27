T = int(input())
for tc in range(T):
    grid = [[0] * 10 for i in range(10)]

    n = int(input())

    for i in range(n):
        x1, y1, x2, y2, color = map(int, input().split())

        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                grid[i][j] += color

    purple = 0
    for i in range(0, 10):
        for j in range(0, 10):
            if (grid[i][j] == 3):
                purple += 1
    print(f"#{tc} {purple}")