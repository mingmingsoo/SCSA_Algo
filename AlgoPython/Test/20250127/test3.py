T = int(input())
for tc in range(T):
    n = int(input())
    arr = list(map(int, input().split()))

    max = arr[-1]
    ans = 0
    for i in range(len(arr) - 2, -1, -1):
        if (arr[i] < max):
            ans += (max - arr[i])
        else:
            max = arr[i]
    print(f"#{tc+1} {ans}")