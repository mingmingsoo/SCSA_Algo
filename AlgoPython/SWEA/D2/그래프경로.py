import sys
sys.setrecursionlimit(10**6)
T = int(input())


def stack(start, end):
    global ans
    cur = start
    stk = [start]
    while True:
        visited[cur] = True
        if (cur == end):
            ans = 1
            return
        for next in adj[cur]:
            if(not visited[next]):
                cur = next
                stk.append(next)
                break #  이거 줄넘김 안돼서 안됐었음..ㅜㅠㅠㅠ
        else:
            if(stk):
                cur = stk.pop()
            else:
                return


for tc in range(T):
    '''
    방향 그래프
    특정 두개 노드가 연결 됐는가?
    됐으면 1 아니면 0
    '''

    V, E = map(int, input().split())
    adj = [[] for i in range(V + 1)]
    for i in range(E):
        start, end = map(int, input().split())
        adj[start].append(end)  # 방향있으므로 한쪽으로만 넣어줌
    start, end = map(int, input().split())
    ans = 0
    visited = [False] * (V + 1)


    # def dfs(cur, end):
    #     global ans
    #     if (cur == end):
    #         ans = 1
    #         return
    #     visited[cur] = True
    #     for next in adj[cur]:
    #         if (not visited[next]):
    #             dfs(next, end)

    # dfs(start, end)
    stack(start,end)

    print(f"#{tc+1} {ans}")
