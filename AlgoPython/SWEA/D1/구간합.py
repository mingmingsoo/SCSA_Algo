T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    min = float('inf')
    max = 0
    for i in range(0, n - m + 1):
        sum = 0
        for j in range(i, i + m):
            sum += arr[j]
        if (min > sum):
            min = sum
        if (max < sum):
            max = sum
    print(f'#{t+1} {max - min}')
