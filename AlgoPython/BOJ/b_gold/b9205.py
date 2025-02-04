'''
한 박스에 20개
50미터에 한 병씩(마시고 출발)

편의점을 다 갈 수 있는게 아니라 한곳만 갈 수 있나봄.??
'''

T = int(input())


def dfs(start, end):
    global ans
    visited[start] = True
    r, c, idx = dist[start]

    if (idx == end):
        ans = "happy"
        return

    for i in range(store + 2):
        if (i == start):
            continue
        nr, nc, nidx = dist[i]
        if (not visited[i] and abs(nr - r) + abs(nc - c) <= 1000):
            dfs(i, end)


for tc in range(T):
    store = int(input())
    visited = [False] * (store + 2)
    dist = []
    hr, hc = map(int, input().split())
    dist.append((hr, hc, 0))
    for i in range(1, store + 1):
        sr, sc = map(int, input().split())
        dist.append((sr, sc, i))
    fr, fc = map(int, input().split())
    dist.append((fr, fc, store + 1))

    ans = "sad"
    dfs(0, store + 1)
    print(ans)
