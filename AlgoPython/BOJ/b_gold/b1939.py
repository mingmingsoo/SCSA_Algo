'''
목적지 -> 도착지를 가는데
최대 무게 위주로 가는데 그중 최솟값
다익스트라를 최댓값 버전으로

4 4
1 2 3
2 3 3
3 4 3
1 4 2
1 4
정답 3


4 4
1 2 3
2 3 2
3 4 3
1 4 1
1 4
정답 2

4 4
1 2 3
2 3 3
3 4 3
1 4 10
1 4
정답 10

4 5
1 3 1
1 2 10
1 4 2
4 2 10
3 4 4
1 3
정답 4

'''
import heapq

V, E = map(int, input().split())

adj = [[] for i in range(V + 1)]
for e in range(E):
    s, e, limit = map(int, input().split())
    adj[s].append((limit, e))
    adj[e].append((limit, s))
start, end = map(int, input().split())
for row in adj:
    row.sort(reverse=True)
ans = 0

def bfs():
    global ans
    visited = [0] * (V + 1)
    q = []
    heapq.heappush(q, (-int(1e9), start))

    while q:
        weight, cur = heapq.heappop(q)
        weight *= -1

        if cur == end:
            ans = weight
            return

        for next in adj[cur]:
            node = next[1]
            next_weight = next[0]
            w = min(weight, next_weight)
            if visited[node] < w:
                visited[node] = w
                heapq.heappush(q, (-w, node))

bfs()

print(ans)
