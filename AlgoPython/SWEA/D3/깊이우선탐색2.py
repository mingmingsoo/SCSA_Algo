T = int(input())


def dfs(start):
    ans = []  # 방문값을 넣어주는 배열
    stk = []  # 초깃값 설정
    visited = [False] * (V + 1)
    stk.append(1)
    while True:
        cur = stk.pop()
        visited[cur] = True
        ans.append(cur)

        for next in adj[cur]:
            if(not visited[next]):
                stk.append(next)
            break
        if(stk):
           cur = stk.pop()




for tc in range(T):
    '''
    강사님 풀이
    '''

    V, E = map(int, input().split())
    adj = [[] for i in range(V + 1)]
    for i in range(E):
        start, end = map(int, input().split())
        adj[start].append(end)
        adj[end].append(start)
    for row in adj:
        row.sort()  # stack으로 풀 때는 반대로!
        # 1의 노드 2,3에서 stk 에 3,2 넣어야 뽑아낼 때 2, 3 순으로 뽑음


    print(f"#{tc + 1}", end=" ")

    dfs(1)

    for x in ans:
        print(x, end=" ")



    print()