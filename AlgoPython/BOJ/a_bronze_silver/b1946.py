T = int(input())
for tc in range(T):
    '''
    [문제 설명]
        다른 모든 지원자와 비교했을 때 2가지 점수 중 적어도 하나가 다른 지원자보다 떨어지지 않으면ㅅ ㅓㄴ발
        A의 성적이 다른 어떤 지원자 B에 비해 모두 떨어지면 안뽑느다.
    [구상]
        모두 오름차순 해서
        나보다 둘 다 낮은애들 있는지 검사한다.
        그리고 idx를 변경해준다.
    '''

    n = int(input())
    arr = []
    for i in range(n):
        a, b = map(int, input().split())
        arr.append((a, b))

    arr.sort()  # 모두 오름차순으로
    out = 0  # 떨어지는 애들 숫자를 세준다.
    idx = 0  # 몇번째 애를 탐색하는지
    # print(arr)
    while idx < n:
        isOut = False
        end = idx  # 마지막 탐색한 애를 기준으로 idx를 넘겨줄 것임
        for i in range(idx + 1, n):
            if (arr[idx][0] < arr[i][0] and arr[idx][1] < arr[i][1]):
                out += 1
                isOut = True
                end = i  # 다음 탐색할 애들을 계속 갱신해줌
            else:
                break
        idx = end + 1  # 탈락한 애 다음으로 넘어간다.
    print(n - out)
