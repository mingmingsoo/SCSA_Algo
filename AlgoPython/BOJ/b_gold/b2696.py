T = int(input()) # 테케 안써서 틀렸음
for tc in range(T):
    import heapq

    n = int(input())
    mok_ = n // 10
    mod_ = n % 10
    arr = []
    for i in range(mok_):
        tmp = list(map(int, input().split()))
        for j in range(10):
            arr.append(tmp[j])
    tmp = list(map(int, input().split()))
    for x in tmp:
        arr.append(x)

    # # 앞에껄 빼줄거임.
    # pq 하나만 쓰면 좋지만... 조회하는 함수가 없어서 큰거/작은거 나눠줘야함.
    # bigger = () # 나보다 크면 여기 넣어줌 -> 작은애 빼줌(최소힙)
    # smaller =  () # 나보다 작으면 여기 넣어주고 -> 큰애 빼줌(최대힙)
    # 그래서 smaller에 넣어줄 때는 - 붙여서 넣어주고 뺄떄도 - 붙여서 빼줘야함!!

    small_pq = []
    big_pq = []
    middle = arr[0]
    print(n // 2 + 1)
    ans = [arr[0]]
    for i in range(1, n):
        if (arr[i] > middle):
            heapq.heappush(big_pq, arr[i])
        else:
            heapq.heappush(small_pq, -arr[i])

        if (i % 2 == 0):  # 홀수번째면 내가 중앙값인지 검사 small과 big size가 같은지
            if (len(small_pq) == len(big_pq)):
                pass
            elif (len(small_pq) > len(big_pq)):
                heapq.heappush(big_pq, middle)
                middle = -heapq.heappop(small_pq)
            else:
                heapq.heappush(small_pq, -middle)  # 여기도 middle에 - 붙혀서 넣어야함
                middle = heapq.heappop(big_pq)
            ans.append(middle)

    for i in range(n // 2 + 1):
        if (i != 0 and i % 10 == 0):
            print()
        print(ans[i], end=" ")
    print()



