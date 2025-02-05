T = int(input())
for tc in range(T):
    '''
    풀었던 문제
    
    단방향
    노드들의 거리가 1000이하면 방문 가능함. -> 간선이 연결될 수 있음
    노드들에 idx 부여해서 idx 도달하면 happy
    
    '''

    store = int(input())
    adj = []  # 집,락, 그리고 편의점들
    hr, hc = map(int, input().split())
    adj.append((hr, hc, 0))
    for i in range(store):
        cr, cc = map(int, input().split())
        adj.append((cr, cc, i + 1))
    rr, rc = map(int, input().split())
    adj.append((rr, rc, store+1))

    ans = "sad"
    visited = [False] * (store + 2)

    def dfs(start, end):
        global ans

        visited[start] = True

        if (start == end):
            ans = "happy"
            return

        for i in range(store + 2):
            if (visited[i]):
                continue
            if (abs(adj[start][0] - adj[i][0]) + abs(adj[start][1] - adj[i][1]) <= 1000):
                dfs(i, end)


    dfs(0, store + 1)
    print(ans)