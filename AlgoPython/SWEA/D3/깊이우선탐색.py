T = int(input())
for tc in range(T):
    '''
    재귀가 아닌 stack으로 풀기
    -> 모르겠읍니다...
    -> 재귀로 풀었습니다
    -> 스택으로 다시 풀어보겠습니다..
    '''

    V, E = map(int, input().split())
    adj = [[] for i in range(V + 1)]
    for i in range(E):
        start, end = map(int, input().split())
        adj[start].append(end)
        adj[end].append(start)
    for row in adj:
        row.sort(reverse=True)  # stack으로 풀 때는 반대로!
        # 1의 노드 2,3에서 stk 에 3,2 넣어야 뽑아낼 때 2, 3 순으로 뽑음
    visited = [False] * (V + 1)


    print(f"#{tc + 1}", end=" ")
    ans = []  # 방문값을 넣어주는 배열
    stk = [1]  # 초깃값 설정

    while stk:
        cur = stk.pop()
        if(visited[cur]):
            continue
        visited[cur] = True
        ans.append(cur)
        for next in adj[cur]:
            stk.append(next)

    for x in ans:
        print(x, end=" ")

    # def dfs(cur):
    #     visited[cur] = True
    #     print(cur, end=" ")
    #     for node in adj[cur]:
    #         if (not visited[node]):
    #             dfs(node)
    # dfs(1)

    print()