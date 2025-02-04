T = int(input())

for tc in range(T):
    '''
    양방향
    최소 몇개 -> bfs
    end되면 그냥 return 처리
    도달 못하면 0출력
    '''

    V, E = map(int, input().split())

    adj = [[] for i in range(V + 1)]

    for i in range(E):
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)
    start, end = map(int, input().split())


    def bfS(start, end):
        visited = [False] * (V + 1)
        visited[start] = True
        q = [(start, 0)]  # 정점과 이동 횟수

        while q:
            cur, cnt = q.pop(0)
            if (cur == end):
                print(f"#{tc+1} {cnt}")
                return
            for node in adj[cur]:
                if (not visited[node]):
                    q.append((node, cnt + 1))
                    visited[node] = True
        print(f"#{tc+1} 0") # 이거안해서 틀렸음

    bfS(start, end)