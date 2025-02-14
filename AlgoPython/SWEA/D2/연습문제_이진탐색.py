T = int(input())
for tc in range(T):
    '''
    문제설명
        오름차순 배열 중 특정 숫자가 몇번쨰 위치에 있는가?
    '''

    n, target = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 0
    start, end = 0, n - 1

    while start <= end:
        middle = (start + end) // 2

        if (arr[middle] == target):
            ans = middle + 1
            break
        else:
            if (arr[middle] < target):
                start = middle + 1
            else:
                end = middle - 1
    print(f"#{tc+1} {ans}")