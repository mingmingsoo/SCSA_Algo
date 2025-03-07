'''
무방향 그래프
1 -> N 까지 가야되는데
a, b 를 들러야함
1 ~ a
a~ b
b~ N

구하거나

1~b
b~a
a~N

10 4
1 2 3
1 3 4
2 3 1
10 1 7
2 4
반례 -1

틀린이유
(v1 ≠ v2, v1 ≠ N, v2 ≠ 1)
이런 ... A = 1, B = V 일수도있음 ;;
'''
import heapq

V, E = map(int, input().split())
adj = [[] for i in range(V + 1)]
for e in range(E):
    s, e, cost = map(int, input().split())
    adj[s].append((cost, e))
    adj[e].append((cost, s))
a, b = map(int, input().split())


def dijk(start, end):
    d = [int(1e9)] * (V + 1)
    d[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        cost, cur = heapq.heappop(q)
        if cur == end:
            return cost
        if cost > d[cur]:
            continue
        for next_cost, next in adj[cur]:
            if d[next] > next_cost + cost:
                d[next] = next_cost + cost
                heapq.heappush(q, (next_cost + cost, next))
    return -1 # 길 없으면 -1 출력


ans11 = dijk(1, a)
ans12 = dijk(a, b)
ans13 = dijk(b, V)

ans21 = dijk(1, b)
ans22 = dijk(b, a)
ans23 = dijk(a, V)

if ans11 == -1 or ans12 == -1 or ans13 == -1 or ans21 == -1 or ans22 == -1 or ans23 == -1:
    print(-1) # 길없으면 -1
else:
    ans1 = ans11 + ans12 + ans13
    ans2 = ans21 + ans22 + ans23
    print(min(ans1, ans2))
