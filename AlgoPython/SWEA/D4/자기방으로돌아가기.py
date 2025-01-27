T = int(input())
for tc in range(T):
    n = int(input())

    list = [0]*201
    for i in range(n):
        x, y = map(int, input().split())
        if (x % 2 == 0):
            x = x // 2
        elif (x % 2 == 1):
            x = (x + 1) // 2
        if (y % 2 == 0):
            y = y // 2
        elif (y % 2 == 1):
            y = (y + 1) // 2

        start = min(x,y)
        end = max(x,y)
        for j in range(start, end+1):
            list[j] += 1
    ans = max(list)
    print(f"#{tc+1} {ans}")
