T = int(input())
for tc in range(T):
    '''
    후위순회해라
    왼 오 루트
    '''

    N, m, l = map(int, input().split())  # 노드갯수, 리프노드갯수, 출력할 번호

    arr = [0] * (N + 1)

    for i in range(m):
        node, num = map(int, input().split())
        arr[node] = num

    for i in range(N, 0, -1):  # //2 이므로 좌 우 합이 arr[i//2]에 합산됨
        arr[i // 2] += arr[i]
    print(f"#{tc+1} {arr[l]}")