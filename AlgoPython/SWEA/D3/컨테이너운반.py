T = int(input())
for tc in range(T):
    '''
    [구상]
    화물 내림차순, 트럭 오름차순 해서 매칭해준다!!
    '''

    n, m = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    container.sort(reverse=True)
    truck.sort(reverse=True)

    weight = 0

    # 자꾸 런타임 에러가 나네요....
    ci = 0  # 컨테이너 인덱스
    for i in range(m):
        if (ci < n):
            while ci< n and container[ci] > truck[i]:
                # 여기오면 못담는 컨테이너임 다음 컨테이너 탐색
                ci+=1
            if (ci<n and container[ci] <= truck[i]):
                weight += container[ci]
                ci += 1
                continue
        else:
            break


    # for i in range(m): # 트럭
    #     while container:
    #         if(truck[i]>= container[0]):
    #             weight+=container[0]
    #             container.pop(0)
    #             break # 다음 트럭으로 넘어가
    #         else:
    #             container.pop(0) # 다음컨테이너로 넘어가

    print(f"#{tc+1} {weight}")
