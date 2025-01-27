T = int(input())
for tc in range(T):
    n, m = map(int, input().split())

    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    if (n > m):
        n, m = m, n
        arr1, arr2 = arr2, arr1
    ans = 0

    startIdx = 0
    while (startIdx <= m - n):
        sum = 0
        for i in range(startIdx, startIdx + n):
            sum += (arr2[i] * arr1[i - startIdx])
        ans = max(ans, sum)
        startIdx += 1
    print(f'#{tc+1} {ans}')