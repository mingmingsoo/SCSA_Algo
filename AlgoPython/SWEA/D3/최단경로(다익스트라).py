T = int(input())
for tc in range(T):
    import heapq

    V, E = map(int, input().split())

    adj = [[] for i in range(V)]

    for i in range(E):
        s, e, cost = map(int, input().split())
        adj[s].append((cost,e))

    d = [10 * 1000 * 50 + 1] * V  # 큰 값
    d[0] = 0  # 시작값


    def dijk(start, end):
        q = []
        heapq.heappush(q, (0,start))

        while q:
            cost, cur = heapq.heappop(q)
            if (cost > d[cur]):
                continue

            for next_dist, next in adj[cur]:
                if (d[next] > cost + next_dist):
                    d[next] = cost + next_dist
                    heapq.heappush(q,(cost + next_dist,next))


    dijk(0, V - 1)
    print(f"#{tc+1} {d[V - 1]}")