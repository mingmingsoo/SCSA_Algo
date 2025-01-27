T = int(input())
for tc in range(T):
    grid = [["."] * 15 for i in range(5)]

    for i in range(5):
        line = input()
        for j in range(len(line)):
            grid[i][j] = line[j]

    # print(grid)
    print(f"#{tc+1}", end = " ")
    for j in range(15):
        for i in range(5):
            if (grid[i][j] != "."):
                print(grid[i][j], end="")
    print()