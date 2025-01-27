T = int(input())
for tc in range(T):
    import copy

    n = int(input())

    arr = [1, 1] + [0] * (n - 2)
    # print(arr)
    length = 2
    print(f'#{tc + 1}')
    print(1)
    while (length <= n):
        tmparr = arr[:]
        for i in range(1, n - 1):
            tmp = tmparr[i - 1] + tmparr[i]
            arr[i] = tmp
        arr[length - 1] = 1
        length += 1
        for i in range(length-1):
            print(arr[i], end = " ")
        print()