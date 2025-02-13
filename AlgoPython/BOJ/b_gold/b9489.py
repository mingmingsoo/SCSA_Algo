import sys
input = sys.stdin.readline
while True:
    n, m = map(int, input().split())
    if(n ==0 and m ==0):
        break
    arr = list(map(int, input().split()))
    size = max(arr)
    # size = 40
    adj = [[] for i in range(size + 1)]
    parent_map = {} # 각 노드들의 부모 저장.
    myparent = 0
    i = 0
    visited = [False] * (size + 1)

    # 트리 만들기. 이게 구현문제가 아닐까?
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
            adj[parent].append(arr[j])
            parent_map[arr[j]] = parent
            if (arr[j] == m):
                myparent = parent
            visited[arr[j]] = True
        i += 1
    cousin = 0
    # 사촌 찾기
    # print(parent_map)
    # print(myparent)
    if myparent in parent_map:
        grandparent = parent_map[myparent]
        for uncle in adj[grandparent]:
            if(uncle!=myparent):
                cousin+=len(adj[uncle])
    print(cousin)
