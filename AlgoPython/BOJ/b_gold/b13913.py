import heapq
from collections import deque

n,m = map(int, input().split())

visited = [-2]*100_001
visited[n] = -1
def dijk():
    q = deque([(0,n)])

    while q:
        cost, cur = q.popleft()
        if cur == m:
            print(cost)
            parent = visited[cur]
            ans = [cur]
            # 경로 추적
            while parent != -1:
                ans.append(parent)
                parent = visited[parent]
            print(*ans[::-1])
            return
        if cur-1>=0 and visited[cur-1] == -2:
            visited[cur-1] = cur # 부모 남겨주기
            q.append((cost+1,cur-1))
        if cur+1<100_001 and visited[cur+1] == -2:
            visited[cur+1] = cur # 부모 남겨주기
            q.append((cost+1,cur+1))
        if cur*2<100_001 and visited[cur*2] == -2:
            visited[cur*2] = cur # 부모 남겨주기
            q.append((cost+1,cur*2))

dijk()