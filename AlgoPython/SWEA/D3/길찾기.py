T = 10
for t in range(T):
    '''
    방향 그래프
    A-> B가능한지
    정점은 무조건 100개
    '''

    tnum, E = map(int, input().split())

    adj = [[] for i in range(100)]

    tmp = list(map(int, input().split()))
    for i in range(0, E * 2, 2):
        adj[tmp[i]].append(tmp[i + 1])

    ans = 0

    visited = [False] * 100


    def dfs(cur, end):
        global ans
        if (cur == end):
            ans = 1
            return
        visited[cur] = True
        for next in adj[cur]:
            if (not visited[next]):
                dfs(next, end)


    dfs(0, 99)
    print(f"#{tnum} {ans}")