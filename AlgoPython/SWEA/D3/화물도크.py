T = int(input())
for tc in range(T):
    '''
    [구상]
    스케쥴을 1. 도착시간이 작은순 2. 출발시간이 작은순 으로 정렬해서
    끝나는 지점과 최대의 갯수를 갱신하며 계산한다.

    [헷갈렸떤 점]
    출발시간으로 오름차순 하려고 했는데
    1 10000 이면.. 다음것도 다탐색해줘야하므로 (이중포문 필요)
    도착시간으로 오름차순 하면 된다.

    '''

    n = int(input())
    arr = []
    for i in range(n):
        s, e = map(int, input().split())
        arr.append((s, e))

    arr.sort(key=lambda x: (x[1], x[0]))
    # print(arr)

    end = 0
    cnt = 0
    for s, e in arr:
        if end <= s:  # 끝나는 시간이 시작시간하고 안겹치면
            end = e  # 끝나는 시간을 다음 스케쥴 끝나는 시간으로 변경한다
            cnt += 1  # 스케쥴 +1 획득
    print(f"#{tc+1} {cnt}")