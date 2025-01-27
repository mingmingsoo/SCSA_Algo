T = 10
for tc in range(T):
    '''
    덤프 횟수 내에 평탄화를 하고
    만약 덤프 횟수 내 평탄화가 된다면 차이 완료 , break

    출력 최고점-최저점
    '''

    end = int(input())
    arr = list(map(int, input().split()))

    start = 1
    ans = 0
    while (start <= end):
        maxNum = max(arr)
        minNum = min(arr)
        # print(maxNum, minNum)
        if (maxNum - minNum <= 1):
            break
        arr[arr.index(maxNum)] -= 1
        arr[arr.index(minNum)] += 1
        start += 1
        # print(arr)
    print(f'#{tc+1} {max(arr)-min(arr)}')




