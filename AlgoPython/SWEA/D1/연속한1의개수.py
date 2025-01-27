T = int(input())
for t in range(T):
    n = int(input())
    arr = list(map(int, input()))

    ans = 0
    for i in range(n):
        if (arr[i] != 0):
            continue
        sum = 0
        for j in range(i + 1, n):
            if (arr[j] == 1):
                sum += 1
            else:
                break
        ans = max(sum, ans)
    print(f'#{t+1} {ans}')