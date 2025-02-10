import sys
input = sys.stdin.readline
while True:
    n, m = map(int, input().split())
    if(n ==0 and m ==0):
        break
    arr = list(map(int, input().split()))
    size = max(arr)

    child_list = [[] for i in range(size + 1)] # 자식들을 담음
    parent_list = [0] *(size + 1)  # 부모들을 담음

    i = 0
    visited = [False] * (size + 1)
    mother = 0
    while (i < n):
        parent = arr[i]
        visited[parent] = True
        start, end = i + 1, i + 1
        for j in range(i + 1, n - 1):
            if (visited[arr[j]]):
                start += 1
                end += 1
                continue
            if (arr[j] + 1 == arr[j + 1]):
                start = min(start, j)
                end = max(end, j + 1)
            else:
                break
        # print(parent, start,end)
        for j in range(start, end + 1):
            if (j >= n):
                continue
            if (visited[arr[j]]):
                continue
            child_list[parent].append(arr[j])
            parent_list[arr[j]]=parent
            if (arr[j] == m):
                mother = parent # 엄마
            visited[arr[j]] = True
        i += 1


    # 할머니.
    grandmother = 0
    if(not parent_list[mother]): # 알고보니 엄마가 외동.
        print(0)
        # exit()
        continue
    else:
        grandmother = parent_list[mother] # 아니라면 할머니 누구야

    # 할머니 손주들 수
    cousin = 0
    for child in child_list[grandmother]:
        if(child != mother): # 우리 엄마 빼고 삼촌들
            cousin += len(child_list[child]) # 자식수 몇명이야

    print(cousin)
