'''
각 구역을 두개의 선거구로 나눔
선거구는 구역을 적어도 하나 포함
한 선거구에 포함된 구역은 연결 되어있어어ㅑ함.
인구 차이 최소값?
'''
V = int(input())
people = list(map(int, input().split()))
adj = [[] for i in range(V)]
for v in range(V):
    tmp = list(map(int, input().split()))
    for i in range(1, len(tmp)):
        adj[v].append(tmp[i] - 1)

# 0~v까지를 어떻게 나눌거냐면
# 1, 2를 중복순열로 백트래킹 할거에요
sel = [0] * V
ans = int(1e9)


def dfs(cur, visited, diff_arr):
    for next in adj[cur]:
        if not visited[next] and next not in diff_arr:
            visited[next] = True
            dfs(next, visited, diff_arr)


def perm(idx):
    global ans
    if idx == V:
        if sel.count(0) == V or sel.count(1) == V:
            return
        # 연결됐는지 검증
        A = []
        B = []
        for i in range(V):
            if sel[i] == 0:
                A.append(i)
            else:
                B.append(i)
        visited = [False] * V
        cnt = 0
        for idx in A:
            if not visited[idx] and cnt == 0:
                visited[idx] = True
                dfs(idx, visited, B)
                cnt += 1
            if not visited[idx] and cnt > 0:
                return  # 연결 안됨

        visited = [False] * V
        cnt = 0
        for idx in B:
            if not visited[idx] and cnt == 0:
                visited[idx] = True
                dfs(idx, visited, A)
                cnt += 1
            if not visited[idx] and cnt > 0:
                return  # 연결 안됨
        # print("A:", end =" ")
        # for num in A:
        #     print(num +1, end = ", ")
        # print("B:", end=" ")
        # for num in B:
        #     print(num +1, end = ", ")
        # print()
        # 여까지 왔으면 연결됐음
        a = b = 0
        for idx in A:
            a += people[idx]
        for idx in B:
            b += people[idx]

        ans = min(ans, abs(a - b))
        return
    for i in (0, 1):
        sel[idx] = i
        perm(idx + 1)


perm(0)
if ans == int(1e9):
    print(-1)
else:
    print(ans)
