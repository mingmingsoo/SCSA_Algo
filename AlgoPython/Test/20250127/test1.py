T = int(input())
for tc in range(T):
    arr = list(map(int, input()))
    # print(arr)
    cnt = 0
    for i in range(len(arr)):
        if (arr[i] == 1):
            cnt += 1
            for j in range(i, len(arr)):
                arr[j] = 1 - arr[j]
    print(f"#{tc+1} {cnt}")
